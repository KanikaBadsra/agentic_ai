from pathlib import Path


REPORTS_DIR = Path("app/reports")

REPORTS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def save_report(filename: str, content: str):

    file_path = REPORTS_DIR / filename

    with open(file_path, "w", encoding="utf-8") as file:

        file.write(content)

    return str(file_path)