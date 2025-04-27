# Project-4-Affine-Cipher

Description

A simple GUI-based tool to encrypt and decrypt messages using the Affine Cipher.The Affine Cipher maps each letter x (A→0, B→1, … Z→25) to C = (α·x + β) mod 26, and decrypts via P = α⁻¹·(C − β) mod 26, where gcd(α, 26)=1.

## Features

Encryption and decryption of arbitrary text (letters only; other characters pass through unchanged).

Modular inverse computation for decryption (α⁻¹ mod 26).

Overview button shows cipher formula and valid key ranges.

Setup Test button preloads a sample message and keys for quick demonstration.

## Prerequisites

Python 3.6 or newer

tkinter (bundled with most Python installations)

## Usage

Launch the GUI app:

python affine_cipher.py

Enter your Input Text.

Provide Alpha (α) and Beta (β) (integers 0–25; α must be one of 1,3,5,7,9,11,15,17,19,21,23,25).

Choose Encrypt or Decrypt.

Click Process to see the result in the Result box.

## Buttons

Overview: Displays the Affine cipher formula and valid key ranges.

Setup Test: Loads "HELLO" with α = 5 and β = 8 into the fields for a quick demo.

## Testing

Click Setup Test → Process → Expect ciphertext RCLLA.

Switch to Decrypt → Process → Expect original HELLO.

Try different α/β values and phrases to verify correctness.

## Built With:

Python 3

tkinter

## Contributing

Contributions are welcome! Please fork the repo, make your changes, and submit a pull request.

## License

This project is released under the MIT License. See LICENSE for details.


