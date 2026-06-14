import requests
from datetime import datetime

def print_banner(report_lines):
    
    def log(text=""):
        print(text)
        report_lines.append(text)
    
    log("="*55)
    log("   Web Security Header Checker v2.0")
    log("   Made by: Shahid Shaikh")
    log("   Purpose: Educational / Security Auditing")
    log("="*55)
    log("⚠️  DISCLAIMER: This tool is for educational")
    log("   purposes only. Only scan websites you own")
    log("   or have permission to test.")
    log("="*55 + "\n")


def check_headers(url, report_lines):
    
    security_headers = {
        "X-Frame-Options":           ("High",   "Site can be embedded in iframes (Clickjacking risk)"),
        "Content-Security-Policy":   ("High",   "No XSS protection policy defined"),
        "X-Content-Type-Options":    ("Medium", "Browser may misinterpret file types"),
        "Strict-Transport-Security": ("High",   "HTTPS not enforced by server"),
        "Referrer-Policy":           ("Low",    "Referrer info may leak to other sites"),
        "Permissions-Policy":        ("Low",    "Browser features not restricted")
    }
    
    def log(text=""):
        print(text)
        report_lines.append(text)
    
    log("="*55)
    log("URL    : " + url)
    log("Scanned: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    log("="*55)
    
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        
        found = 0
        missing = 0
        high_risk = 0
        
        for header, (severity, reason) in security_headers.items():
            if header in headers:
                log("✅ FOUND   → " + header)
                found += 1
            else:
                log("❌ MISSING → " + header)
                log("   ⚠️  Risk: " + severity + " - " + reason)
                log()
                missing += 1
                if severity == "High":
                    high_risk += 1
        
        # Calculate grade
        if missing == 0:
            grade = "A - Excellent"
        elif high_risk == 0 and missing <= 2:
            grade = "B - Good"
        elif high_risk == 1:
            grade = "C - Fair"
        elif high_risk == 2:
            grade = "D - Poor"
        else:
            grade = "F - Critical"
        
        log("="*55)
        log(f"Headers Found  : {found}/6")
        log(f"Headers Missing: {missing}/6")
        log(f"Security Grade : {grade}")
        log("="*55 + "\n")
        
    except Exception as e:
        log("❌ ERROR: Could not reach " + url)
        log("   Reason: " + str(e))
        log("="*55 + "\n")


def main():
    
    report_lines = []
    
    print_banner(report_lines)
    
    count = int(input("How many URLs do you want to scan? "))
    urls = []
    for i in range(count):
        url = input(f"Enter URL {i+1}: ")
        urls.append(url)
    
    report_lines.append("\nScanning " + str(len(urls)) + " URL(s)...\n")
    print("\nScanning " + str(len(urls)) + " URL(s)...\n")
    
    for url in urls:
        check_headers(url, report_lines)
    
    # Save full report
    filename = "report_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
    
    print("📄 Report saved as:", filename)


# --- Run ---
main()