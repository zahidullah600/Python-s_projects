
import json


default_config = {
    "app_name": "Student Management System",
    "version": "1.0",
    "settings": {
        "language": "English",
        "notifications": True,
        "max_students": 100
    }
}

try:
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)

    print("Configuration loaded successfully.")

except FileNotFoundError:
    config = default_config

    print("Config file not found. Using default settings.")


print("\nApplication Name:", config["app_name"])
print("Version:", config["version"])
print("Language:", config["settings"]["language"])
print("Notifications:", config["settings"]["notifications"])
print("Maximum Students:", config["settings"]["max_students"])

config["settings"]["language"] = "Pashto"

print("\nLanguage setting updated.")

with open("config.json", "w", encoding="utf-8") as file:
    json.dump(config, file, indent=4)

print("Configuration saved successfully.")
