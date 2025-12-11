import pandas as pd
import datetime
import sys
import re

# ---------- ANSI COLORS ----------
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

# ---------- GOOGLE SHEET CSV URL ----------
SHEET_URL = "https://docs.google.com/spreadsheets/d/1sFBhxfaTkvMpST4VMKWi8qYtMSEvdyFt/export?format=csv&gid=159509381"

def pretty_box(title, body_lines):
    width = max(len(line) for line in body_lines) + 4
    top = f"{BLUE}┏{'━' * width}┓{RESET}"
    mid = f"{CYAN}┃ {title.center(width - 2)} ┃{RESET}"
    separator = f"{BLUE}┠{'─' * width}┨{RESET}"
    bottom = f"{BLUE}┗{'━' * width}┛{RESET}"

    body = "\n".join([
        f"{GREEN}┃{RESET} {line.ljust(width - 2)} {GREEN}┃{RESET}"
        for line in body_lines
    ])

    return f"{top}\n{mid}\n{separator}\n{body}\n{bottom}"

# ---------- LOAD SHEET ----------
try:
    df = pd.read_csv(SHEET_URL)
    print(f"{GREEN}Loaded menu from Google Sheets.{RESET}")
except Exception as e:
    print(f"{RED}Error loading sheet: {e}{RESET}")
    sys.exit()

# ---------- SANITIZE COLUMNS ----------
original_cols = df.columns.tolist()
df.columns = [re.sub(r"\s+", "", str(col)).lower() for col in df.columns]

# ---------- FIND TODAY ----------
today = datetime.datetime.now().strftime("%A").lower()

today_col = None
for col in df.columns:
    if today in col:
        today_col = col
        break

if today_col is None:
    print(f"{YELLOW}Could not find today's column in sheet.{RESET}")
    print("Available columns:", original_cols)
    sys.exit()

# ---------- EXTRACT MENU ITEMS ----------
items = df[today_col].dropna().tolist()
items = [str(x).strip() for x in items if str(x).strip().lower() != "nan"]

if not items:
    print(f"{YELLOW}No items found for today ({today}).{RESET}")
    sys.exit()

# ---------- BUILD PRETTY LINES ----------
lines = [f"{YELLOW}{i+1}. {item}{RESET}" for i, item in enumerate(items)]

# ---------- PRINT MENU ----------
title = f"MESS MENU FOR {today.upper()}"
print(pretty_box(title, lines))
