# update_allow_list.py
# This script updates an access control allow list by
# removing IP addresses that appear on a removal list.

# File containing allowed IP addresses
import_file = "allow_list.txt"

# Open the allow list file and read its contents
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert the string of IP addresses into a list
ip_addresses = ip_addresses.split()

# List of IP addresses that should be removed
remove_list = [
    "192.168.1.10",
    "10.0.0.5",
    "172.16.0.3"
]

# Remove any IP addresses that appear in the removal list
ip_addresses = [
    ip for ip in ip_addresses
    if ip not in remove_list
]

# Convert the updated list back into a newline-separated string
updated_ips = "\n".join(ip_addresses)

# Write the revised allow list back to the file
with open(import_file, "w") as file:
    file.write(updated_ips)
