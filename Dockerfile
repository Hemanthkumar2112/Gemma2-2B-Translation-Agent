
FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime
#FROM nvidia/cuda:12.1.1-runtime-ubuntu22.04
RUN mkdir -p /app/models/gemma-2-2b
# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    python3-pip \
    curl\
    && rm -rf /var/lib/apt/lists/* 
RUN pip install huggingface_hub 
RUN python -c "\
from huggingface_hub import snapshot_download; \
snapshot_dir = snapshot_download(repo_id='Hemanth-thunder/gemma-2-2b-bnb-4bit', revision='main',local_dir='/app/models/gemma-2-2b',); \
print(f'Downloaded snapshot at: {snapshot_dir}');"
# Install the correct version of bitsandbytes with CUDA support
#RUN pip install bitsandbytes-cuda117

# Install Hugging Face Transformers and other dependencies
#RUN pip install -U transformers torch torchvision --upgrade

# Set the working directory

WORKDIR /app


# Copy the project files into the container
COPY . /app

# Install additional Python dependencies if needed
RUN pip install --no-cache-dir -r requirements.txt

# Run the Hugging Face model script
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
EXPOSE 8080