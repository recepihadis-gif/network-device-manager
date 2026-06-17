import json


def load_devices():
    try:
        with open("devices.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
            {"name": "firewall", "ip": "172.16.0.1", "status": "up"},
            {"name": "switch", "ip": "10.75.10.50", "status": "down"},
            {"name": "access point", "ip": "10.75.10.60", "status": "up"},
        ]


def save_devices(devices):
    with open("devices.json", "w") as file:
        json.dump(devices, file, indent=4)


def show_all_devices():
    for device in devices:
        print(device["name"], "-", device["ip"], "-", device["status"])


def show_down_devices():
    for device in devices:
        if device["status"] == "down":
            print(device["name"], "-", device["ip"])


def add_device():
    name = input("Enter device name: ").strip()
    ip = input("Enter device ip: ").strip()
    status = input("Status (up/down): ").strip().lower()
    new_device = {"name": name, "ip": ip, "status": status}
    devices.append(new_device)
    save_devices(devices)
    print("Device added and saved!")


def search_devices():
    search_name = input("Enter device name: ").strip()
    found = False
    for device in devices:
        if device["name"].lower() == search_name.lower():
            print(device["name"], "-", device["ip"], "-", device["status"])
            found = True
    if not found:
        print("Device not found")


def count_down_devices():
    count = 0
    for device in devices:
        if device["status"] == "down":
            count = count + 1
    print("Number of down devices:", count)


devices = load_devices()

while True:
    print()
    print("Network Device Manager")
    print("1. Show all devices")
    print("2. Show down devices")
    print("3. Add device")
    print("4. Search device")
    print("5. Count down devices")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_all_devices()
    elif choice == "2":
        show_down_devices()
    elif choice == "3":
        add_device()
    elif choice == "4":
        search_devices()
    elif choice == "5":
        count_down_devices()
    elif choice == "6":
        print("Goodbye")
        break
    else:
        print("Wrong choice")
