import streamlit as st
from googletrans import Translator
from docx import Document
import base64
import io
import streamlit_theme as stt

# Set the theme using a dictionary with the primary color specified
stt.set_theme({'primary': '00CCFF'})

# Rest of your Streamlit application code


# Create a translator object
translator = Translator()

# Mapping of language names to language codes
language_mapping = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Afrikaans": "af",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Basque": "eu",
    "Belarusian": "be",
    "Bengali": "bn",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Cebuano": "ceb",
    "Chichewa": "ny",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Corsican": "co",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "Esperanto": "eo",
    "Estonian": "et",
    "Filipino": "tl",
    "Finnish": "fi",
    "Frisian": "fy",
    "Galician": "gl",
    "Georgian": "ka",
    "Greek": "el",
    "Gujarati": "gu",
    "Haitian Creole": "ht",
    "Hausa": "ha",
    "Hawaiian": "haw",
    "Hebrew": "iw",
    "Hmong": "hmn",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Igbo": "ig",
    "Indonesian": "id",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jw",
    "Kazakh": "kk",
    "Khmer": "km",
    "Kinyarwanda": "rw",
    "Korean": "ko",
    "Kurdish (Kurmanji)": "ku",
    "Kyrgyz": "ky",
    "Lao": "lo",
    "Latin": "la",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Luxembourgish": "lb",
    "Macedonian": "mk",
    "Malagasy": "mg",
    "Malay": "ms",
    "Maltese": "mt",
    "Maori": "mi",
    "Marathi": "mr",
    "Mongolian": "mn",
    "Myanmar (Burmese)": "my",
    "Nepali": "ne",
    "Norwegian": "no",
    "Odia (Oriya)": "or",
    "Pashto": "ps",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Romanian": "ro",
    "Russian": "ru",
    "Samoan": "sm",
    "Scots Gaelic": "gd",
    "Serbian": "sr",
    "Sesotho": "st",
    "Shona": "sn",
    "Sindhi": "sd",
    "Sinhala": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Sundanese": "su",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tajik": "tg",
    "Tatar": "tt",
    "Thai": "th",
    "Turkish": "tr",
    "Turkmen": "tk",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uyghur": "ug",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Xhosa": "xh",
    "Yiddish": "yi",
    "Yoruba": "yo",
    "Zulu": "zu"
}

# Function to translate text
def translate_text(input_text, src_lang, tgt_lang):
    try:
        src_code = language_mapping[src_lang]
        tgt_code = language_mapping[tgt_lang]
        translated_text = translator.translate(input_text, src=src_code, dest=tgt_code).text
        return translated_text
    except Exception as e:
        st.error(f"Translation failed: {str(e)}")

# Function for the translation page
def translation_page():
    st.title("Multi-Language Translation")
    input_text = st.text_area("Enter text to translate:")
    src_lang = st.selectbox("Select source language:", list(language_mapping.keys()))
    tgt_lang = st.selectbox("Select target language:", list(language_mapping.keys()))
    if st.button("Translate"):
        if input_text.strip() != "":
            st.info("Translating...")
            translated_text = translate_text(input_text, src_lang, tgt_lang)
            if translated_text:
                st.write("Translation:")
                st.write(translated_text)
                st.session_state.translated_text = translated_text
                st.session_state.translation_ready = True
        else:
            st.warning("Please enter some text to translate.")

# Function for the download page
def download_page():
    st.title("Download Translated Document")
    if st.button("Download Document"):
        if "translated_text" in st.session_state:
            document = Document()
            document.add_paragraph(st.session_state.translated_text)
            document_stream = io.BytesIO()
            document.save(document_stream)
            document_stream.seek(0)
            b64 = base64.b64encode(document_stream.read()).decode()
            href = f'<a href="data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{b64}" download="translated_document.docx">Click here to download</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.success("Translated document has been downloaded successfully.")
        else:
            st.error("No translated text found. Please translate some text first.")

# Function to display the model description on the home page
def home_page():
    st.title("Welcome to Multi Language Translation APP")
    st.markdown(
        """
        Welcome to our Multi-Language Translator! Our translator model is designed to effortlessly translate 
        text between multiple languages with just a few clicks. Powered by state-of-the-art translation technology, 
        our model ensures accurate and reliable translations for all your communication needs.

        With support for a wide range of languages, including English, Tamil, Hindi, French, Spanish, German, and 
        many more, our translator empowers you to break down language barriers and connect with people from diverse 
        backgrounds across the globe.

        Whether you're a traveler exploring new destinations, a student studying foreign languages, or a professional 
        communicating with international clients, our Multi-Language Translator is your go-to solution for seamless 
        and efficient translation.

        Ready to embark on a journey of linguistic exploration? Click on the "Multi-Language Translator" option 
        in the sidebar and start translating text effortlessly between different languages. Say goodbye to language 
        barriers and hello to global communication!
        """
    )
    st.markdown("---")
    st.write("Ready to translate? Click on the 'Multi-Language Translator' option in the navigation menu.")

# Main function to switch between pages
def main():
    page = st.sidebar.selectbox("Select page:", ["Home", "Multi-Language Translator", "Download"])
    if page == "Home":
        home_page()
    elif page == "Multi-Language Translator":
        translation_page()
    elif page == "Download":
        download_page()

if __name__ == "__main__":
    main()
