# PdfChatAI

PdfChatAI enables users to add PDFs in a chat-based session and ask any questions related to them in a conversational manner. The application also includes a scoring system where a thumbs up gives a +1 score, helping to improve the model based on user feedback.

## Table of Contents

- [Description](#description)
- [Tech Stack](#tech-stack)
- [First Time Setup](#first-time-setup)
- [Running the App](#running-the-app)

## Description

PdfChatAI is an innovative application designed to revolutionize how users interact with PDF documents. By leveraging advanced language models and seamless integration with various technologies, PdfChatAI provides a conversational interface where users can upload a PDF and ask questions about its content. The application responds accurately and contextually to user queries, making information retrieval from PDFs more intuitive and efficient.

Key Features:
- **Conversational Interaction**: Users can ask questions about the content of a PDF in a natural, conversational manner.
- **Scoring System**: Users can rate responses with a thumbs up (+1 score), which is stored in Redis and used to train the model for improved accuracy.
- **Efficient Storage**: The application uses Pinecone to store embeddings, ensuring quick and efficient retrieval of document information.

## Tech Stack

**Backend:**
- **Language**: Python - The primary programming language used for the application.
- **LLM Model**: OpenAI - Provides the language model used for generating responses.
- **Interaction**: LangChain - Facilitates interaction with the OpenAI model, allowing seamless conversational flow.
- **Text Generation Tracing**: LangFuse - Used for tracing and monitoring text generation processes.
- **Score Storage**: Redis - Stores user feedback scores for each reply, which helps in training the model to improve response accuracy.
- **Embeddings Storage**: Pinecone - Efficiently stores and retrieves embeddings for quick access to document information.

**Frontend:**
- **Framework**: Flask - Provides the web framework for the chat-based UI.
- **Background Processing**: Celery - Integrates with Flask to handle background tasks, such as processing user queries and interacting with the language model.



## First Time Setup

### Using pip [Recommended]

```
# Install dependencies
pip3 install -r requirements.txt

# Initialize the database
flask --app app.web init-db

```

### Using Venv [Optional]

These instructions are included if you wish to use venv to manage your evironment and dependencies instead of Pipenv.

```
# Create the venv virtual environment
python -m venv .venv

# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate

# Install dependencies
pip3 install -r requirements.txt

# Initialize the database
flask --app app.web init-db
```

## Running the app 

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

```
inv dev
```

### To run the worker

```
inv devworker
```

### To run Redis

```
redis-server
```

### To reset the database

```
flask --app app.web init-db
```

## Running the app [Venv]

_These instructions are included if you wish to use venv to manage your evironment and dependencies instead of Pipenv._

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
inv devworker
```

### To run Redis

```
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
flask --app app.web init-db
```
