# Use the official Python image as the base image
FROM python:3.10

RUN apt-get update && apt-get install -y \
    curl \
    build-essential

# # Install Poetry
# RUN curl -sSL https://install.python-poetry.org | python3 -
# ENV PATH="/root/.local/bin:$PATH"
WORKDIR /indic_translate

#COPY pyproject.toml poetry.lock* /indic_translate/

#RUN poetry install --no-root

COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt
 
COPY . .
EXPOSE 8080

CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
