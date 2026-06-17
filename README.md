# Network Device Manager

A simple command-line tool built in Python to manage and monitor network devices such as firewalls, switches, and access points. Device data is stored in a JSON file, so it is saved between runs.

This is my first Python project, built while learning network and cloud automation.

## Features

- **Show all devices** — list every device with its IP and status
- **Show down devices** — quickly see which devices are down
- **Add device** — add a new device (name, IP, status)
- **Search device** — find a device by name (not case-sensitive)
- **Count down devices** — show how many devices are down
- **Save & load** — data is stored in `devices.json` automatically

## How to run

    python device_manager.py

Then choose an option from the menu by typing a number.

## What I learned

- Lists and dictionaries
- Loops and conditions (`for`, `if` / `elif`)
- Functions (`def`)
- Reading user input
- Reading and writing JSON files
- Cleaning input with `.strip()` and `.lower()`

## Built with

- Python 3
- JSON for data storage
