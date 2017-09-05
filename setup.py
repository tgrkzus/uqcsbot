from setuptools import setup
from setuptools.command.install import install
import os
import readline

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
        name='uqcsbot',
        version='1.0',
        description='Bot for uqcsbot',
        author='Various',
        packages=['uqcsbot'],
        install_requires=required,
        )

