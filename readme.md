# Multilingual Language Translation using LSTM

This project implements a Language Translation system using Long Short-Term Memory (LSTM) networks. The model is trained to perform translation between English and multiple languages, including Tamil, French, and Spanish.

## Technologies Used

- **LSTM Model:** The core of the translation is based on the LSTM (Long Short-Term Memory) neural network architecture, providing a solid foundation for sequence-to-sequence learning.

- **Streamlit:** The application leverages Streamlit, a user-friendly Python library for creating web applications with minimal effort.

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/ramakrishnan2503/Language_Translation_using_LSTM.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:

    ```bash
    streamlit run app.py
    ```

4. Open your web browser and navigate to the provided URL.

5. Enter an English sentence in the input box, select the desired translation language, and click the "Translate" button.
   
### Model Details

The translation model utilizes LSTM (Long Short-Term Memory) networks for sequence-to-sequence learning, enabling effective language translation.
- **LSTM Nodes:** 256
- **Embedding Size:** 100
- **Batch Size:** 64
- **Epochs:** 20

## Supported Languages

- English to Tamil
- English to French
- English to Spanish
- Tamil to English
- French to English
- Spanish to English

## File Structure

- `app.py`: Main script for the Streamlit web application.
- `eng_tam_model.py`: Script for loading the trained LSTM model and performing translations for English to Tamil.
- `tam_eng_model.py`: Script for loading the trained LSTM model and performing translations for Tamil to English.
- `eng_fre_model.py`: Script for loading the trained LSTM model and performing translations for English to French.
- `fre_eng_model.py`: Script for loading the trained LSTM model and performing translations for French to English.
- `eng_spa_model.py`: Script for loading the trained LSTM model and performing translations for English to Spanish.
- `spa_eng_model.py`: Script for loading the trained LSTM model and performing translations for Spanish to English.
  
## Acknowledgments

The LSTM model is trained for basic translation purposes and is not fine-tuned on vast datasets.

**Download Model,Encoder,Decoder and Tokenizer**:[Drive](https://drive.google.com/drive/folders/1U31eq0EmvcbfD82i6P46XFcBCa6uuGKq?usp=sharing)

**Note:** The models and tokenizers have been saved for convenient usage.

