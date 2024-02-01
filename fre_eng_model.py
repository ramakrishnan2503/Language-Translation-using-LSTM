import joblib
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
import numpy as np

#fretoengmodel = tf.keras.models.load_model(r"D:\Language Translator using LSTM\Models\FrenchToEnglish.h5")
encoder_model = tf.keras.models.load_model(r"D:\Language Translator using LSTM\Models\fr-enencoder.h5")
decoder_model = tf.keras.models.load_model(r"D:\Language Translator using LSTM\Models\fr-endecoder.h5")
input_tokenizer = joblib.load(r"D:\Language Translator using LSTM\Models\fr-enInputTokenizer.pkl")
output_tokenizer = joblib.load(r"D:\Language Translator using LSTM\Models\fr-enOutputTokenizer.pkl")


max_input_len = 10
word2idx_inputs = input_tokenizer.word_index
word2idx_outputs = output_tokenizer.word_index
max_out_len = 6
idx2word_input = {v:k for k, v in word2idx_inputs.items()}
idx2word_target = {v:k for k, v in word2idx_outputs.items()}

def fre_eng(input_val):
        def translate_sentence(input_seq):
                states_value = encoder_model.predict(input_seq)
                target_seq = np.zeros((1, 1))
                target_seq[0, 0] = word2idx_outputs['<sos>']
                eos = word2idx_outputs['<eos>']
                output_sentence = []

                for _ in range(max_out_len):
                        output_tokens, h, c = decoder_model.predict([target_seq] + states_value)
                        idx = np.argmax(output_tokens[0, 0, :])

                        if eos == idx:
                                break

                        word = ''

                        if idx > 0:
                                word = idx2word_target[idx]
                                output_sentence.append(word)

                                target_seq[0, 0] = idx
                                states_value = [h, c]

                return ' '.join(output_sentence)

        # Assume 'input_sentence' is the sentence you want to translate
        input_sentence = input_val

        # Tokenize and pad the input sentence
        input_sequence = input_tokenizer.texts_to_sequences([input_sentence])
        input_sequence_padded = pad_sequences(input_sequence, maxlen=max_input_len)

        # Translate the sentence
        translation = translate_sentence(input_sequence_padded)

        # Print the results
        print('Input:', input_sentence)
        print('Translation:', translation)
        return input_sentence,translation

