import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s")
logging.debug("Debugging information")
logging.info("Program started")
logging.warning("Check this situation")
logging.error("Something went wrong")