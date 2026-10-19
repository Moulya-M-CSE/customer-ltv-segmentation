import pandas as pd
from pathlib import Path


def load_data(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    data = pd.read_csv(path)

    required_columns = {
        "InvoiceNo",
        "InvoiceDate",
        "CustomerID",
        "TotalAmount"
    }

    if not required_columns.issubset(data.columns):
        raise ValueError("Dataset is missing required columns.")

    return data