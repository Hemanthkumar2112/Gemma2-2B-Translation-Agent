from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
 
from dotenv import load_dotenv
import os
from groq import Groq

import logging
logging.basicConfig(filename="inference.log",format='%(asctime)s %(message)s',filemode='w')

# Creating an object
logger = logging.getLogger()
load_dotenv()

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
base_model ="/app/models/gemma-2-2b" #"Hemanth-thunder/gemma-2-2b-bnb-4bit"
HUGGING_FACE_TOKEN = os.getenv('HUGGING_FACE_TOKEN') ####replace_this_to_huggingface_token
client = Groq(api_key=os.environ.get("AGENT_GROQ"))

#bnb_config = BitsAndBytesConfig(load_in_4bit=True,bnb_4bit_quant_type="nf4",bnb_4bit_compute_dtype=torch.bfloat16,bnb_4bit_use_double_quant=True)
logger.info("Loading Base Model")
model = AutoModelForCausalLM.from_pretrained(base_model,low_cpu_mem_usage=True).to("cuda")#, ,token=HUGGING_FACE_TOKEN ,quantization_config=bnb_config
logger.info("Loading Tokenizer")
tokenizer = AutoTokenizer.from_pretrained(base_model, use_fast=True) #,token=HUGGING_FACE_TOKEN

# PEFT models paths
peft_models_path = {
    'hindi': "Hemanth-thunder/model_gemma2b_mt-hi_1k_steps",
    'tamil': "Hemanth-thunder/model_gemma2b_mt-ta_2k_steps",
    'kannada': "Hemanth-thunder/model_gemma2b_mt-kh_10k_steps",
    'malayalam': "Hemanth-thunder/model_gemma2b_mt-ml_10k_steps",
    'telugu': "Hemanth-thunder/model_gemma2b_mt-te_10k_steps",
    'bengali': "Hemanth-thunder/model_gemma2b_mt-bn_10k_steps",
    'marathi': "Hemanth-thunder/model_gemma2b_mt-mr_10k_steps",
    'gujarati': "Hemanth-thunder/model_gemma2b_mt-gujarati_gu_10k_steps",
    'odia': "Hemanth-thunder/model_gemma2b_mt-odia_or_10k_steps"
}

# Adapter names
adapter_names = list(peft_models_path.keys())

pipeline_type = "text-generation"

peft_model = PeftModel.from_pretrained(model, peft_models_path['tamil'], adapter_name="tamil")

for lang, path in peft_models_path.items():
    if lang != "tamil":
        try:
            _ = peft_model.load_adapter(path, adapter_name=lang)
            print(f"load {lang}")
        except Exception as e:
            print(f"Error loading adapter for {lang}: {e}")
# Set the model to evaluation mode
peft_model.eval()



alpaca_prompt = """
### Instruction:
Your are an AI translator to translate the following English input sentence to {} sentence.

### Input:
{}

### Response:
{}"""


## function for generatining text 
def generate(lang, english_text, response_text, merged_model, to_set_lang):
    # Prepare the prompt using the language and texts
    prompt = alpaca_prompt.format(lang.capitalize(), english_text, response_text)

    # Set the adapter for the merged model if specified
    if to_set_lang:
        merged_model.set_adapter(lang)
        print(f"adaptor switched to {lang}")

    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

    # Generate output using the model
    try:
        outputs = merged_model.generate(**inputs, max_new_tokens=256,do_sample=True,top_p=0.95,temperature=0.2,repetition_penalty=1.2,eos_token_id=tokenizer.eos_token_id,)
        # Decode and return the response
        response = tokenizer.decode(outputs[0])
        return response.split("### Response:")[-1].strip()
    
    except Exception as e:
        print(f"Error during generation: {e}")
        return None
    




