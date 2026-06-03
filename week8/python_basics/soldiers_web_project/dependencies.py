from dataclasses import dataclass, field

from soldier_modules import Soldier
from logger_config import create_logger
from utils.io import write

logger = create_logger(__name__, "system.log")


@dataclass(frozen=True)
class DatabaseState:
    soldiers: dict[str, Soldier] = field(default_factory=dict)


db: DatabaseState = DatabaseState()


def get_db() -> DatabaseState:
    return db


def set_db(new_db: DatabaseState) -> None:
    global db
    db = new_db


def prep_data_for_commit(data: DatabaseState):
    return [s.model_dump() for s in data.soldiers.values()]


def commit_db(db_name: str = "soldiers.json"):
    data: DatabaseState = get_db()
    data_for_commit = prep_data_for_commit(data)
    write(db_name, data_for_commit)
    logger.info("db committed")
