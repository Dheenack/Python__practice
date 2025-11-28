import pandas as pd

# Step 1: Data ingestion (simulation)
data = {
    "user": ["A", "B", "C"],
    "transactions": [120, 350, 500]
}
df = pd.DataFrame(data)

# Step 2: Processing
df["discount"] = df["transactions"] * 0.10

# Step 3: Analytics
high_spenders = df[df["transactions"] > 300]

print(high_spenders)
