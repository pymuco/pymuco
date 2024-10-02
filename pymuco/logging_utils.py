# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         logging_utils.py
# Purpose:      Pymuco classes
#
# Authors:      German Margon
#
# Copyright:    Copyright © 2022-2023 German Margon. All rights reserved.
# License:      BSD 3-Clause License, see LICENSE
# ------------------------------------------------------------------------------
import logging


def setup_logger(name: str) -> logging.Logger:
    """
    Sets up and returns a logger for a given name.

    Parameters:
    -----------
    name: str
        The name to be used for the logger (usually the module's __name__).

    Returns:
    --------
    logging.Logger: A logger for handling log messages.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
