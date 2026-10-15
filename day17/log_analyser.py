from collections import Counter
from pathlib import Path

LOG_FILE = Path("sample.log")


def analyse_log():
    if not LOG_FILE.exists():
        print("Log file not found.")
        return

    error_counts = Counter()

    with LOG_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            if "ERROR" in line:
                error_type = line.split("ERROR", 1)[1].strip()
                error_counts[error_type] += 1

    print("Error summary:")

    if not error_counts:
        print("No errors found.")
        return

    for error, count in error_counts.items():
        print(f"{error}: {count}")


if __name__ == "__main__":
    analyse_log()