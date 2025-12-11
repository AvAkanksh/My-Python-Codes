#!/usr/bin/env python3

import pandas as pd
import datetime
import requests
from io import StringIO
import math

SHEET_URL = "https://docs.google.com/spreadsheets/d/1sFBhxfaTkvMpST4VMKWi8qYtMSEvdyFt/export?format=csv&gid=159509381"

# Important category labels (arrow)
IMPORTANT_TAGS = {
    "main dish", "main", "dry", "gravy", "dal", "rice", "indian bread", "chutney",
    "snack", "dry vegetable", "curry", "special rice", "soup",
    "sweet dish", "desserts", "sweet dish /desserts", "extras*",
    "sambhar", "rasam", "sambhar/rasam", "rasam/sambhar"
}

# Meal headers
MEAL_HEADERS = {"BREAKFAST", "LUNCH", "TIFFIN", "DINNER"}


def fetch_csv(url):
    r = requests.get(url)
    r.raise_for_status()
    return pd.read_csv(StringIO(r.text))


def find_today_column(df):
    """Today’s date is in ROW 0."""
    today = datetime.date.today()

    date_row = df.iloc[0]
    for col in df.columns[2:]:
        cell = str(date_row[col]).strip()
        if cell:
            try:
                parsed = pd.to_datetime(cell).date()
                if parsed == today:
                    return col
            except:
                pass
    return None


def is_header(value):
    return str(value).strip().upper() in MEAL_HEADERS


def clean(text):
    return str(text).strip().lower()


def value_or_none(v):
    """Convert NaN → None."""
    if v is None:
        return None
    if isinstance(v, float) and math.isnan(v):
        return None
    if str(v).strip().lower() == "nan":
        return None
    if str(v).strip() == "":
        return None
    return str(v).strip()


def format_line(label, item):
    """Arrow for important items, bullet for others."""
    if not item:
        return None
    label_clean = clean(label)
    if label_clean in IMPORTANT_TAGS:
        return f"> {item}"
    return f"• {item}"


def print_header(name):
    print("\n" + "-" * 50)
    print(name.upper())
    print("-" * 50)


def main():
    df = fetch_csv(SHEET_URL)

    today_col = find_today_column(df)
    if not today_col:
        print("Today's column not found in sheet.")
        return

    today = datetime.date.today()
    print("=" * 60)
    print(f" MENU FOR {today.strftime('%A').upper()} - {today.strftime('%d-%b-%Y')} ")
    print("=" * 60)

    current_section = None

    for i in range(1, len(df)):
        colA = value_or_none(df.iloc[i, 0])
        colB = value_or_none(df.iloc[i, 1])
        item = value_or_none(df.at[i, today_col])

        # Section header
        if colA and is_header(colA):
            current_section = colA.upper()
            print_header(current_section)
            continue

        # Skip empty rows
        if not colA and not colB:
            continue

        # Determine category label (A preferred, otherwise B)
        label = colA if (colA and not is_header(colA)) else colB
        if not label:
            # If still no label, treat as ordinary item
            label = "other"

        line = format_line(label, item)
        if line:
            print(line)

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
