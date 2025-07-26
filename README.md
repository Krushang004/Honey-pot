# Honey-pot
A lightweight Python-based HTTP Honeypot designed for educational and research purposes. It mimics a vulnerable web server and logs all incoming HTTP requests — useful for detecting unauthorized access attempts, bots, or scanning activity on unused ports.
# 🕵️‍♂️ HoneyPot: Simple Python Web Honeypot

A lightweight, customizable HTTP honeypot built using Python's built-in `http.server` module. It simulates a vulnerable server and logs all access attempts — great for learning cybersecurity, testing detection tools, or analyzing potential intrusions.

---

## 📌 Features

- Logs **all HTTP GET requests** with IP and path
- Simulates a real web server (but serves fake responses)
- **No external libraries required** — runs with default Python
- Fully runnable on Windows/Linux/macOS
- Ideal for LAN demos or ethical hacker training labs

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/honeypot.git
cd honeypot
