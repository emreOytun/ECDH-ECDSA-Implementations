# Elliptic Curves and Applications

This repository contains materials and code related to the study of elliptic curves and their applications, with a focus on cryptography. The project explores the mathematical foundations of elliptic curves, their properties, key algorithms, and their use in modern cryptographic protocols such as Elliptic Curve Cryptography (ECC), Elliptic Curve Digital Signature Algorithm (ECDSA), and Elliptic Curve Diffie-Hellman (ECDH).

## Project Contents

### 1. Presentation
- **`Elliptic Curves.pptx`**: A PowerPoint presentation summarizing the key points of the project, including mathematical definitions, algorithms, and cryptographic applications of elliptic curves.

### 2. Final Report
- **`Final Report Emre Oytun.pdf`**: A detailed report on elliptic curves and their applications. This includes theoretical foundations, pseudocode for key algorithms, complexity analysis, and practical examples.

### 3. Code Implementations
- **`ecdh.py`**: A Python implementation of the Elliptic Curve Diffie-Hellman (ECDH) algorithm for secure key exchange. This script demonstrates how two parties can securely compute a shared secret over an insecure channel using elliptic curves.
- **`ecdsa.py`**: A Python implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) for signing and verifying messages. This script illustrates how to create and validate digital signatures using elliptic curves.

### 4. Documentation
- **`README.md`**: This file provides an overview of the project, its purpose, and descriptions of the included files.

## Key Topics Covered
- **Mathematical Background**: Definitions, properties, and operations on elliptic curves.
- **Algorithms**: Implementation of point addition, point doubling, and the double-and-add algorithm.
- **Applications in Cryptography**:
  - **ECC**: Secure communication with smaller key sizes compared to RSA.
  - **ECDH**: Secure key exchange protocol.
  - **ECDSA**: Digital signature generation and verification.

## How to Use the Code
To get started with the project:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/elliptic-curves-project.git

2. Navigate to the project directory:
   ```bash
   cd elliptic-curves-project

3. Make sure you have Python installed. You need to install these dependencies:
   ```bash
   pip install random
   pip install hashlib

3. Run the Python scripts to see the implementations:
   ```bash
   python ecdh.py
   python ecdsa.py
