# Usa imagem oficial Python
FROM python:3.11

# Define diretório de trabalho
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos do projeto
COPY requirements.txt .
COPY . .

# Instala dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta do Flask
EXPOSE 5000

# Comando para rodar o servidor Flask
CMD ["python", "app.py"]
