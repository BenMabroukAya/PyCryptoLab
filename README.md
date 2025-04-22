Here's the corrected and properly formatted version of your README.md (I fixed the header syntax and spacing issues):

```markdown
# PyCryptoLab  
*A Python Toolkit for Classical Cryptography & Cryptanalysis*  

## Overview  
PyCryptoLab implements classical ciphers and cryptanalysis tools in Python. It supports encryption/decryption, frequency analysis, and key detection for educational and research purposes.

## Features  
- **Ciphers**: Caesar, Affine, Vigenère, Transposition, ADFGVX, Porta, RSA  
- **Analysis**: Frequency counting, index of coincidence, key length estimation  
- **Text Processing**: Automatic cleaning and block formatting  

## Quick Start  
```bash
git clone https://github.com/BenMabroukAya/PyCryptoLab.git
cd PyCryptoLab
python cryptovault.py
```

### Basic Usage  
```python
# Caesar Cipher
from cryptovault import cesar
ciphertext = cesar("HELLO", 3, ischiffre=True)  # Encrypt
plaintext = cesar(ciphertext, 3, ischiffre=False)  # Decrypt
```

## Supported Algorithms  
| Cipher         | Encryption | Decryption | Analysis |  
|----------------|------------|------------|----------|  
| Caesar         | ✓          | ✓          | ✓        |  
| Vigenère       | ✓          | ✓          | ✓        |  
| RSA            | ✓          | ✓          | ✗        |  


## License
[MIT](LICENSE) © 2025 [Aya Ben Mabrouk]

