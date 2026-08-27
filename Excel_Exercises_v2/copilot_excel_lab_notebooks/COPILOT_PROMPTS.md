# GitHub Copilot Chat — Excel + Python Prompt Library

**Audience:** beginners learning Python for Excel automation with Copilot as the drafting tool.
**Data:** `data/leave_balances.xlsx`, `data/leave_raw.csv`, `data/tickets.csv` (fictional teaching data).
**Habit being taught:** *Copilot drafts, you read, then you run.* Never run generated code you haven't read line by line.

> These prompts are written in plain natural language so they work in GitHub Copilot Chat (VS Code, paid or Free tier) and in most other AI chat surfaces. Where a Copilot-specific feature is referenced (e.g., `#file` context, `/explain`), it is marked **[VERIFY]** — confirm behaviour in the current Copilot docs for your tenant/plan before teaching it, as the UI changes frequently.

---

## Warm-up — make Copilot explain before it writes

**Prompt 0 (comprehension first):**
```
I'm a beginner. Before writing any code, explain in 3 bullet points what the
pandas library does and why I'd use it instead of opening Excel by hand.
```

---

## Level 1 — Reading Excel data

**Prompt 1 (read and show):**
```
Write a Python script using pandas that reads the file data/leave_balances.xlsx
(sheet name "LeaveBalances", first 20 data rows only), then prints the column
names and the first 5 rows. Add a comment above every line explaining what it does.
```
*Done means:* you see 6 columns ending in `Balance`, and 5 rows of employee data.

**Prompt 2 (targeted filter):**
```
Extend that script: filter the DataFrame to only rows where Department is
"Payroll" and print the result sorted by Balance ascending. Explain what
.sort_values does in a comment.
```
*Done means:* Sara (E1018) appears first with Balance −3.

---

## Level 2 — Flags and business rules (the trust layer)

**Prompt 3 (conditional flags):**
```
Add a new column called "Flag" to the leave balances DataFrame using these rules:
- Balance below 0  -> "NEGATIVE - investigate"
- Balance exactly 0 -> "ZERO - no leave left"
- Balance below 3 (but above 0) -> "LOW - below 3 days"
- everything else -> "OK"
Print only the rows that are not OK. Use a plain function with if/elif so a
beginner can read it — no lambda, no np.select.
```
*Done means:* **exactly 3 rows** are flagged: E1018 (negative), E1019 (zero), E1020 (low). If you get any other count, the code is wrong — read it again. This is the planted-case check.

---

## Level 3 — Counting and grouping (tickets.csv)

**Prompt 4 (value counts):**
```
Write a Python script that reads data/tickets.csv with pandas and prints how
many tickets are in each Queue, sorted from most to fewest.
```
*Done means:* four queues, counts summing to 60.

**Prompt 5 (groupby, two levels):**
```
Extend it: count tickets by Queue AND Status, so I can see how many Open vs
Closed tickets each queue has. Explain the difference between value_counts()
and groupby() in comments.
```

**Prompt 6 (pivot + reconciliation):**
```
Create a pivot table from tickets.csv: rows = month of DateOpened, columns =
Queue, values = count of tickets, missing values shown as 0. Then add an assert
that checks the pivot's grand total equals the number of rows in the raw file,
and print PASS if it matches. Explain why that check matters.
```
*Done means:* the assert passes with total 60. This is the "trust but verify" pattern from Day 7 — every number Copilot produces gets reconciled to the source.

---

## Level 4 — Writing back to Excel

**Prompt 7 (export):**
```
Take the queue counts and the monthly pivot and write them to a new Excel file
called ticket_summary_output.xlsx with two sheets: "ByQueue" and "MonthlyPivot".
Use pandas ExcelWriter with the openpyxl engine.
```
*Done means:* the file opens in Excel with two named sheets and no error values.

**Prompt 8 (chart — optional stretch):**
```
Using matplotlib, make a labelled bar chart of ticket counts per queue from
tickets.csv. Title it "Tickets by Queue", label both axes, and save it as
tickets_by_queue.png. Do not use plt.show().
```

---

## Level 5 — Debugging and understanding (the read-before-run habit)

**Prompt 9 (explain someone else's code):**
```
Explain this code to me line by line as if I've never seen pandas. Then tell me
one thing that could go wrong if the input file had a missing value in the
Balance column.
[paste the code from solutions/solution_1_flag_balances.py]
```

**Prompt 10 (fix a planted bug):**
```
This script should flag balances below 3 but it flags nothing. Find the bug,
explain it in one sentence, then show the corrected line only:
[paste code where the comparison is written as  df["Balance"] > 3 ]
```

---

## Copilot-specific variants **[VERIFY current UI before teaching]**

In VS Code with the file open, Copilot Chat supports referencing context rather than pasting:

- `#file:tickets.csv` style file references, and slash commands like `/explain` and `/fix` on selected code, have existed in Copilot Chat — but exact syntax and availability differ by version and plan. **Verify in the current GitHub Copilot documentation and in your actual tenant build before putting them on a slide.**
- GitHub Copilot has offered a **Free tier** with monthly limits on completions and chat messages. Limits and model availability change — **verify current numbers on github.com/features/copilot before quoting any figure to participants.** Do not state specific limits from memory.

## Anti-patterns to demonstrate live

1. **The vague prompt:** "analyze my excel file" → show the generic, wrong-column output, then contrast with Prompt 1. Specific file, sheet, columns, and output = usable code.
2. **The unread run:** run a generated snippet that "works" but reads the wrong sheet — the numbers look plausible and are wrong. This motivates every verification check above.
3. **The hardcoded answer:** Copilot sometimes computes a total in Python and prints it as if verified. The reconciliation assert in Prompt 6 is the antidote.
