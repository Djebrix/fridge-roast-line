"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line about a smart fridge to entry.txt.

The roast targets the fridge's firmware update locking the ice maker
behind a terms-of-service screen: a specific smart-fridge behaviour
(firmware updates, ice maker, touchscreen EULA) rather than the generic
"it orders groceries" or "it watches you" cracks the judge has heard
a thousand times. The punchline turns on the last clause -- even the
freezer, the coldest and dumbest part of the appliance, now demands a
legal agreement before it will do its one job.
"""

import os

LINE = (
    "My smart fridge updated its firmware and now the ice maker "
    "refuses to make ice until I accept the terms \u2014 even my freezer has a EULA."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
