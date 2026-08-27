# Solution 1 - Read leave_balances.xlsx and flag risky balances
# Matches Prompts 1-3 in COPILOT_PROMPTS.md
# Expected: exactly 3 flagged rows (E1018 negative, E1019 zero, E1020 low)

import pandas as pd

# ---- STEP 1: Read the Excel file ----
# Read sheet "LeaveBalances" from ../data/leave_balances.xlsx,
# first 20 data rows only (the note row below the table must be excluded).
df = pd.read_excel("../data/leave_balances.xlsx", sheet_name="LeaveBalances", nrows=20)
# ---- END STEP 1 ----

# ---- STEP 2: Write the flag function ----
# Rules: <0 -> "NEGATIVE - investigate"; ==0 -> "ZERO - no leave left";
# <3 -> "LOW - below 3 days"; else "OK". Plain if/elif, beginner-readable.
def flag(balance):
    if balance < 0:
        return "NEGATIVE - investigate"
    elif balance == 0:
        return "ZERO - no leave left"
    elif balance < 3:
        return "LOW - below 3 days"
    return "OK"
# ---- END STEP 2 ----

# ---- STEP 3: Apply the function and filter to non-OK rows ----
df["Flag"] = df["Balance"].apply(flag)
flagged = df[df["Flag"] != "OK"]
# ---- END STEP 3 ----

print("Flagged employees:")
print(flagged[["EmployeeID", "Name", "Department", "Balance", "Flag"]].to_string(index=False))
print(f"\nTotal flagged: {len(flagged)} (expected: 3)")

# Verification check -- the 'done means' test (do not edit)
expected = {"E1018", "E1019", "E1020"}
actual = set(flagged["EmployeeID"])
assert actual == expected, f"MISMATCH: got {actual}"
print("PASS: all 3 planted cases flagged correctly")
