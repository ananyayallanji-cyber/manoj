import os
import subprocess

user_input = input("Enter command: ")
os.system("echo " + user_input)  # Command Injection vulnerability
password = "admin12345_hardcoded_password"  # Hardcoded Secret vulnerability
eval(user_input)  # Arbitrary Code Execution vulnerability
