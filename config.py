import yaml
import logging
from pathlib import Path

CONFIG_PATH = 'config.yaml'


VECTOR_STORE_PARAMS = yaml.safe_load(open(CONFIG_PATH))['vector_store']
LOG_PARAMS = yaml.safe_load(open(CONFIG_PATH))["logger"]
GITHUB_PARAMS = yaml.safe_load(open(CONFIG_PATH))["github"]

# create auxiliary variables
loggerName = Path(__file__).stem

# create logging formatter
logFormatter = logging.Formatter(
    fmt=LOG_PARAMS["logfmt"], datefmt=LOG_PARAMS["datefmt"]
)
# create logger
loglvl = getattr(logging, LOG_PARAMS["level"])
logger = logging.getLogger(loggerName)
logger.setLevel(loglvl)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(loglvl)
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)


class Bcolors:
    HEADER = "\033[95m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
