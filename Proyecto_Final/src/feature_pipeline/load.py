"""
Load & time-split the raw dataset.

- Production default writes to data/raw/
- Tests can pass a temp `output_dir` so nothing in data/ is touched.
"""

import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")




if __name__ == "__main__":
    load_and_split_data()
