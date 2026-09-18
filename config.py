# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv
load_dotenv()

# ════════════════════════════════════════════════════════════════════════════════
# ░ CONFIGURATION SETTINGS
# ════════════════════════════════════════════════════════════════════════════════

# VPS --- FILL COOKIES 🍪 in """ ... """ 
INST_COOKIES = """
# write up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

# ─── BOT / DATABASE CONFIG ──────────────────────────────────────────────────────
API_ID       = os.getenv("API_ID", "23712517")
API_HASH     = os.getenv("API_HASH", "334d992b622e393e838a7c21a1aded67")
BOT_TOKEN    = os.getenv("BOT_TOKEN", "")
MONGO_DB     = os.getenv("MONGO_DB", "mongodb+srv://jaishreeshyam:shyam@cluster0.icja6lh.mongodb.net/?appName=Cluster0")
DB_NAME      = os.getenv("DB_NAME", "telegram_downloader")

# ─── OWNER / CONTROL SETTINGS ───────────────────────────────────────────────────
OWNER_ID     = list(map(int, os.getenv("OWNER_ID", "8741623856").split()))  # space-separated list
STRING       = os.getenv("STRING", None)  # optional session string
LOG_GROUP    = int(os.getenv("LOG_GROUP", "-1003937881669"))
FORCE_SUB    = int(os.getenv("FORCE_SUB", "-1003937881669"))

# ─── SECURITY KEYS ──────────────────────────────────────────────────────────────
MASTER_KEY   = os.getenv("MASTER_KEY", "gK8API_HASH     = os.getenv(\"API_HASH\", \"334d992b622e393e838a7c21a1aded67\")HzLfT9QpViJcYeB5wRa3DmN7P2xUq")  # session encryption
IV_KEY       = os.getenv("IV_KEY", "s7Yx5CpVmE3F")  # decryption key

# ─── COOKIES HANDLING ───────────────────────────────────────────────────────────
YT_COOKIES   = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)

# ─── USAGE LIMITS ───────────────────────────────────────────────────────────────
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "8840"))
PREMIUM_LIMIT  = int(os.getenv("PREMIUM_LIMIT", "50840"))

# ─── UI / LINKS ─────────────────────────────────────────────────────────────────
JOIN_LINK     = os.getenv("JOIN_LINK", "https://t.me/team_spy_pro")
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/username_of_admin")

# ════════════════════════════════════════════════════════════════════════════════
# ░ PREMIUM PLANS CONFIGURATION
# ════════════════════════════════════════════════════════════════════════════════

P0 = {
    "d": {
        "s": int(os.getenv("PLAN_D_S", 1)),
        "du": int(os.getenv("PLAN_D_DU", 1)),
        "u": os.getenv("PLAN_D_U", "days"),
        "l": os.getenv("PLAN_D_L", "Daily"),
    },
    "w": {
        "s": int(os.getenv("PLAN_W_S", 3)),
        "du": int(os.getenv("PLAN_W_DU", 1)),
        "u": os.getenv("PLAN_W_U", "weeks"),
        "l": os.getenv("PLAN_W_L", "Weekly"),
    },
    "m": {
        "s": int(os.getenv("PLAN_M_S", 5)),
        "du": int(os.getenv("PLAN_M_DU", 1)),
        "u": os.getenv("PLAN_M_U", "month"),
        "l": os.getenv("PLAN_M_L", "Monthly"),
    },
}

# ════════════════════════════════════════════════════════════════════════════════
# ░ DEVGAGAN
# ════════════════════════════════════════════════════════════════════════════════
