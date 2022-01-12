import inspect
import logging
import os

import __root__


def custom_logger(log_level=logging.DEBUG):

    reports = os.path.join(__root__.path(), "Reports")
    if not os.path.exists(reports):
        os.mkdir(reports)
    # Gets the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    reports_path = os.path.join(__root__.path(), "Reports/Logs.log")
    file_handler = logging.FileHandler(reports_path, mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    # logger.addHandler(fileHandler)

    return logger
