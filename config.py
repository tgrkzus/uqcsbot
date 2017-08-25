import logging
import os;

BACKEND = 'Slack'

# Bot config
BOT_DATA_DIR = r'data/'
BOT_EXTRA_PLUGIN_DIR = 'plugins/'

BOT_LOG_FILE = r'errbot.log/'
BOT_LOG_LEVEL = logging.DEBUG

BOT_PREFIX = '!'
BOT_IDENTITY = {
        'token': os.environ["SLACK_BOT_TOKEN"] 
        }

BOT_ADMINS = ('@tgrkzus', )

CORE_PLUGINS = ()
