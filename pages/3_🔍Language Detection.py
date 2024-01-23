import detectlanguage
import streamlit as st
from deep_translator import GoogleTranslator as Gt

st.set_page_config(
    page_title="Language Detection",
    page_icon="🔍",
)

detectlanguage.configuration.api_key = "726c429b2e00ac5d3cab1ee10a9b9afd"

st.header("Language Detection:")

lang_list = Gt().get_supported_languages()

user_input = st.text_input("Enter your preferred sentence in your preferred language.", placeholder='Enter text...')

# The GoogleTranslator and detectlanguage are two separate libraries, so the languages they support varies;
# I have to go through both to see if what our user typed is in both libraries because as detectlanguage is used to only
# detect languages, GoogleTranslate is used for translation.
if not user_input:
    st.warning("Enter your preferred sentence in your preferred language")
else:
    lang = detectlanguage.simple_detect(user_input)
    lang_detect = detectlanguage.languages()

# Separating the 'code' and 'name' values of the lang_detect dictionary
    code = [i['code'] for i in lang_detect]
    name = [i['name'].lower() for i in lang_detect]

    # To check the index location of the language code returned by the detect language library
    code_index = code.index(lang)

    st.write(f"You are typing in: **{name[code_index].upper()}**")

    options = st.selectbox("Enter the language you want a translation to.", lang_list,
                           index=27,
                           placeholder="Select a language you want to translate to")
    st.write(f"Your selected translation is: **{options.upper()}**")

    if not user_input:
        st.warning("Enter your preferred sentence in your preferred language.")
    else:
        translated = Gt(source=lang, target=options).translate(user_input)
        st.success(translated)

