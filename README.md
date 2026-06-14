# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:54:56 2026

@author: shaik
"""

# Web Security Header Checker

A Python-based command-line tool that scans websites for missing HTTP security headers and generates a detailed security audit report.

---

## What It Does

- Accepts single or multiple URLs as input
- Checks for 6 critical HTTP security headers
- Shows risk level (High / Medium / Low) for each missing header
- Gives an overall security grade (A to F) for each site
- Saves a timestamped `.txt` report automatically

---

## Security Headers Checked

| Header | Risk if Missing |
|---|---|
| X-Frame-Options | High - Clickjacking attacks |
| Content-Security-Policy | High - XSS attacks |
| X-Content-Type-Options | Medium - MIME sniffing attacks |
| Strict-Transport-Security | High - Forces HTTPS |
| Referrer-Policy | Low - Data leakage via referrer |
| Permissions-Policy | Low - Unrestricted browser features |

---

## Grading System

| Grade | Meaning |
|---|---|
| A | All headers present |
| B | No high risk missing, max 2 missing |
| C | 1 high risk header missing |
| D | 2 high risk headers missing |
| F | 3 or more high risk headers missing |

---

## Sample Output
=======================================================

Web Security Header Checker v2.0

Made by: Shahid Shaikh

Purpose: Educational / Security Auditing
URL    : https://youtube.com

Scanned: 2026-06-14 17:50:40
✅ FOUND   → X-Frame-Options

✅ FOUND   → Content-Security-Policy

✅ FOUND   → X-Content-Type-Options

✅ FOUND   → Strict-Transport-Security

❌ MISSING → Referrer-Policy

⚠️  Risk: Low - Referrer info may leak to other sites

✅ FOUND   → Permissions-Policy
Headers Found  : 5/6

Headers Missing: 1/6

Security Grade : B - Good

---

## How To Run

**1. Install the required library:**
pip install requests

**2. Run the script:**
python scanner.py

**3. Enter the number of URLs and paste them one by one**

**4. Check the generated `report_YYYYMMDD_HHMMSS.txt` file in the same folder**

---

## Tech Used

- Python 3
- `requests` library
- `datetime` module

---

## Disclaimer

This tool is for **educational purposes only.**
Only scan websites you own or have explicit permission to test.
The author is not responsible for any misuse.

---

## Author

**Shahid Shaikh**  
BCA Student | Ethical Hacking Trainee  

