# File Encryption — Python

This is a project I developed to explore how encryption algorithms work, particularly the mathematics behind them.

This version operates directly on bytes, allowing it to work with different file formats. It incorporates XOR operations, modular arithmetic, ciphertext chaining, byte mixing and randomly generated keys.


## A Note on Security

**Please do not use this programme to encrypt important or confidential files.**

Although the algorithm is reversible, that does not necessarily make it secure. I developed it primarily to understand encryption, and I cannot attest to its resistance against cryptographic attacks.

There may be mathematical weaknesses or errors that I have yet to discern. An incorrect decryption key could also produce corrupted data without any warning.

If you want to experiment with the programme, use disposable files and retain backups of anything important.

This project is for educational purposes and should not be relied upon for actual data protection.

## Requirements

- Python 3
- PyAutoGUI (for the interface)
- No external cryptography libraries

## Status

Under development.
