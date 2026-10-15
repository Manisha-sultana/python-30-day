
import json
from pathlib import Path

CONFIG_FILE = Path("config.json")

def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return {
        "username": "Manisha",
        "theme": "light",
        "language": "Hindi"
    }

def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)

def main():
    config = load_config()

    print("Current settings:")
    print(config)

    config["theme"] = "dark"

    save_config(config)

    print("Settings saved successfully!")

if __name__ == "__main__":
    main()
