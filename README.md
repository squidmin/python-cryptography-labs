# python-cryptography-labs

This project is a simple backend service developed using FastAPI that provides APIs for encrypting and decrypting data using AES encryption.
It is intended as a straightforward example to demonstrate encryption and decryption in Python with the PyCryptodome library.

## Features

- **Encrypt API**: Allows users to encrypt plaintext and receive ciphertext along with the key and IV needed for decryption.
- **Decrypt API**: Allows users to decrypt ciphertext using the provided key and IV.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python 3.7+ installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/squidmin/python-cryptography-labs.git
   cd python-cryptography-labs
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

### Running the application

1. **Start the server**
   ```bash
   uvicorn main:app --reload
   ```
   This command will start the server on `http://127.0.0.1:8000`. The `--reload` flag enables auto-reload so the server will restart after code changes.

### Using the API

You can interact with the API using the automatically generated Swagger UI:

- **Open your web browser and navigate to** `http://127.0.0.1:8000/docs`
- You can use the interactive API documentation to send requests to encrypt and decrypt data.

#### API Endpoints

- **POST `/encrypt/`**
  - **Description**: Encrypts provided plaintext.
  - **Request Body**: `{"plaintext": "your text here"}`
  - **Response**: `{"iv": "iv", "ciphertext": "ciphertext", "key": "key"}`

- **POST `/decrypt/`**
  - **Description**: Decrypts provided ciphertext.
  - **Request Body**: `{"ciphertext": "your encrypted text here", "iv": "iv from encryption", "key": "key from encryption"}`
  - **Response**: `{"plaintext": "original text"}`
