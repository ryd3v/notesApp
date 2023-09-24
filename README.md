
# NotesVault
![ALT](https://github.com/ryd3v/notesVault/blob/main/Screenshot-1.png)
![ALT](https://github.com/ryd3v/notesVault/blob/main/Screenshot-2.png)

## Overview

NotesVault is a secure notes application that allows you to create, save, and load encrypted notes. The application leverages advanced cryptographic algorithms to ensure the privacy and security of your notes.

## Features

- **Create Notes**: Easily create new notes with a simple and intuitive interface.
- **Save and Load**: Save your notes to disk in an encrypted format and load them back when needed.
- **Markdown Support**: Render your notes in Markdown format for better readability.
- **Strong Encryption**: Utilizes AES-256-GCM for note encryption and bcrypt for password hashing.

## Algorithms Used

### AES-256-GCM

- **What**: Advanced Encryption Standard with a 256-bit key size, used in Galois/Counter Mode (GCM).
- **Why**: Provides both encryption and integrity verification.
- **How**: Encrypts the notes using a key derived from the user's password.

### bcrypt

- **What**: A cryptographic hashing algorithm.
- **Why**: For securely hashing and verifying user passwords.
- **How**: Hashes the user's password and saves it. Verifies the hash against entered passwords.

## Usage

1. **Start the App**: Run the application executable.
2. **Enter Password**: On startup, the application will prompt you to enter a strong password which will be used for encryption.
3. **Create or Load Notes**: Use the interface to create new notes or load existing ones.
4. **Save Notes**: Use the "Save" button to save notes to disk in an encrypted format.

## Dependencies

- PyQt5: For the graphical user interface.
- cryptography: For AES-256-GCM encryption.
- bcrypt: For password hashing.
- Markdown: For rendering Markdown text.

## How to Install

1. Clone the repository or download the source code.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the application.

## Contributing

Contributions are welcome! Please read the contributing guidelines before submitting any changes.

## License

This project is licensed under the MIT License.

