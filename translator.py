import streamlit as st
from eng_tam_model import eng_tam
from spa_eng_model import spa_eng
from tam_eng_model import tam_eng
from eng_spa_model import eng_spa
from fre_eng_model import fre_eng
from eng_fre_model import eng_fre

st.title("Translation App")

# Input text box
input_text = st.text_area("Enter text:", "How are you?")

st.markdown("<br>",unsafe_allow_html=True)

col1, col2 = st.columns(2)
from_lang = ["Tamil","English", "French","Spanish"]
to_lang = ["Tamil","English", "French","Spanish"]




with col1:
    st.title("Source language")
    # Source language selection
    source_lang = st.selectbox("Select source language:", from_lang, index=None)
    if source_lang == "Tamil":
        to_lang.remove("Spanish")
        to_lang.remove("French")
        to_lang.remove("Tamil")
    elif source_lang == "French":
        to_lang.remove("Spanish")
        to_lang.remove("French")
        to_lang.remove("Tamil")
    elif source_lang == "Spanish":
        to_lang.remove("Spanish")
        to_lang.remove("French")
        to_lang.remove("Tamil")
    elif source_lang == "English":
        to_lang.remove("English")


with col2:
    st.title("Target Language")
    # Target language selection
    target_lang = st.selectbox("Select target language:", to_lang, index=None)
    

st.markdown("<br><br>",unsafe_allow_html=True)
print(input_text)

button = st.button("Translate")
# Translate button
st.markdown("<br>",unsafe_allow_html=True)
if not input_text and button:
    st.warning("Enter text to translate")

if source_lang and target_lang:
    if button:
        # Perform translation
        if source_lang == "English" and target_lang == "Tamil":
            input_text , output_text = eng_tam(input_text)
            translated_text = output_text
        elif source_lang == "Tamil" and target_lang == "English":
            input_text , output_text = tam_eng(input_text)
            translated_text = output_text
        elif source_lang == "Spanish" and target_lang == "English":
            input_text , output_text = spa_eng(input_text)
            translated_text = output_text
        elif source_lang == "English" and target_lang == "Spanish":
            input_text , output_text = eng_spa(input_text)
            translated_text = output_text
        elif source_lang == "French" and target_lang == "English":
            input_text , output_text = fre_eng(input_text)
            translated_text = output_text
        elif source_lang == "English" and target_lang == "French":
            input_text , output_text = eng_fre(input_text)
            translated_text = output_text
        else:
            translated_text = "dummy"

        # Display translated text
        st.subheader(f"Input Text ({source_lang}):")
        st.write(input_text)
        st.subheader(f"Translated Text ({target_lang}):")
        st.write(translated_text)
else:
    st.warning("Please select a Source and Target Language")