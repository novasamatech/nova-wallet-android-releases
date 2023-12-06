"""
Usage:
    python fetch_comment_body.py <comment_link> <version>

Example:
    python fetch_comment_body.py "http://example.com/comment" "1.0.0"

This script fetches the body of a comment from a given link and saves it to a file.
The filename is derived from the provided version number, with periods replaced by underscores.
"""

import requests
import argparse
import json


def fetch_comment_body_and_save(comment_link, version):
    # Get the comment body
    response = requests.get(comment_link)
    comment_body = json.loads(response.text)["body"]

    # Replace "Release notes:" and "Release time:" lines
    lines = comment_body.split("\n")
    lines = [
        line
        for line in lines
        if not line.startswith(("Release notes:", "Release time:", "Release severity:"))
    ]
    comment_body = "\n".join(lines)

    # Replace '.' with '_' in the version
    version_underscore = version.replace(".", "_")

    # Write the comment body to a file
    with open(f"updates/changelogs/release/{version_underscore}.md", "w") as file:
        file.write(comment_body)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("comment_link")
    parser.add_argument("version")
    args = parser.parse_args()

    fetch_comment_body_and_save(args.comment_link, args.version)
