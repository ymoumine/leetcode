import re

def update_readme(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    checked = len(re.findall(r"\[x\]", content, flags=re.IGNORECASE))
    unchecked = len(re.findall(r"\[ \]", content, flags=re.IGNORECASE))

    # Replace the placeholder with the actual count
    updated = re.sub(
        r"Total completed tasks: \*\*.*?\*\*",
        f"Total completed tasks: **{checked}/{unchecked}**",
        content
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated)

if __name__ == "__main__":
    update_readme("README.md")
