import os
import time
import subprocess
from dotenv import load_dotenv
from pypresence import Presence

load_dotenv()


DISCORD_CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")

def get_opencomic_window():
    try:
        window_id = subprocess.check_output(["xdotool", "search", "--onlyvisible", "--class", "OpenComic", "getwindowname"]).decode().strip()
        return window_id if window_id else None
    except subprocess.CalledProcessError:
        return None

try:
    rpc = Presence(DISCORD_CLIENT_ID)
    rpc.connect()

    while True:
        window_details = get_opencomic_window().split(".")[0]

        try: 
            manga_name, chapter = window_details.split("_")
            manga_name = manga_name.replace("-", " ").title()
            chapter = ''.join(filter(str.isdigit, chapter))
        except Exception as e:
            manga_name = None
            chapter = None

        status = f"Reading: {manga_name}" 
        progress = f"Chapter: {chapter}"
        if not manga_name:
            status = "Searching for manga"
            progress = "^-^"
        if not chapter:
            progress = "^-^"

        try:
            rpc.update(state=progress, details=status)
            print(f"Updated Presence: {status} | {progress}")
        except Exception as e:
            print(f"Failed to update presence: {e}")

        time.sleep(30)
except Exception as e:
    print(f"Failed to connect to Discord RPC: {e}")
