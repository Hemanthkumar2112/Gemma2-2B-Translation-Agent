import streamlit as st
import time
st.title("_Indic Machine translation with Gemma2 2B_  :sunglasses:",)

# Dictionary of languages with descriptions and their respective language codes
languages = {
    "Tamil 🇮🇳": {"code": "ta" },
    "Hindi 🇮🇳": {"code": "hi" },
    "Kannada 🇮🇳": {"code": "kn",  },
    "Malayalam 🇮🇳": {"code": "ml",  },
    "Telugu 🇮🇳": {"code": "te",  },
    "Bengali 🇮🇳": {"code": "bn",  },
    "Marathi 🇮🇳": {"code": "mr", },
    "Gujarati 🇮🇳": {"code": "gu", },
    "Odia 🇮🇳": {"code": "or", }
}

col1, col2,col3 = st.columns(3)
 
selected_language = col3.radio("Select a language for translation", list(languages.keys()))

 
with col1:
    text = col1.text_area("English")
    if col1.button("Translate"):
        if text:
            with st.spinner("Translating..."):
                time.sleep(5)
                st.session_state['translated_text'] = text
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
    
 


    

 
         
        
         


    