import logging

from app.utils.init_db import init_db
from app.utils.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    logger.info("Creando data incial")
    init()
    logger.info("Data incial creada")


if __name__ == "__main__":
    main()
