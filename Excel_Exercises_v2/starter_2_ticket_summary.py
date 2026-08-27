# Starter 2 - Ticket counts by queue, monthly pivot, export to Excel
# Matches Prompts 4-7 in COPILOT_PROMPTS.md
# Verification: pivot grand total must equal the raw row count (60)

import pandas as pd

# ---- STEP 1: Read tickets.csv with dates parsed ----
# TODO: write your code here (ask Copilot with the matching prompt)
raise NotImplementedError("STEP 1 not implemented")
# ---- END STEP 1 ----

# ---- STEP 2: Count tickets per queue, sorted descending ----
# TODO: write your code here (ask Copilot with the matching prompt)
raise NotImplementedError("STEP 2 not implemented")
# ---- END STEP 2 ----
print("Tickets per queue:")
print(counts.to_string())

# ---- STEP 3: Monthly pivot (rows = month, columns = queue, fill 0) ----
# TODO: write your code here (ask Copilot with the matching prompt)
raise NotImplementedError("STEP 3 not implemented")
# ---- END STEP 3 ----
print("\nMonthly pivot:")
print(pivot)

# Verification -- pivot total reconciles to raw file (do not edit)
assert pivot.values.sum() == len(df), "Pivot total does not match raw row count"
print(f"\nPASS: pivot total ({pivot.values.sum()}) == raw rows ({len(df)})")

# ---- STEP 4: Export both results to one Excel file, two sheets ----
# TODO: write your code here (ask Copilot with the matching prompt)
raise NotImplementedError("STEP 4 not implemented")
# ---- END STEP 4 ----
print("Written: ticket_summary_output.xlsx")
