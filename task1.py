
import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print("Initial Shape:", df.shape)

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

print("Duplicates Removed:", before - after)

df["orderdate"] = pd.to_datetime(df["orderdate"], errors="coerce")
df["orderdate"] = df["orderdate"].dt.strftime("%d-%m-%Y")

print(df[["addressline2", "state", "territory", "postalcode"]].isnull().sum())

df["addressline2"] = df["addressline2"].fillna("N/A")

df["state"] = df["state"].fillna("N/A")

df["territory"] = df.apply(
    lambda x: "NA"
    if pd.isnull(x["territory"]) and x["country"].strip().upper() == "USA"
    else ("Unknown" if pd.isnull(x["territory"]) else x["territory"]),
    axis=1
)

df["postalcode"] = df["postalcode"].astype(str)
df["postalcode"] = df["postalcode"].replace("nan", "N/A")
df["postalcode"] = df["postalcode"].fillna("N/A")

print(df[["addressline2", "state", "territory", "postalcode"]].isnull().sum())

cols = [
    "status",
    "productline",
    "dealsize",
    "country",
    "city",
    "customername"
]

for col in cols:
    df[col] = df[col].astype(str).str.strip()

int_cols = [
    "ordernumber",
    "quantityordered",
    "orderlinenumber",
    "msrp",
    "qtr_id",
    "month_id",
    "year_id"
]

float_cols = [
    "priceeach",
    "sales"
]

str_cols = [
    "orderdate",
    "postalcode"
]

for col in int_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

for col in float_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

for col in str_cols:
    df[col] = df[col].astype(str)

print("Total Nulls:", df.isnull().sum().sum())

assert df.isnull().sum().sum() == 0

print("Final Shape:", df.shape)
print(df.dtypes)

df.to_csv("sales_data_cleaned.csv", index=False)

print("File Saved: sales_data_cleaned.csv")
