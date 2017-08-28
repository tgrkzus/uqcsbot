# Requires
- Python 3.x (may need python-dev)

# Setup
- Clone the repo
- Optionally create a virtualenv with python3 (``virtualenv --python `which python3` [PATH]``)
  - Activate env: `source [PATH]/bin/activate`
- Run `python setup.py install`
- Setup tokens (i.e. `export THING=stuff`):
  - `SLACK_BOT_TOKEN` - Bot token you can get from the slack api (TODO better instr)
  - `SLACK_ADMIN_TOKEN` - If you want to do any admin specific features (this is only used for !muterip right now)
- Run `errbot` in the `uqcsbot` directory (TODO setuptools run?)

# New plugins
- Go into `uqcsbot/plugins`
- Run `errbot --new-plugin [NAME]` and follow the prompts
- Go into your new plugin folder
- Edit your `.plug` file for documentation 
- Your `.py` file will contain all the functions you might need (you can remove the ones you don't want/need)

# Docs
[Errbot docs](http://errbot.io/en/latest/)
