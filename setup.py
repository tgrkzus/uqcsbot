from setuptools import setup
from setuptools.command.install import install
import os
import readline

with open('requirements.txt') as f:
    required = f.read().splitlines()


class SetupTokens(install):
        def run(self):
            install.run(self)
            # Process tokens
            botToken = ""
            adminToken = ""

            # Prompt for tokens or get current
            print("")
            print("Checking bot tokens...")
            botToken = input("Slack bot token (Empty if unchanged): ")
            os.environ["SLACK_BOT_TOKEN"] = botToken

            adminToken = input("Slack admin token (Empty if unchanged:): ")
            os.environ["SLACK_ADMIN_TOKEN"] = adminToken

            print("")
            print("Using tokens:")
            print("SLACK_BOT_TOKEN: " + botToken)
            print("SLACK_ADMIN_TOKEN: " + adminToken)

setup(
        name='uqcsbot',
        version='1.0',
        description='Bot for uqcsbot',
        author='Various',
        packages=['uqcsbot'],
        install_requires=required,
        cmdclass={'install': SetupTokens}
        )

