"""
This script updates a JSON file with a new payload or updates an existing one based on the version.

Usage:
    python version_updater.py <version> <time> <severity>

Example:
    python version_updater.py 6.7.1 2023-07-26T15:00:00Z Major
"""

import argparse
import json

RELEASE_FILE_PATH = "updates/v1/entrypoint_release.json"


def update_json(version, time, severity):
    # Load the existing data
    with open(RELEASE_FILE_PATH, "r") as f:
        data = json.load(f)

    # Create the new payload
    payload = {"version": version, "severity": severity, "time": time}

    # Check if the version already exists in the data
    for item in data:
        if item["version"] == version:
            item["severity"] = severity
            item["time"] = time
            break
    else:
        # Add the new payload if the version was not found
        data.append(payload)

    # Save the updated data
    with open(RELEASE_FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)
        f.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("version")
    parser.add_argument("time")
    parser.add_argument("severity")
    args = parser.parse_args()

    update_json(args.version, args.time, args.severity)
