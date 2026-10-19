import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def segment_customers(rfm, n_clusters=3):
    rfm = rfm.copy()

    features = ["Recency", "Frequency", "Monetary"]
    X = rfm[features].copy()

    X["Recency"] = X["Recency"].clip(lower=1)
    X["Frequency"] = X["Frequency"].clip(lower=1)
    X["Monetary"] = X["Monetary"].clip(lower=1)

    X = X.apply(lambda column: __import__("numpy").log1p(column))

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(X)

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    rfm["Segment"] = model.fit_predict(scaled_features)

    return rfm