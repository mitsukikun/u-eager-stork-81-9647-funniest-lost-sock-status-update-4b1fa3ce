import os

# Entry line limit: 120 characters max.
OPENING = "Day 9 behind the dryer. My partner escaped."
MIDDLE = " New life with a dust bunny now."
CLOSING = " Tell the drawer I said goodbye."

LINE = OPENING + MIDDLE + CLOSING

MAX_CHARS = 120

if len(LINE) > MAX_CHARS:
    raise ValueError("line exceeds 120 characters")

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as handle:
    handle.write(LINE)
