# LockdownX Ransomware

## Overview
This repository contains a simple ransomware script written in Python. The script encrypts all files in the current directory and requires a password to decrypt them.

### Disclaimer
This project is intended for educational purposes only. Do not use it to harm or compromise any systems without explicit permission. Misuse of this code can lead to legal consequences.

## How It Works

### Encryption Script (`LockdownX.py`)

The encryption script does the following:
1. Lists all files in the current directory, excluding the encryption script itself, the decryption script, and the key file.
2. Generates a unique encryption key using `cryptography.fernet.Fernet`.
3. Encrypts each file and writes the encrypted content back to the original file.
4. Saves the encryption key to a file named `thekey.key`.

### Decryption Script (`decrypt.py`)

The decryption script does the following:
1. Lists all files in the current directory, excluding the encryption script, the decryption script, and the key file.
2. Reads the encryption key from `thekey.key`.
3. Prompts the user for a password. If the correct password (`pasiya123`) is entered, it decrypts each file and writes the decrypted content back to the original file.

## Usage

Install the cryptography library using `pip install cryptography` in Windows before running.

1. **Encrypt Files**:
    ```sh
    python3 LockdownX.py
    ```

2. **Decrypt Files**:
    ```sh
    python3 decrypt.py
    ```

    Enter the password: `pasiya123`.

## Note
Please remember to use this code responsibly. It is designed for learning and demonstration purposes only.

## Credit
This project was inspired by a [NetworkChuck YouTube video](https://shorturl.at/bVPcn).

