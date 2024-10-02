import streamlit as st
from indic_MT_inference_script import peft_model,adapter_names,generate
st.title("_Indic Machine translation with Gemma2 2B_  :sunglasses:",)

# Dictionary of languages with descriptions and their respective language codes
languages = {
    "Tamil 🇮🇳": {"code": "ta","lang":"tamil" } ,
    "Hindi 🇮🇳": {"code": "hi","lang": "hindi"},
    "Kannada 🇮🇳": {"code": "kn","lang":"kannada"},
    "Malayalam 🇮🇳": {"code": "ml", "lang": "malayalam"},
    "Telugu 🇮🇳": {"code": "te","lang": "telugu" },
    "Bengali 🇮🇳": {"code": "bn",  "lang":"bengali"},
    "Marathi 🇮🇳": {"code": "mr","lang": "marathi"},
    "Gujarati 🇮🇳": {"code": "gu", "lang":"gujarati"},
    "Odia 🇮🇳": {"code": "or", "lang":"odia"}
}

col1, col2,col3 = st.columns(3)
 
selected_language = col3.radio("Select a language for translation", list(languages.keys()))

### testing # lang,english_text,response_text,merged_model
#text = "Heavy rain has caused widespread flooding in several parts of the country."


def translate_text(lang,text):
    inference_result = generate(lang,text,"",peft_model,to_set_lang=True)
    print(f"inference_result for {lang} : {inference_result}")
    return inference_result
 
with col1:
    text = col1.text_area("English")
    if col1.button("Translate"):
        if text:
            with st.spinner("Translating..."):
                print(selected_language)
                print(languages[selected_language]['code'],languages[selected_language]['lang'])
                translated_result = translate_text(text=text,lang=languages[selected_language]['lang'])
                st.session_state['translated_text'] = translated_result
        else:
            st.warning('please enter any english sentence to translate', icon="⚠️")
 

 
with col2:
    translated_text = ""
    if 'translated_text' in st.session_state:
        translated_text = st.session_state['translated_text']
        st.text_area("Translate to",value=translated_text)
        col2.download_button(label="Download", data=translated_text,file_name="translated_sentence.txt")
    else:
        st.text_area("Translate to",value=translated_text)
    
 


    

 
         
        
         


    