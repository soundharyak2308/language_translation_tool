import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 Language Translation Tool")
st.caption("Translate text between languages using Google Translator")

# Get all supported Google Translator languages
translator = GoogleTranslator(source="auto", target="en")
supported_languages = translator.get_supported_languages(as_dict=True)

# Sort language names alphabetically
language_names = sorted(supported_languages.keys())

# "Auto Detect" is available only as a source language
source_options = ["Auto Detect"] + language_names
target_options = language_names

text = st.text_area(
    "Enter text to translate",
    placeholder="Type or paste text here...",
    height=160,
    max_chars=5000
)

st.caption(f"{len(text)} / 5000 characters")

col1, col2 = st.columns(2)

with col1:
    source_name = st.selectbox(
        "Translate from",
        source_options,
        index=0
    )

with col2:
    target_name = st.selectbox(
        "Translate to",
        target_options,
        index=target_options.index("hindi") if "hindi" in target_options else 0
    )

if st.button("Translate", type="primary", use_container_width=True):
    if not text.strip():
        st.warning("Please enter text before translating.")

    else:
        # Convert selected language name into its language code
        source_code = "auto" if source_name == "Auto Detect" else supported_languages[source_name]
        target_code = supported_languages[target_name]

        if source_code == target_code:
            st.warning("Please choose two different languages.")

        else:
            try:
                with st.spinner("Translating..."):
                    translated_text = GoogleTranslator(
                        source=source_code,
                        target=target_code
                    ).translate(text)

                st.subheader("Translation")
                st.success(translated_text)

                # st.code provides a built-in copy icon
                st.code(translated_text, language=None)

            except Exception as error:
                st.error("Translation failed.")
                st.exception(error)