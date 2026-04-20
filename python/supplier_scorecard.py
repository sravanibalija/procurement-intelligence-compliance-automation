import pandas as pd

supp = pd.read_csv("data/supplier_performance_data.csv")

supp["On_Time_Delivery_Pct"] = (supp["Orders_On_Time"] / supp["Orders_Total"]) * 100
supp["Late_Delivery_Pct"] = (supp["Late_Deliveries"] / supp["Orders_Total"]) * 100
supp["Defect_Rate_Pct"] = (supp["Defect_Count"] / supp["Units_Received"]) * 100

scorecard = supp[[
    "Supplier_Name",
    "On_Time_Delivery_Pct",
    "Late_Delivery_Pct",
    "Defect_Rate_Pct",
    "Avg_Lead_Time_Days",
    "Risk_Level"
]].sort_values(by="On_Time_Delivery_Pct", ascending=False)

scorecard.to_csv("outputs/supplier_scorecard.csv", index=False)
print("Supplier scorecard created.")
