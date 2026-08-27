# Solution 2 - Ticket counts by queue, monthly pivot, export to Excel
# Matches Prompts 4-7 in COPILOT_PROMPTS.md
# Verification: pivot grand total must equal the raw row count (60)

import pandas as pd

# ---- STEP 1: Read tickets.csv with dates parsed ----
df = pd.read_csv("../data/tickets.csv", parse_dates=["DateOpened"])
# ---- END STEP 1 ----

# ---- STEP 2: Count tickets per queue, sorted descending ----
counts = df["Queue"].value_counts()
# ---- END STEP 2 ----
print("Tickets per queue:")
print(counts.to_string())

# ---- STEP 3: Monthly pivot (rows = month, columns = queue, fill 0) ----
df["Month"] = df["DateOpened"].dt.to_period("M").astype(str)
pivot = pd.pivot_table(df, index="Month", columns="Queue",
                       values="TicketID", aggfunc="count", fill_value=0)
# ---- END STEP 3 ----
print("\nMonthly pivot:")
print(pivot)

# Verification -- pivot total reconciles to raw file (do not edit)
assert pivot.values.sum() == len(df), "Pivot total does not match raw row count"
print(f"\nPASS: pivot total ({pivot.values.sum()}) == raw rows ({len(df)})")

# ---- STEP 4: Export both results to one Excel file, two sheets ----
with pd.ExcelWriter("../data/ticket_summary_output.xlsx", engine="openpyxl") as xw:
    counts.rename("Count").to_excel(xw, sheet_name="ByQueue")
    pivot.to_excel(xw, sheet_name="MonthlyPivot")
# ---- END STEP 4 ----
print("Written: ticket_summary_output.xlsx")
