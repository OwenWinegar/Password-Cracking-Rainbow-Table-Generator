# Password Cracking & Rainbow Table Generator

## Overview
This project is a Python-based password‑cracking tool that generates custom rainbow tables and attempts to recover passwords using MD5 hashing.  
The program builds wordlists from social‑engineered data, expands them into multiple password candidates, filters them based on each person’s password rules, and compares each attempt against a target MD5 hash.

This project demonstrates:
- MD5 hashing
- Rainbow table generation
- Combinatoric password generation using `itertools`
- Social‑engineering‑guided wordlist creation
- Unicode filtering (removing symbols)
- File I/O for large wordlist and log generation
- Defensive security analysis (salting, slow hashing, rate limiting)

## Features

### Wordlist Processing
- Reads text files containing social‑engineered information  
- Splits on colons, commas, and whitespace  
- Normalizes or preserves case depending on user profile  
- Builds a unique sorted set of usable words  

### Rainbow Table Generation
Generates thousands of password combinations by:
- Combining 1–6 words
- Enforcing character length rules
- Enforcing alphanumeric-only rules
- Ensuring uppercase/lowercase/digit requirements (for Dr. Pearson)

All attempts are logged to:
- `bobs_rainbow_table.txt`
- `dr_pearsons_rainbow_table.txt`

### Password Requirements

#### Bob
- 5–10 characters  
- Alphanumeric only  
- No symbols  
- No uppercase requirement  

#### Dr. Pearson
- 12–18 characters  
- Alphanumeric only  
- Must include:
  - At least one digit  
  - At least one uppercase letter  
  - At least one lowercase letter  

### Hash Matching
Uses Python’s `hashlib.md5()` to compare each generated password against:
- `bob_hash`
- `dr_pearson_hash`

Stops early if a match is found.

## File Structure
Password-Cracker/

-main.py

-bob.txt # Social‑engineered source words for Bob

-dr_pearson.txt # Social‑engineered source words for Dr. Pearson

-bobs_rainbow_table.txt # Generated attempts for Bob

-dr_pearsons_rainbow_table.txt # Generated attempts for Dr. Pearson

-README.md

## How It Works

### 1. Process Wordlist
```python
process_file("bob.txt", True)
```
### 2. Run the cracker
Bob:
```python
hash_finderB(bob_hash)
```
Dr. Pearson:
```python
hash_finderD(dr_pearson_hash)
```
