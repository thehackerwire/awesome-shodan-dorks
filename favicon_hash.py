#!/usr/bin/env python3
"""
Favicon MurmurHash3 Calculator for Shodan Reconnaissance
TheHackerWire - https://thehackerwire.com/hacking-tools/shodan-dorks

Usage:
    python favicon_hash.py https://target.com/favicon.ico
    python favicon_hash.py target.com
"""

import sys
import codecs
import argparse
import urllib.parse

try:
    import mmh3
    import requests
except ImportError:
    print("[!] Missing dependencies. Please run: pip install mmh3 requests")
    sys.exit(1)


def calculate_hash(url: str):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    parsed = urllib.parse.urlparse(url)
    if not parsed.path or parsed.path == "/":
        url = urllib.parse.urljoin(url, "/favicon.ico")

    print(f"[*] Fetching favicon from: {url}")
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) TheHackerWire-Recon/1.0"}
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        response.raise_for_status()
    except Exception as e:
        print(f"[-] Error fetching favicon: {e}")
        sys.exit(1)

    # Encode to base64 with linebreaks as Shodan requires
    b64_content = codecs.encode(response.content, "base64")
    fav_hash = mmh3.hash(b64_content)

    print("\n" + "=" * 60)
    print(f"[+] MurmurHash3 Value:  {fav_hash}")
    print(f"[+] Shodan Search Query: http.favicon.hash:{fav_hash}")
    print(f"[+] Shodan Direct URL:   https://www.shodan.io/search?query=http.favicon.hash%3A{fav_hash}")
    print(f"[+] TheHackerWire Tool:  https://thehackerwire.com/hacking-tools/shodan-dorks")
    print("=" * 60 + "\n")
    return fav_hash


if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    parser = argparse.ArgumentParser(description="Calculate Shodan Favicon MurmurHash3")
    parser.add_argument("target", help="URL or domain of target (e.g., https://example.com or example.com)")
    args = parser.parse_args()

    calculate_hash(args.target)
