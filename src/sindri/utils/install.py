#!/usr/bin/env python3
"""
Install Sindri service and other items.
"""

# Standard library imports
import logging
import sys

# Third party imports
import serviceinstaller

# Local imports
import sindri.config.service


def log_setup(verbose=None):
    if verbose is None:
        logging_level = 99
    elif verbose:
        logging_level = "DEBUG"
    else:
        logging_level = "INFO"
    logging.basicConfig(stream=sys.stdout, level=logging_level)


def install_sindri_service(platform=None, mode="client", verbose=None):
    log_setup(verbose)

    serviceinstaller.install_service(
        platform=platform, **sindri.config.service.SERVICE_CONFIG[mode])


if __name__ == "__main__":
    install_sindri_service()
