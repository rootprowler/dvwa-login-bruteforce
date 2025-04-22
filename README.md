# 🛡️ DVWA Login Brute-Force Attack | Hydra Automation

A beginner-level offensive security project that simulates a real-world credential brute-force attack against the login page of DVWA (Damn Vulnerable Web Application), hosted on Metasploitable 2. The project also includes a client-style penetration test report and an automated Python script for executing Hydra attacks.

---

## 📌 Project Objectives

- Understand how login brute-force attacks work
- Learn how to use **Hydra** for web form attacks
- Automate brute-force with **Python scripting**
- Create a **client-style penetration test report**
- Showcase practical skills in a GitHub portfolio

---

## 🛠️ Tools & Technologies Used

| Tool         | Purpose                             |
|--------------|--------------------------------------|
| **Hydra**     | Brute-force attack against login    |
| **Python**    | Script automation                   |
| **Kali Linux**| Attack machine                      |
| **Metasploitable 2** | Target environment         |
| **DVWA**      | Vulnerable web app (login portal)   |
| **Nmap**      | Network scanning & host discovery   |
| **Markdown & PDF** | Report creation                |

---

## 🧪 Attack Methodology

1. Scanned the network using `nmap -sn 192.168.56.0/24` to find the Metasploitable IP.
2. Identified DVWA running at `http://192.168.254.130/dvwa/login.php`.
3. Used Hydra with custom wordlists to launch a POST-based brute-force.
4. Valid credentials (`admin:password`) were successfully discovered.
5. Automated the process with a Python script.
6. Documented everything in a client-style report.

---

## 🐍 Hydra Automation Script

```bash
python3 hydra_bruteforce.py
