# Sagara Crypt (Data Lock Safety and Cryptography)

A simple code that can encrypt, decrypt, and file hashing.<br>

## Features

- Data Encryption and Decryption
- Data File Checker and Hashing 
- Secure File Deletion
- File Compression and Decompression

## Setup  
1. clone this repository:
```bash
git clone https://github.com/sagarabilly/sagara-command.git
```  
2. Add the cloned folder to the system or user environmet path variable. (See the main README.md)  

## Use Case Example

1. Encryption<br>
```sagaracrypt --encrypt input.txt encrypted_output.txt myencryptionkey123```

2. Decryption<br>
```sagaracrypt --decrypt encrypted_output.txt decrypted_output.txt myencryptionkey12i3```

3. Compression<br>
```sagaracrypt --compress input.txt compressed_output.zip```

4. Decompression<br>
```sagaracrypt --decompress compressed_output.zip decompressed_folder```

5. Hashing<br>
```sagaracrypt --hash sha256 input.txt```<br>
```sagaracrypt --hash sha1 input.txt```<br>
```sagaracrypt --hash md5 input.txt```

6. Secure Deletion<br>
```sagaracrypt --secure-delete input.txt```

## Contributions
Please feel free to modify and any contributions are appreciated
