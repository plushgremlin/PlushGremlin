import logging
from logging import StreamHandler, FileHandler

# Create a logger object
logging.basicConfig(level=logging.DEBUG, handlers= [
    StreamHandler(),
    FileHandler('PlushGremlin.log')
])