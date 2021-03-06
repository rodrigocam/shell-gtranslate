from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='shell-gtranslate',

    version='0.1',

    description='A simple tool to translate any text from command line',

    url='https://github.com/rodrigocam/shell-gtranslate',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['googletrans'],

    entry_points={
        'console_scripts': [
            'tl=src:main.test',
        ],
    },
)