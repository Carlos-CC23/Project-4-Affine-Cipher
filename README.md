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
