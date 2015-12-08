from setuptools import setup, find_packages

import sequence_database

setup(
    name = sequence_database.__projectname__,
    version = sequence_database.__release__,
    packages = find_packages(),
    author = sequence_database.__authors__,
    author_email = sequence_database.__authoremails__,
    description = sequence_database.__description__,
    license = "GPLv2",
    keywords = sequence_database.__keywords__,
    entry_points = {
        'console_scripts': [
            'sequence_database = sequence_database.sequence_database:main'
        ],
    },
)
