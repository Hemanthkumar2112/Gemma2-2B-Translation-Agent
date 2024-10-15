import streamlit as st



trans_analysis_agent_prompt = """Please analyze the Translation Quality Analysis for the given source and target text 
    
    - Source Text (English): {}
    - Target Text (Translated): {}
    Analysis Questions:

    1. Accuracy:
       - Does the translation correctly convey the meaning of the original text? 
       - Are there any parts of the translation that change or lose the original meaning?

    2. Grammar and Syntax:
       - Is the grammar in the target language correct?
       - Does the translated text flow naturally, or does it sound awkward or stilted?

    3. Cultural Relevance:
       - Are there any cultural or contextual nuances from the source text that were not accurately reflected in the translation?
       - Does the translated text make sense in the target language's cultural context?

    4. Terminology and Vocabulary:
       - Are specific terms or technical words translated correctly and consistently?
       - Are there any mistranslations of key words or phrases?

    5. Tone and Style:
       - Does the translation maintain the same tone (formal, informal, technical, etc.) as the original?
       - Has the style of the original text been preserved or altered in the translation?

    Overall Judgment:
       - Does the translation accurately reflect the intent, meaning, and style of the source text?
       - If not, what changes would you suggest to improve the translation?

give the result in a simple english and should be simple and clear"""



def agent_groq(prompt):
    from indic_MT_inference_script import client
    chat_completion = client.chat.completions.create( 
            messages=[
                {
                    "role": "user",
                    "content": prompt,  
                }
            ],
            model="gemma2-9b-it",stream=True
        )

    for chunk in chat_completion:
        yield chunk.choices[0].delta.content 


st.set_page_config(
    page_title="Adaptive Machine Translation",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
 
)

st.header("🌟 Adaptive Machine Translation for Indian Languages with Brand Voice & Glossary Using Gemma2 2B fine tuning LLM 🤖",)


example_sentences = [
"Heavy rain has caused widespread flooding in several parts of the country.",
"The government has announced new measures to boost the country's economy.",
"The health ministry has issued guidelines to prevent the spread of the new virus variant.",
"The election commission has declared the dates for the upcoming general elections.",
"Farmers across the nation are protesting against the recently passed agricultural laws."
]

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

col1, col2,col3  = st.columns(3)

 

placeholder = col3.empty()  
selected_language = col3.radio("Select a language for translation", list(languages.keys()))
 
counter = 0
col3.markdown('##### Analyzing Machine Translation in AI Agents 🤖🧠')
if col3.button('Analysis Translation 📚' , use_container_width=True):  

    with placeholder.container():
        
        if 'translated_text' in st.session_state:
            source_text = st.session_state.get("source_text",None)
            translated_text = st.session_state.get('translated_text',None)
            prompt = trans_analysis_agent_prompt.format(source_text,translated_text)
            col3.write(agent_groq(prompt))
        else:
            col3.warning("Do some translation to start analysis", icon="⚠️")
 


 
def translate_text(lang,text):
    from indic_MT_inference_script import peft_model,generate,logger
    inference_result = generate(lang,text,"",peft_model,to_set_lang=True)
    logger.info("done translation"+inference_result)
    return inference_result
 



#################################################################
 
with col1:
    if st.session_state.get('example_sentence',None):
        text = col1.text_area("English",value=st.session_state['example_sentence'])
    else:
        text = col1.text_area("English")

    if col1.button("Translate"):
        if text:
            with st.spinner("Translating..."):
                translated_result = translate_text(text=text,lang=languages[selected_language]['lang'])
                st.session_state['translated_text'] = translated_result
                st.session_state["source_text"] = text
        else:
            st.warning('please enter any english sentence to translate', icon="⚠️")
for sentence in example_sentences:
    if col1.button(sentence):
        st.session_state['example_sentence'] = sentence 



with col2:
    translated_text = ""
    if 'translated_text' in st.session_state:
        translated_text = st.session_state['translated_text']
        st.text_area("Translate to",value=translated_text)
        col2.download_button(label="Download", data=translated_text,file_name="translated_sentence.txt")
    else:
        st.text_area("Translate to",value=translated_text)
    

    
 
#col2.("### Connect with Me:")

st.write("-----------------------------------------------------------------------------------------------------------------------------------")
st.title("Connect with Me:")
st.markdown("[GitHub](https://github.com/Hemanthkumar2112) | [Hugging Face](https://huggingface.co/Hemanth-thunder) | [LinkedIn](https://www.linkedin.com/in/hemanth-m-a97b19b1/)")
 

 


 
         
        
         


    