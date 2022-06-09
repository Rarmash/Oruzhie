from dotenv import load_dotenv

from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

token = os.environ["TOKEN"]
log_channel = 952519133117960192
admin_id = 390567552830406656