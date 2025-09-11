# Simples Chatbot Flutuante para Website com Flask + DSPy + GPT-4o-mini

Este projeto implementa um **chatbot flutuante** para websites utilizando **Python Flask** e **DSPy**, integrado à **LLM OpenAI GPT-4o-mini**. O chatbot responde perguntas do usuário. (Em breve: consultará documentos do cliente (`.txt` e `.json`) para respostas mais contextuais (RAG)).

---

## Funcionalidades

- Chat flutuante no canto inferior direito da página web
- Respostas geradas por **GPT-4o-mini** via **DSPy**
- Layout moderno e responsivo
- Fácil integração com qualquer site HTML

---

## Estrutura do Projeto

```
📁 flask_dspy_chatbot/
├─ 📝 app.py
├─ 📝 requirements.txt
├─ 🛡 .env
├─ 📁 templates/
│   └─ 📝 index.html
├─ 📁 static/
│   ├─ 🎨 chat.css
│   └─ ⚙️ chat.js
├─ 📁 docs/
│   ├─ 📝 produto_info.txt
│   ├─ 📝 clientes.json
│   ├─ 🖼 chat_screenshot.png
│   └─ 🎞 chat_demo.gif
├─ 🐳 Dockerfile
└─ 🐳 docker-compose.yml
```

---

## Pré-requisitos

- Python 3.10+
- Conta OpenAI com chave API
- Pip ou pipenv para instalar dependências
- Docker e Docker Compose (para rodar em container)

---

## Instalação (local)

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/flask_dspy_chatbot.git
cd flask_dspy_chatbot
```

2. Crie e ative um virtualenv:

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie o arquivo `.env` com a chave OpenAI:

```env
OPENAI_API_KEY=coloque_sua_chave_aqui
```

5. Coloque arquivos `.txt` ou `.json` na pasta `docs/` com informações que o chatbot deve usar (opcional).

---

## Executando o Servidor (local)

```bash
python app.py
```

Abra [http://localhost:5000](http://localhost:5000) no navegador.

---

## Executando com Docker

1. Crie o arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=coloque_sua_chave_aqui
```

2. Construa e suba o container:

```bash
docker-compose up --build
```

3. Acesse [http://localhost:5000](http://localhost:5000)

---

## Estrutura do Chat

- **Chat flutuante** com botão para abrir/fechar
- **Mensagens do usuário** em azul claro, **respostas da LLM** em cinza.

---

## Tecnologias

- Python 3
- Flask
- DSPy
- OpenAI GPT-4o-mini
- HTML, CSS e JS
- Docker / Docker Compose

---

## Licença

MIT

---

## Contato


Abra uma **issue** no GitHub ou me contate pelo perfil do GitHub para dúvidas ou sugestões.

