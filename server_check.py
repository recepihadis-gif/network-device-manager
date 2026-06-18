import requests
import json
from datetime import datetime

servers = ["https://google.com", "https://github.com", "https://anthropic.com"]

results = []
down_count = 0

check_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Check time:", check_time)
print()

for server in servers:
    try:
        response = requests.get(server)
        status = "UP"
        print(server, "is UP -", response.status_code)
    except:
        status = "DOWN"
        print(server, "is DOWN")
        down_count = down_count + 1
    results.append({"server": server, "status": status, "time": check_time})

print()
print("Number of down servers:", down_count)

with open("server_log.json", "w") as file:
    json.dump(results, file, indent=4)

print("Results saved to server_log.json")
