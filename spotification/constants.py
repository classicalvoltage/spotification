import os
import time
import json

"""
PYTHON
"""
YMD_FMT = "%Y-%m-%d"
YMD_FMT_NODASH = "%Y%m%d"
YMDHMS_FMT = "%Y-%m-%d %H:%M:%S"
YMDHMS_FMT_NODASH = "%Y%m%dT%H%M%S"

"""
PATHS
"""

### GLOBAL PATHS
with open("/root/paths/volumes.json", "r") as fp:
    VOLUMES = json.load(fp)

REPO_PATH = VOLUMES['volume1']

"""

"""

SPOTIFY_CREDS_PATH = "/root/credentials/spotify.json"
with open(SPOTIFY_CREDS_PATH, "r") as fp:
    SPOTIFY_CLIENT_ID = json.load(fp)['client_id']
    SPOTIFY_CLIENT_SECRET = json.load(fp)['client_secret']