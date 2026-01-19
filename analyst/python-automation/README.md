# Python Automation: Access Control List Update

## Project Overview

This project demonstrates a Python-based automation used to maintain an access control allow list. The script reads a file containing IP addresses permitted to access restricted resources and removes any IP addresses that appear on a separate removal list.

This type of automation is commonly used in security operations to reduce manual effort, prevent configuration drift, and enforce access policies consistently.

## Skills Demonstrated

- Python file handling using `open()` and `with` statements
- Reading and writing files with `.read()` and `.write()`
- String manipulation with `.split()` and `.join()`
- Iteration and conditional logic
- Secure handling of access control data

## Files

- `update_allow_list.py` — Python script that performs the allow list update
- `allow_list.txt` — Sample allow list of permitted IP addresses
- `remove_list.txt` — Sample list of IP addresses to be removed

## Notes

This project is educational and demonstrates defensive automation techniques used in cybersecurity and system administration contexts.
