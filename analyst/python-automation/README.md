# Python Automation: Access Control List Update

## Project Overview

This project demonstrates a Python-based automation used to maintain an access control allow list. The script reads a file containing IP addresses permitted to access restricted resources and removes any IP addresses that appear on a separate removal list.

Automations like this are commonly used in security operations to reduce manual effort, prevent configuration drift, and enforce access policies consistently.

---

## How It Works

- Reads a list of allowed IP addresses from a text file
- Converts the data into a Python list for processing
- Filters out IP addresses that appear on a defined removal list
- Writes the updated allow list back to the file

The logic is designed to be clear, safe, and easy to extend.

---

## Security Relevance

Access control lists must be updated regularly as users change roles, leave organizations, or no longer require access to sensitive systems. Automating this process helps security teams:

- Reduce manual configuration errors
- Enforce least-privilege access
- Maintain accurate access records
- Respond quickly to access revocation requirements

This project represents a small but realistic example of defensive automation used in security operations and system administration.

---

## Skills Demonstrated

- Python file handling using `open()` and `with` statements
- Reading and writing files with `.read()` and `.write()`
- String manipulation with `.split()` and `.join()`
- Safe list filtering using list comprehensions
- Defensive automation and access control logic

---

## Files

- `update_allow_list.py` — Python script that updates the allow list
- `allow_list.txt` — Sample allow list of permitted IP addresses
- `remove_list.txt` — Sample list of IP addresses to be removed

---

## Context

This project was developed as part of an educational cybersecurity program and was expanded to reflect professional coding practices and real-world security automation workflows.
