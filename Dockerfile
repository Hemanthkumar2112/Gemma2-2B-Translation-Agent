 
# FROM python:3.10

# RUN apt-get update && apt-get install -y \
#     curl \
#     build-essential

 
# WORKDIR /indic_translate

 

# COPY requirements.txt . 
# RUN pip install --no-cache-dir -r requirements.txt
 
# COPY . .
# EXPOSE 8080

# CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]


# Base image with CUDA support
FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install the correct version of bitsandbytes with CUDA support
RUN pip install bitsandbytes-cuda117

# Install Hugging Face Transformers and other dependencies
RUN pip install transformers torch torchvision --upgrade

# Set the working directory
WORKDIR /app


# Copy the project files into the container
COPY . /app

# Install additional Python dependencies if needed
RUN pip install -r requirements.txt

# Run the Hugging Face model script
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
