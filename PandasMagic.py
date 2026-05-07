import pandas as pd

df = pd.DataFrame({
    "date": ["2024-01-03", "2024-01-10", "2024-01-12", "2024-02-01", "2024-02-03", "2024-02-10"],
    "city": [" singapore ", "SINGAPORE", "tokyo", "TOKYO ", " singapore", "Tokyo"],
    "product": [" apple", "APPLE ", "banana", "BANANA ", "apple", " banana"],
    "sales": [100, 150, 80, 120, 200, 90]
})

# 1) clean ugly text
df["city"] = df["city"].str.strip().str.title()
df["product"] = df["product"].str.strip().str.title()

# 2) turn date text into real dates
df["date"] = pd.to_datetime(df["date"])

# 3) pull out month
df["month"] = df["date"].dt.to_period("M")

# 4) group and add up sales
summary = (
    df.groupby(["month", "city", "product"], as_index=False)["sales"]
      .sum()
)

# 5) reshape into a neat report
report = summary.pivot_table(
    index=["month", "city"],
    columns="product",
    values="sales",
    fill_value=0
)

print(df)
print("\n--- summary ---")
print(summary)
print("\n--- report ---")
print(report)