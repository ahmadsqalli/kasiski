# 🗝️ Kasiski - Cryptographic Toolkit for Python

A Python library for classical cryptography, frequency analysis, and cryptanalysis. Named after [Friedrich Kasiski](https://en.wikipedia.org/wiki/Friedrich_Kasiski), the father of modern cryptanalysis.
The library contains many of the famous ciphers, and all the cryptoanalysis tools and functions you'd need in your deciphering journey.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

### 🔐 Classical Ciphers
- **Atbash Cipher** - Simple reversal cipher
- **Caesar Cipher** - Shift cipher, with brute-force capability (doubles as ROT13 cipher)
- **Affine Cipher** - Mathematical substitution cipher
- **Vigenère Cipher** - Polyalphabetic substitution
- **Rail Fence Cipher** - Transposition cipher
- **Chaocipher** - Dynamic substitution cipher
- **Gematria** - Numerology-based encoding
- **Nihilist Cipher** - Symmetric encryption ciphe

### 🔍 Cryptanalysis Tools
- **N-gram Frequency Analysis** - Unigram, digram, bigram, trigram
- **N-gram Scan** - `ngram_frequency_scan()` combines the results of multiple N-gram scans and weighs them against each other, used mainly for simple substitution ciphers
- **Text Comparison** - `text_match_rate()` for accuracy measurement
- **Random Text Generation** - For testing and analysis
- **Diversity index** - A score for spicies diversity in a sample (diversity/equitability)
- **Index of coincidence** - Calculate the probability of drawing two identical letters randomly from a text.

## 🚀 Quick Start

### Installation

```bash
pip install .
