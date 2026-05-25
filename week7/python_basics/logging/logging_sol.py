"""
1. x
2. v
3. x
4. x
5. v
6. v
7. x
"""

"""
info
error
debug
error
warning
info
"""

"""
1. this should be info not error
2. should log sensitive information
3. this isn's a log you should always log
"""

"""
the current time
the level of the log
name of the file
a message
"""


def exce5():
    import logging

    logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
    logger = logging.getLogger(__name__)
    logger.info("Application started")


def process_payment(user_id, amount):
    import logging

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    logger = logging.getLogger(__name__)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    logger.info(f"Starting payment for user {user_id}")
    if amount <= 0:
        logger.error("Invalid amount")
        return
    if amount > 10000:
        logger.warning("Large transaction")
        logger.info(f"Payment of {amount} completed for user {user_id}")


def exce7():
    import logging

    logger = logging.getLogger("payments")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s |%(name)s |%(message)s")

    file_handler = logging.FileHandler("app.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info("stuff")
    logger.info("some more stuff")
    logger.info("and more")


def read_config(filepath):
    import logging

    logger = logging.getLogger("payments")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s |%(name)s |%(message)s")

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    logger.debug("need to do it here for some reason")
    try:
        with open(filepath) as f:
            data = f.read()
            logger.info("file read ended successfully")
        return data
    except FileNotFoundError:
        logger.error(f"the file {filepath} did not exist")
        return None


def json_logging(level: str, module, message, **extra):
    import logging
    import json
    import datetime

    log_func = getattr(logging, level.lower(), logging.info)
    timestamp = (
        datetime.datetime.now(datetime.timezone.utc)
        .replace(tzinfo=None)
        .isoformat(timespec="seconds")
    )
    log_entry = {
        "timestamp": timestamp,
        "level": level,
        "module": module,
        "message": message,
        **extra,
    }
    log_func(json.dumps(log_entry))


"""
exce 10
1. a very unspecific message write what is done
2. a very unspecific message write what failed
3. a very unspecific message write what about that user
"""

"""
exce 11
1. info
2. error
3. info
4. warning
5. warning
6. error
"""


def exce12():
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    def register_user(email, password, age):
        logger.info(f"started registering email {email}")
        if age < 18:
            logger.error("age too low")
            return
        logger.info("registered email=%s", email)
        logger.info("registering complete")


def get_logger(name):
    import logging

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s |"
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler("app.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def process_request(request_id, user_id):
    logger = get_logger("log")

    logger.debug(f"user_id = {user_id}, request_id = {request_id}")
    if not 100000000 > request_id > 10000000:
        logger.error("invalid request id")
    logger.info(f"processing request {request_id}")

    "things"
    "function calls"
    "calculations"
    "api calls"
    "services activation"
    "discussions and arguments"

    logger.info(f"request {request_id} was processed successfully")
