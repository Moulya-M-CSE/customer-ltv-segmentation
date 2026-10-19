import pandas as pd
from src.customer_analysis import calculate_rfm


def test_calculate_rfm():
    data = pd.DataFrame({
        "CustomerID": [101, 101, 102],
        "InvoiceDate": [
            "2026-01-01",
            "2026-01-05",
            "2026-01-03"
        ],
        "InvoiceNo": ["INV1", "INV2", "INV3"],
        "TotalAmount": [100, 200, 150]
    })

    result = calculate_rfm(data)

    assert len(result) == 2
    assert "Recency" in result.columns
    assert "Frequency" in result.columns
    assert "Monetary" in result.columns