<div align="center">

# 📡 Awesome Shodan Dorks & Reconnaissance Cheat Sheet

**A curated, production-grade collection of 500+ advanced Shodan search queries, filters, and reconnaissance techniques for security researchers, penetration testers, bug bounty hunters, and defenders.**

[![Live Interactive Engine](https://img.shields.io/badge/Live_Engine-TheHackerWire-00ff41?style=for-the-badge&logo=target)](https://thehackerwire.com/hacking-tools/shodan-dorks)
[![Total Queries](https://img.shields.io/badge/Queries-500+-ff334b?style=for-the-badge)](#curated-dork-categories)
[![License: MIT](https://img.shields.io/badge/License-MIT-00e5ff?style=for-the-badge)](LICENSE)
[![Awesome](https://awesome.re/badge.svg)](https://github.com/thehackerwire)

[⚡ Launch Interactive Shodan Engine](https://thehackerwire.com/hacking-tools/shodan-dorks) • [Google Dorking Engine](https://thehackerwire.com/hacking-tools/google-dorking-engine) • [All Hacking Tools](https://thehackerwire.com/hacking-tools/)

</div>

---

> [!TIP]
> **Prefer an interactive interface?**  
> Use the web-based **[TheHackerWire Shodan Dorks Engine](https://thehackerwire.com/hacking-tools/shodan-dorks)** to dynamically inject target hostnames (`hostname:"target.com"`), filter by SSL cert SANs (`ssl:"target.com"`), toggle threat severities, build queries with a visual sandbox, and export ready-to-run `.sh` recon dossiers with one click.

---

## 📑 Table of Contents

- [Core Shodan Search Filters](#-core-shodan-search-filters)
- [Curated Dork Categories](#-curated-dork-categories)
  - [1. Exposed Databases & Big Data](#1-exposed-databases--big-data)
  - [2. Webcams & CCTV Surveillance](#2-webcams--cctv-surveillance)
  - [3. Industrial Control Systems (ICS / SCADA)](#3-industrial-control-systems-ics--scada)
  - [4. DevOps, CI/CD & Cloud Infrastructure](#4-devops-cicd--cloud-infrastructure)
  - [5. Admin Consoles & Remote Access](#5-admin-consoles--remote-access)
  - [6. Default Credentials & Setup Portals](#6-default-credentials--setup-portals)
  - [7. High-Impact CVEs & Vulnerabilities](#7-high-impact-cves--vulnerabilities)
  - [8. Corporate Attack Surface & SSL Recon](#8-corporate-attack-surface--ssl-recon)
- [Favicon MurmurHash3 Reconnaissance](#-favicon-murmurhash3-reconnaissance)
- [Shodan CLI Cheat Sheet](#-shodan-cli-cheat-sheet)
- [Target Scoping Best Practices](#-target-scoping-best-practices)
- [Legal & Ethical Disclaimer](#-legal--ethical-disclaimer)

---

## 🔍 Core Shodan Search Filters

| Filter Operator | Syntax Example | Description |
| :--- | :--- | :--- |
| `hostname:` | `hostname:"target.com"` | Matches hosts resolving to target domain or subdomains |
| `ssl:` | `ssl:"target.com"` | Matches certificates containing domain in CN or SAN |
| `ssl.cert.subject.cn:` | `ssl.cert.subject.cn:"*.target.com"` | Matches specific Common Name in SSL/TLS certs |
| `org:` | `org:"Target Corporation"` | Matches organization assigned to IP block (ASN/WHOIS) |
| `asn:` | `asn:AS15169` | Restricts search to an Autonomous System Number |
| `port:` | `port:27017,9200,6379` | Filters by single or multiple TCP/UDP open ports |
| `product:` | `product:"Apache Tomcat"` | Filters by recognized software or service banner |
| `http.title:` | `http.title:"Dashboard"` | Searches HTML `<title>` tags of web services |
| `http.favicon.hash:` | `http.favicon.hash:116323821` | Matches web services presenting exact favicon hash |
| `country:` | `country:US` | Two-letter ISO country code |
| `city:` | `city:"New York"` | Target city location |
| `vuln:` | `vuln:CVE-2021-44228` | Verified CVE vulnerabilities indexed on host |

---

## 🗂️ Curated Dork Categories

### 1. Exposed Databases & Big Data
Unauthenticated NoSQL clusters, data lakes, search indices, and database web interfaces:

```sh
# Unauthenticated MongoDB instances
"MongoDB Server Information" port:27017 -authentication

# Exposed Elasticsearch clusters without Shield/X-Pack auth
port:9200 "cluster_name" "tagline" "You Know, for Search" -auth

# Redis servers without NOAUTH required
port:6379 "redis_version" -NOAUTH

# CouchDB welcome page with administrative APIs
port:5984 "couchdb" "welcome"

# Open Kibana dashboards
port:5601 "kibana" "status" "green"

# RabbitMQ Management console exposed
port:15672 "RabbitMQ Management" -login

# MinIO Object Storage Console
port:9000 "MinIO" "Console" -login

# Apache Solr Admin Panel
port:8983 "Apache Solr" "Solr Admin"

# Exposed Memcached statistics
port:11211 "STAT pid" "uptime"

# Unprotected Hadoop YARN ResourceManagers
port:8088 "Hadoop YARN ResourceManager"
```

### 2. Webcams & CCTV Surveillance
Open RTSP video streams, IP cameras, and network video recorders:

```sh
# Hikvision IP Cameras & DVRs
product:"Hikvision" port:80,8000

# Open RTSP Streams without authentication
port:554 "RTSP/1.0 200 OK"

# Axis network cameras with MJPEG live video
product:"Axis" "live/mjpg"

# Live video MJPEG streams
http.html:"/mjpg/video.mjpg" port:80,8080

# Blue Iris Video Surveillance web portal
http.title:"Blue Iris" port:81

# Dahua video surveillance controllers
product:"Dahua" port:37777,80

# Mobotix webcam live interface
product:"Mobotix" http.title:"MOBOTIX"
```

### 3. Industrial Control Systems (ICS / SCADA)
Critical infrastructure, programmable logic controllers (PLCs), and building automation:

```sh
# Modbus protocol on port 502 (Schneider, WAGO, Modicon)
port:502 "Unit ID"

# BACnet Building Automation and Control networks
port:47808 "BACnet"

# Siemens S7 PLC industrial automation
port:102 "PLC" "Siemens"

# DNP3 electrical substation telemetry protocol
port:20000 "DNP3"

# Omron FINS industrial controllers
port:9600 "FINS" "Omron"

# Niagara Fox building management protocol
port:1911,4911 "fox" "Niagara"

# Rockwell Automation EtherNet/IP PLCs
product:"Rockwell Automation" port:44818

# ProConOS industrial execution systems
port:20547 "ProConOS"

# Veeder-Root TLS fuel tank monitoring consoles
port:10001 "Veeder-Root" "TLS-350"
```

### 4. DevOps, CI/CD & Cloud Infrastructure
Exposed build pipelines, container daemon sockets, and monitoring tools:

```sh
# Docker Remote API daemon without TLS client verification
port:2375 "Docker Containers" -auth

# Exposed Kubernetes etcd cluster state
port:2379 "etcd_server_version"

# Unauthenticated Jenkins automation controllers
http.title:"Dashboard [Jenkins]" -login port:8080

# SonarQube code quality dashboards
http.title:"SonarQube" port:9000

# Grafana monitoring dashboards with anonymous view enabled
http.title:"Grafana - Home" port:3000

# Exposed Prometheus metrics scraping endpoints
http.title:"Prometheus Time Series" port:9090

# Apache Airflow DAG management consoles
http.title:"Airflow" -login port:8080

# HashiCorp Consul service catalog API
port:8500 "Consul" "services"
```

### 5. Admin Consoles & Remote Access
Management interfaces, graphical remote desktops, and terminal gateways:

```sh
# Exposed Windows Remote Desktop (RDP)
port:3389 "Remote Desktop"

# VNC graphical consoles without authentication
port:5900 "RFB 003.008" -authentication

# phpMyAdmin database administration consoles
http.title:"phpMyAdmin" port:80,443,8080

# pfSense firewall WebGUI logins
http.title:"pfSense - Login" port:443,80

# VMware ESXi hypervisor web interface
http.title:"VMware ESXi" port:443

# IPMI remote server management controllers
port:623 "IPMI"

# Telnet servers with unencrypted terminal prompts
port:23 "login:" OR "Password:"
```

### 6. Default Credentials & Setup Portals
Unfinished installation wizards and factory default login portals:

```sh
# SonicWall default credentials prompt
product:"SonicWall" "default password"

# Fortinet FortiGate setup wizard
http.title:"FortiGate" "Setup Wizard"

# MikroTik RouterOS WebFig interface
http.title:"RouterOS router configuration page"

# Ubiquiti UniFi Controller setup wizard
http.title:"UniFi Setup Wizard" port:8443

# WordPress uncompleted installation screen
http.title:"WordPress &rsaquo; Installation"
```

### 7. High-Impact CVEs & Vulnerabilities
Services explicitly flagged or signature-matched to critical vulnerabilities:

```sh
# Log4Shell (Apache Log4j RCE)
vuln:CVE-2021-44228

# Spring4Shell (Spring Framework RCE)
vuln:CVE-2022-22965

# Atlassian Confluence OGNL RCE
vuln:CVE-2022-26134

# OpenSSL Heartbleed leak
vuln:CVE-2014-0160

# Microsoft Exchange ProxyLogon RCE
vuln:CVE-2021-26855

# Apache HTTP Server path traversal & RCE
vuln:CVE-2021-41773
```

### 8. Corporate Attack Surface & SSL Recon
Techniques to map an organization's perimeter IPs, cloud origins, and staging environments:

```sh
# SSL Subject Common Name wildcard match
ssl.cert.subject.cn:"*.TARGET.COM"

# SSL Subject Alternative Names (SAN)
ssl:"TARGET.COM" port:443 -http.status:404

# Hostname banner match
hostname:"TARGET.COM"

# Corporate Autonomous System Number (ASN)
asn:ASXXXXX

# Organization WHOIS match
org:"TARGET CORPORATION"
```

---

## 🎨 Favicon MurmurHash3 Reconnaissance

Favicon hashing allows finding origin IP addresses hidden behind Cloudflare, Akamai, or reverse proxies by searching for the website's unique favicon hash.

### Python Calculator (`favicon_hash.py`)

Run the included [favicon_hash.py](favicon_hash.py) script:

```bash
python favicon_hash.py https://target.com/favicon.ico
```

**Output:**
```
[*] Fetching favicon from: https://target.com/favicon.ico
[+] MurmurHash3 Value:  -123456789
[+] Shodan Search Query: http.favicon.hash:-123456789
```

---

## 💻 Shodan CLI Cheat Sheet

If you use the official Shodan CLI client (`pip install shodan`), here are quick terminal commands:

```bash
# Initialize API key
shodan init YOUR_API_KEY

# Count matching devices for a query
shodan count hostname:"target.com" port:443

# Search and print IP, port, and organization
shodan search --fields ip_str,port,org 'ssl:"target.com" -http.status:404'

# Download first 1,000 results into a compressed JSON file
shodan download target_recon 'hostname:"target.com"'

# Parse downloaded data into readable format
shodan parse --fields ip_str,port,hostnames target_recon.json.gz

# Scan a target IP range directly
shodan scan submit 192.168.1.0/24
```

---

## 🎯 Target Scoping Best Practices

When targeting a specific company for authorized bug bounty or penetration testing:

1. **Host-Level Scoping**: Combine `hostname:"target.com"` with specific high-risk ports:
   ```sh
   hostname:"target.com" port:9200,6379,27017
   ```
2. **Certificate Scoping**: Locate unlisted cloud origin servers that present the company's SSL cert:
   ```sh
   ssl:"target.com" -http.title:"Cloudflare"
   ```
3. **Interactive Recon**: Test combinations live with the [Shodan Dorks Engine](https://thehackerwire.com/hacking-tools/shodan-dorks).

---

## ⚖️ Legal & Ethical Disclaimer

This repository is provided strictly for **educational, authorized security auditing, and defensive vulnerability research purposes**. Searching Shodan queries public data indexed by third-party internet scanners. However, attempting unauthorized access, executing exploits, or interacting with discovered systems without explicit written permission from the asset owner is illegal under the Computer Fraud and Abuse Act (CFAA) and international cybersecurity laws.

---

<div align="center">

**Maintained by [TheHackerWire](https://thehackerwire.com)**  
*Cybersecurity Intelligence, Exploits & Online Tool Suite*

[Shodan Dorks Engine](https://thehackerwire.com/hacking-tools/shodan-dorks) • [Google Dorking Engine](https://thehackerwire.com/hacking-tools/google-dorking-engine) • [Security News](https://thehackerwire.com/category/security-news/)

</div>
