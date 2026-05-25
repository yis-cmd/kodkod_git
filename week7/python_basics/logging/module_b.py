from logging_sol import get_logger

def give_gift(amount):
    logger = get_logger("moneyyyyyyy")
    if amount < 0:
        logger.error("cant gift less than 0$")