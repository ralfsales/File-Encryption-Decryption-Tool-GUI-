# File-Encryption-Decryption-Tool-GUI-
This is a simple Python-based tool that allows users to encrypt and decrypt text files using the Fernet symmetric encryption scheme from the cryptography library. The tool provides an easy-to-use GUI built with tkinter, enabling users to select files for encryption and decryption through file dialogs.

Key Features:

Encryption: Encrypt text files securely using the Fernet encryption scheme.
Decryption: Decrypt previously encrypted files back to their original content.
GUI Interface: A user-friendly graphical interface to select files for encryption and decryption.
Key Management: The program generates and loads a secret encryption key stored in a file (secret.key), ensuring secure operations.
File Handling: The tool works directly with text files and modifies them in place (overwriting with encrypted or decrypted data).
Technologies Used:

Python
tkinter (for GUI)
cryptography (for encryption and decryption)
How it Works:

The program generates and stores a secret key if one does not already exist.
Users can select files for encryption or decryption via a file dialog.
The program uses the Fernet symmetric encryption scheme to secure the file contents.
Feedback is provided via message boxes to inform the user about the success or failure of the operation.
Usage Instructions:

Run the file_encryptor_gui.py script to launch the GUI.
Select Encrypt File to encrypt a file, or Decrypt File to decrypt it.
Ensure that the secret.key file is present for decryption (it is created automatically during the first encryption).
Potential Use Cases:

Secure file storage and transmission.
Protecting sensitive information in text files.
Simple encryption tool for personal or organizational use.
