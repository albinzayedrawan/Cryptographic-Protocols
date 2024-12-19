# Cryptographic Protocols

## Overview

This workspace contains two Python scripts: signature.py and TLS.py

Each script demonstrates cryptographic operations using the cryptography library.

## Files

**1. Simulating the TLS Handshake:**
signature.py

This script demonstrates how to implement a digital signature using RSA. It includes the following steps:

1. Generate an RSA key pair.
2. Sign a message using the private key.
3. Verify the signature using the public key.

**2. Digital Signatures:**

TLS.py

This script simulates a simplified TLS handshake. It includes the following steps:

1. The client generates a random value.
2. The server generates a random value and an RSA key pair.
3. The client encrypts a pre-master secret using the server's public key.
4. The server decrypts the pre-master secret using its private key.
5. The script verifies that the shared secret is established successfully.

## Usage

To run the script, execute the following command:

```sh
python signature.py
python TLS.py
```

## Requirements

- Python 3.x
- cryptography library

## Installation

To install the required cryptography library, run:

```sh
pip install cryptography
```
