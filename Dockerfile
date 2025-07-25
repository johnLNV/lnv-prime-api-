# Usa uma imagem oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos da sua API
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define o comando para rodar a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]

