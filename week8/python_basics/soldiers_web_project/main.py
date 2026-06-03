from fastapi import FastAPI

from utils.io import read
from logger_config import create_logger
from soldier_modules import Soldier

logger = create_logger(__name__, "system.log")


from dependencies import DatabaseState, set_db
import api


def load_db(db_name: str):
    data = read(db_name)
    soldiers = {s.get("id"): Soldier.model_validate(s) for s in data}
    logger.info("db loaded")
    return DatabaseState(soldiers)




db_name = "soldiers.json"
set_db(load_db(db_name))
logger.info("db set")

app = FastAPI()
logger.info("starting server")
app.include_router(api.router)


if __name__ == "__main__":
    pass
