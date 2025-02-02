from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class FileEncryptorDecryptorGUI:
    def __init__(self):
        self.key_file = "encryption_key.key"
        self.key = None

        # GUI setup
        self.root = tk.Tk()
        self.root.title("File Encryptor/Decryptor")
        self.root.geometry("400x200")

        # Buttons and labels
        self.label = tk.Label(self.root, text="Select an action:")
        self.label.pack(pady=10)

        self.encrypt_button = tk.Button(self.root, text="Encrypt File", command=self.encrypt_file)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(self.root, text="Decrypt File", command=self.decrypt_file)
        self.decrypt_button.pack(pady=5)

        self.generate_key_button = tk.Button(self.root, text="Generate New Key", command=self.generate_key)
        self.generate_key_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=10)

        self.root.mainloop()

    def generate_key(self):
        """Generate and save a new encryption key."""
        self.key = Fernet.generate_key()
        with open(self.key_file, "wb") as key_out:
            key_out.write(self.key)
        messagebox.showinfo("Key Generated", f"Encryption key saved to {self.key_file}")

    def load_key(self):
        """Load the encryption key from a file."""
        if not os.path.exists(self.key_file):
            self.generate_key()
        else:
            with open(self.key_file, "rb") as key_in:
                self.key = key_in.read()

    def encrypt_file(self):
        """Encrypt a file using the loaded key."""
        self.load_key()
        file_path = filedialog.askopenfilename(title="Select File to Encrypt")
        if not file_path:
            return

        try:
            with open(file_path, "rb") as file:
                data = file.read()

            fernet = Fernet(self.key)
            encrypted_data = fernet.encrypt(data)

            with open(file_path, "wb") as file:
                file.write(encrypted_data)

            messagebox.showinfo("Success", f"File encrypted successfully: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def decrypt_file(self):
        """Decrypt a file using the loaded key."""
        self.load_key()
        file_path = filedialog.askopenfilename(title="Select File to Decrypt")
        if not file_path:
            return

        try:
            with open(file_path, "rb") as file:
                encrypted_data = file.read()

            fernet = Fernet(self.key)
            decrypted_data = fernet.decrypt(encrypted_data)

            with open(file_path, "wb") as file:
                file.write(decrypted_data)

            messagebox.showinfo("Success", f"File decrypted successfully: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Run the GUI application
if __name__ == "__main__":
    FileEncryptorDecryptorGUI()
