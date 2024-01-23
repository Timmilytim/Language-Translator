from deep_translator import GoogleTranslator as Gt
import streamlit as st

st.set_page_config(
    page_title="Translation",
    page_icon="📝",
)

st.title("Welcome to my Language Translator")

lang_list = Gt().get_supported_languages()

col1, col2 = st.columns(2)

with col1:
    options = st.selectbox("Translate from:", lang_list,
                           index=27,
                           placeholder="Select a language you want to translate to")
    st.write(f"Your selected translation is : **{options.upper()}**")


with col2:
    option = st.selectbox("Translate to:", lang_list,
                          key="",
                          index=None,
                          placeholder="Select a language you want to translate to")
    if not option:
        pass
    else:
        st.write(f"Your selected translation is : **{option.upper()}**")


title = st.text_input('Sentence you wished translated', '')

if not option or not options:
    st.warning("Please make a selection for your preferred translation")
else:
    try:
        translated = Gt(source=options, target=option).translate(title)
        st.markdown(f"Your translated text is:")
        st.success(translated)
    except ConnectionError:
        st.warning("Please check your internet connection and try again")


# st.markdown(f"User text is **:{title}**")
# st.write(f"English {lang_list.index('english')}")
