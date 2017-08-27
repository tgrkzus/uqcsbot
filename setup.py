from setuptools import setup
import os

with open('requirements.txt') as f:
    required = f.read().splitlines()

# Install requirements backwards?
required.reverse()

setup(
        name='uqcsbot',
        version='1.0',
        description='Bot for uqcsbot',
        author='Various',
        packages=['uqcsbot'],
        install_requires=required, # It's backwards for some reason TODO fix
        )
