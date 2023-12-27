# Factorization Script

This script reads a file containing natural numbers greater than 1, factorizes each number into a product of two smaller numbers, and prints the factorization.

## Usage

python factors.py <file>
<file>: A file containing natural numbers to factor, with one number per line.
Requirements
Python 3.x
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/your-repository.git
cd your-repository
Run the script:

python factors.py <file>
Example
Suppose you have a file named numbers.txt with the following content:

15
28
7
Run the script:

python factors.py numbers.txt
Output:

15=5*3
28=14*2
7=7*1
Notes
The script handles invalid input gracefully and reports errors with line numbers.
Ensure the input file contains valid natural numbers greater than 1.
Author
Your Calebkech

## RSA Key Generation Script

This script generates RSA key pairs based on the factorization script's principles. It reads a file containing an RSA modulus (product of two prime numbers) and outputs the corresponding prime factors.

RSA Key Generation Usage
python rsa.py <file>
<file>: A file containing the RSA modulus (product of two prime numbers).
RSA Key Generation Requirements
Python 3.x
RSA Key Generation Installation
Clone the repository:

git clone https://github.com/calebkech/
cd your-repository
Run the script:
python rsa.py <file>
RSA Key Generation Example
Suppose you have a file named rsa_modulus.txt with the RSA modulus:
143
Run the script:
python rsa.py rsa_modulus.txt
Output:
143=11*13
RSA Key Generation Notes
The script handles invalid input gracefully and reports errors.
Ensure the input file contains a valid RSA modulus.
RSA Key Generation Author
<code>calebkech<code>
