import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_excel(r"01KA3C6HDNJ2WD10KGHCJJ111E.xlsx")
print(df.head())

C= None

for col in df.columns:
    if "date" in col.lower() or "time" in col.lower():
        C = col
        break

if C is None:
    print(" not found colum for date or time")
    exit()

# بحول العمود دا لتاريخ/وقت فعلي
df["datetime"] = pd.to_datetime(df[C], errors="coerce")
df = df.dropna(subset=["datetime"])  
df["hour"] = df["datetime"].dt.hour
df["weekday"] = df["datetime"].dt.day_name()
def make_slot(h):
  
    start = (h // 2) * 2
    end = start + 1
    return f"{start:02d}:00 - {end+1:02d}:59"

df["slot"] = df["hour"].apply(make_slot)
amount_col = None
for col in df.columns:
    if "amount" in col.lower() or "total" in col.lower() or "price" in col.lower():
        amount_col = col
        break
if amount_col is None:
    df["amount_num"] = 1
else:
    df["amount_num"] = pd.to_numeric(df[amount_col], errors="coerce").fillna(0)


hourly = df.groupby("hour").agg(
    orders=("hour", "count"),
    sales=("amount_num", "sum")
).reset_index()


weekday = df.groupby("weekday").agg(
    orders=("weekday", "count"),
    sales=("amount_num", "sum")
).reset_index()


weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday["weekday"] = pd.Categorical(weekday["weekday"], categories=weekday_order, ordered=True)
weekday = weekday.sort_values("weekday")


slot = df.groupby("slot").agg( orders=("slot", "count"),sales=("amount_num", "sum")).reset_index()

print("\n=== Hourly Sales ===")
print(hourly)

print("\n=== Weekday Sales ===")
print(weekday)

print("\n=== 2-Hour Slot Sales ===")
print(slot)


slot.to_csv("cafe_time_slot_analysis.csv", index=False)
print("\nCSV saved!")




plt.figure(figsize=(10,5))
plt.bar(hourly["hour"], hourly["sales"])
plt.title("Sales by Hour")
plt.xlabel("Hour")
plt.ylabel("Sales")
plt.grid()
plt.show()

plt.figure(figsize=(10,5))
plt.bar(weekday["weekday"], weekday["sales"])
plt.title("Sales by Weekday")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.grid()
plt.show()


plt.figure(figsize=(12,5))
plt.bar(slot["slot"], slot["sales"])
plt.title("Sales by Time Slot (2 hours)")
plt.xlabel("Slot")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid()
plt.show()