'''
Problem Statement:
Implement the Affine Cipher encryption and decryption functions:
  Encryption: C = (α * x + β) mod 26
  Decryption: P = α⁻¹ * (C - β) mod 26
where x = 0..25 maps to letters A..Z, key=(α, β), and gcd(α,26)=1.

Informal Proof:
Because gcd(α,26)=1, α has a multiplicative inverse mod 26, denoted α⁻¹.
Thus decryption reverses encryption:
  P = α⁻¹ * (C - β) mod 26
    = α⁻¹ * ((α x + β) - β) mod 26
    = α⁻¹ * α x mod 26
    = x.

Algorithm (pseudocode):
  function modinv(a, m):
    return the multiplicative inverse of a under modulus m using extended Euclid

  function encrypt(msg, a, b):
    for each character in msg:
      if letter is A–Z or a–z:
        map to 0–25, apply (a * x + b) mod 26, map back to letter
      else:
        keep unchanged
    return ciphertext

  function decrypt(cipher, a, b):
    a_inv = modinv(a, 26)
    for each character in cipher:
      if letter is A–Z or a–z:
        map to 0–25, apply a_inv * (y - b) mod 26, map back to letter
      else:
        keep unchanged
    return plaintext
'''

import tkinter as tk
from tkinter import messagebox

# Extended Euclidean Algorithm to find modular inverse
def modinv(a, m):
    def egcd(x, y):
        if y == 0:
            return (x, 1, 0)
        g, px, py = egcd(y, x % y)
        return (g, py, px - (x // y) * py)

    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse for alpha={a} under mod {m}")
    return x % m

# Encryption function
def affine_encrypt(msg, a, b):
    cipher = ''
    for ch in msg:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            x = ord(ch) - base
            y = (a * x + b) % 26
            cipher += chr(y + base)
        else:
            cipher += ch
    return cipher

# Decryption function
def affine_decrypt(cipher, a, b):
    plain = ''
    a_inv = modinv(a, 26)
    for ch in cipher:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            y = ord(ch) - base
            x = (a_inv * (y - b)) % 26
            plain += chr(x + base)
        else:
            plain += ch
    return plain

# GUI Application
class AffineCipherApp:
    def __init__(self, master):
        self.master = master
        master.title("Affine Cipher Simulator")

        # Input text
        tk.Label(master, text="Input Text:").grid(row=0, column=0, sticky='e')
        self.input_text = tk.Text(master, height=4, width=40)
        self.input_text.grid(row=0, column=1, columnspan=3)

        # Alpha entry
        tk.Label(master, text="Alpha (α):").grid(row=1, column=0, sticky='e')
        self.alpha_entry = tk.Entry(master, width=5)
        self.alpha_entry.grid(row=1, column=1, sticky='w')

        # Beta entry
        tk.Label(master, text="Beta (β):").grid(row=1, column=2, sticky='e')
        self.beta_entry = tk.Entry(master, width=5)
        self.beta_entry.grid(row=1, column=3, sticky='w')

        # Mode selection
        self.mode = tk.StringVar(value='encrypt')
        tk.Radiobutton(master, text="Encrypt", variable=self.mode, value='encrypt').grid(row=2, column=1)
        tk.Radiobutton(master, text="Decrypt", variable=self.mode, value='decrypt').grid(row=2, column=2)

        # Buttons: Overview, Process, Test Setup
        tk.Button(master, text="Overview", command=self.show_overview).grid(row=3, column=0)
        tk.Button(master, text="Process", command=self.process).grid(row=3, column=1, columnspan=2)
        tk.Button(master, text="Setup Test", command=self.setup_test).grid(row=3, column=3)

        # Output label
        tk.Label(master, text="Result:").grid(row=4, column=0, sticky='ne')
        self.output_text = tk.Text(master, height=4, width=40, state='disabled')
        self.output_text.grid(row=4, column=1, columnspan=3)

    def show_overview(self):
        overview = (
            "Affine Cipher Simulator\n"
            "- Encryption: C = (αx + β) mod 26\n"
            "- Decryption: P = α⁻¹(C - β) mod 26\n"
            "Keys: α ∈ {1,3,5,7,9,11,15,17,19,21,23,25}, β ∈ [0,25]\n"
            "Enter text, choose α and β, then Encrypt or Decrypt."
        )
        messagebox.showinfo("Project Overview", overview)

    def setup_test(self):
        # Prefill fields for a simple test: "HELLO" with α=5, β=8
        self.input_text.delete("1.0", tk.END)
        self.input_text.insert(tk.END, "HELLO")
        self.alpha_entry.delete(0, tk.END)
        self.alpha_entry.insert(0, "5")
        self.beta_entry.delete(0, tk.END)
        self.beta_entry.insert(0, "8")
        self.mode.set('encrypt')
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state='disabled')

    def process(self):
        msg = self.input_text.get("1.0", tk.END).strip()
        try:
            a = int(self.alpha_entry.get())
            b = int(self.beta_entry.get())
            if not (0 <= a < 26 and 0 <= b < 26):
                raise ValueError("Alpha and Beta must be between 0 and 25.")
            if self.mode.get() == 'encrypt':
                result = affine_encrypt(msg, a, b)
            else:
                result = affine_decrypt(msg, a, b)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state='disabled')

if __name__ == '__main__':
    root = tk.Tk()
    app = AffineCipherApp(root)
    root.mainloop()
