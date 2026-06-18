# Hadis — My Learning Progress

**Goal:** Become a Cloud / Network Automation Engineer (Python + Network + Cloud + AI tools).

**Coaching style I like:** simple English, explain the idea first, give full code, then test, then check I understood. One step at a time. Don't overwhelm.

---

## What I have already learned

**Setup**
- Python 3.13 installed (I run it with `py`)
- Project folder on E: -> `E:\automation-lab`
- Virtual environment (venv) -> activate with `venv\Scripts\activate`
- VS Code is my editor
- Git + GitHub account: `recepihadis-gif`

**Python basics**
- Lists `[]` and dictionaries `{}`
- Loops (`for`), conditions (`if` / `elif` / `else`)
- Functions (`def`) and calling them with `()`
- `input()`, `.append()`, `.strip()`, `.lower()`
- JSON files: `json.load`, `json.dump` (load -> change -> save)
- `try` / `except` (so the program does not crash)
- Reading errors and fixing my own bugs

**Project 1 - Device Manager** (`device_manager.py`)
- Menu tool: show all / show down / add / search / count down devices
- Saves devices in `devices.json`

**Project 2 - Server Health Checker** (`server_check.py`)
- Checks if servers are UP or DOWN (live, using APIs)
- Shows a clean timestamp, counts down servers
- Saves a log to `server_log.json`

**APIs** (`api_test.py`)
- An API = my program asks another computer for data, gets JSON back
- `import requests`, `requests.get("url")`, `.json()`, `data["key"]`
- Status codes: 200 = OK / UP
- Checked my public IP, country, city, ISP

---

## Where I am now
Phase 2 of my plan: Files, JSON, and APIs. I can call APIs and save results to files.

## What is next
1. Practice APIs more (different APIs, safe error handling)
2. Status codes and headers
3. Then: network automation with Netmiko
4. Then: cloud (Azure) and AI tools

---

## How to continue from any computer / new chat
1. Open this GitHub repo
2. Start a new chat, paste this file, and say:
   "I am continuing my automation engineer program. Here is my progress. What is next?"
