from logging_sol import get_logger

def register_users(name):
    logger = get_logger("app")
    if not name:
        logger.error("no name provided to register")