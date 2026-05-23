import logging
from pathlib import Path


LOG_DIR = Path("app/logs")

LOG_DIR.mkdir(
    parents=True,
    exist_ok=True
)


log_file = LOG_DIR / "nexus.log"


logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    )
)


logger = logging.getLogger("nexusiq")