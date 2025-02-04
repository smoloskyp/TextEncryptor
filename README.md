# Enscryptor

Enscryptor is a simple text encryption and decryption tool that uses bitwise inversion based on a binary mask.

## How It Works
The program converts each character of the input text into its 16-bit binary Unicode representation, then applies a binary mask to invert selected bits. The same mask is used to reverse the process and restore the original text.

## Features
- Encrypts text using a binary mask.
- Decrypts the text back to its original form.
- Simple implementation using Python.


## Requirements
The program only relies on standard Python libraries, so no additional dependencies are required.


## Example
```
Original text: Hello
Encrypted text: 1101101010111001::1101101010110100::110110101011...
Decrypted text: Hello
```

## License
This project is licensed under the MIT License.

