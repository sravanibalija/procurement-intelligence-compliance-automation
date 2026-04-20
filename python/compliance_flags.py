import pandas as pd

proc = pd.read_csv("data/raw_procurement_data.csv")
supp = pd.read_csv("data/supplier_performance_data.csv")

proc["Compliance_Flag"] = proc["Contract_Compliance"].apply(lambda x: "Flag" if x == "No" else "OK")
proc["Missing_PO_Flag"] = proc.apply(
    lambda row: "Flag" if row["Amount"] > 10000 and row["PO_Status"] == "Missing" else "OK",
    axis=1
)
proc["Delayed_Invoice_Flag"] = proc["Invoice_Processing_Days"].apply(lambda x: "Flag" if x > 30 else "OK")

merged = proc.merge(
    supp[["Supplier_ID", "Risk_Level", "Contract_Active"]],
    on="Supplier_ID",
    how="left"
)

merged["Risk_Flag"] = merged.apply(
    lambda row: "Flag" if row["Risk_Level"] == "High" and row["Amount"] > 10000 else "OK",
    axis=1
)
merged["Inactive_Contract_Flag"] = merged["Contract_Active"].apply(lambda x: "Flag" if x == "No" else "OK")

exceptions = merged[
    (merged["Compliance_Flag"] == "Flag") |
    (merged["Missing_PO_Flag"] == "Flag") |
    (merged["Delayed_Invoice_Flag"] == "Flag") |
    (merged["Risk_Flag"] == "Flag") |
    (merged["Inactive_Contract_Flag"] == "Flag")
]

exceptions.to_csv("outputs/compliance_exceptions.csv", index=False)
print("Compliance exceptions file created.")
