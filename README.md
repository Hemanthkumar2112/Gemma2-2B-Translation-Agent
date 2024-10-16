# Indic Translation App

This project tackles the challenge of **on-demand machine translation** for multiple **Indic languages** in a **resource-constrained environment**. By leveraging the **Gemma2 2B LLM** and employing **adapter switching** (LoRA switch), the model can efficiently translate between various Indian languages without the need for separate models for each one, reducing **computational demands**. 

The project specifically addresses the difficulties of training machine translation from **English** to nine Indic languages—**Tamil**, **Hindi**, **Kannada**, **Malayalam**, **Telugu**, **Bengali**, **Marathi**, **Gujarati**, and **Odia**—by utilizing adapter switching to enhance performance and manage the complexity of **multilingual translation**.

Analyzing the translation of source segments into target segments using an agentic approach. The system leverages the Groq API to ensure that the source segment is accurately translated into its corresponding target segment. The process involves validating the translation quality by comparing both segments and ensuring semantic and contextual alignment.

Key features include:
- Machine translation done with the fine tuned Gemma2-2B model
- Agentic methods Analysis for quality assurance and check for correctness in the translation process.
- Use of Groq API to analysis

## huggingface model
```bash
base_model: Hemanth-thunder/gemma-2-2b-bnb-4bit
peft_adapters: Hemanth-thunder/indic_mt_fine_tuned_peft_adapter
```
## Demo

https://github.com/user-attachments/assets/c410d65c-fa78-47ac-95cc-ca12d8c8de08

In the root directory, create a new file called .env.

```bash
Create a .env file:
```
Generate your  hugging face token and Groq Api(Agent) from the relevant service and
Store the API key in the .env file:

```bash
HUGGING_FACE_TOKEN=your_api_key_here
AGENT_GROQ=your_api_key_here
```

## Prerequisites

This repository holds the code for an Indic language translation application, packaged with Docker for easy deployment.

- Make sure you have [Docker](https://www.docker.com/products/docker-desktop) installed on your machine.

## Steps to Build and Run the App

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Hemanthkumar2112/Indic-machine-translation-gemma2-2B
   cd Indic-machine-translation-gemma2-2B
    ```
2. **Build the Docker image**:
   ```bash
   docker build -t indic_translation .
   ```
3. **Run the Docker container**:
   ```bash
   docker run --gpus all -p 8080:8080 indic_translation 
   ```
4. **Access the application**:
   ```bash
   http://localhost:8080
   ```
4. **logging**
   ```bash
   docker logs -f container_id --tail 1000 
   ```
License
This project is licensed under the MIT License - see the LICENSE file for details.


