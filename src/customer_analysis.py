import pandas as pd


def calculate_rfm(data):
    data = data.copy()
    data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])

    reference_date = data["InvoiceDate"].max() + pd.Timedelta(days=1)

    rfm = data.groupby("CustomerID").agg(
        Recency=("InvoiceDate", lambda dates: (reference_date - dates.max()).days),
        Frequency=("InvoiceNo", "nunique"),
        Monetary=("TotalAmount", "sum")
    )

    return rfm.reset_index()