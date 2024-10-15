# Indic Translation App

This project tackles the challenge of **on-device machine translation** for multiple **Indic languages** in a **resource-constrained environment**. By leveraging the **Gemma2 2B LLM** and employing **adapter switching**, the model can efficiently translate between various Indian languages without the need for separate models for each one, reducing **computational demands**. 

The project specifically addresses the difficulties of training machine translation from **English** to nine Indic languages—**Tamil**, **Hindi**, **Kannada**, **Malayalam**, **Telugu**, **Bengali**, **Marathi**, **Gujarati**, and **Odia**—by utilizing adapter switching to enhance performance and manage the complexity of **multilingual translation**.

## Demo

[Watch the demo video]

https://github.com/user-attachments/assets/c410d65c-fa78-47ac-95cc-ca12d8c8de08

This repository contains the code for an Indic language translation app using Docker.

## Prerequisites

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
## Customizing the App
- Feel free to modify the source code and rebuild the Docker image to customize the translation functionality.

License
This project is licensed under the MIT License - see the LICENSE file for details.


