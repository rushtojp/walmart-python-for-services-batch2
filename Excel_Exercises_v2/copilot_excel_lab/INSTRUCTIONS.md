# Setup & Step-by-Step Lab Instructions

## What's in this pack

```
copilot_excel_lab/
├── COPILOT_PROMPTS.md            <- 10 graduated prompts + anti-patterns
├── INSTRUCTIONS.md               <- this file
├── data/
│   ├── leave_balances.xlsx       <- 20 employees, live Balance formula, 3 planted cases
│   ├── leave_raw.csv             <- same data as CSV (no formulas)
│   └── tickets.csv               <- 60 tickets, 4 queues, 6 months (Jan–Jun 2026)
├── starters/                     <- what participants START from (script track)
│   ├── starter_1_flag_balances.py    <- STEP stubs; raises NotImplementedError until completed
│   └── starter_2_ticket_summary.py
├── notebooks/                    <- Jupyter track (same exercises, cell by cell)
│   ├── lab_1_leave_balances.ipynb        <- exercise notebook with STEP stubs + prompt pointers
│   ├── lab_2_ticket_summary.ipynb
│   ├── solution_1_leave_balances.ipynb   <- executed; real outputs embedded
│   └── solution_2_ticket_summary.ipynb
└── solutions/
    ├── solution_1_flag_balances.py   <- verified answer to Prompts 1–3
    └── solution_2_ticket_summary.py  <- verified answer to Prompts 4–7
```

All data is fictional teaching data. Planted cases in the leave file: **E1018** (balance −3), **E1019** (balance 0), **E1020** (balance 2). Both solutions were executed and pass their asserts before shipping.

**Two delivery tracks, same content:**
- **Script track** (`starters/` → `solutions/`): for VS Code + Copilot Chat. Each starter keeps the STEP comments as the task spec and raises `NotImplementedError` per step until completed — an unfinished starter fails loudly, never silently.
- **Notebook track** (`notebooks/`): for Jupyter / Colab / VS Code notebooks. Lab notebooks carry the same STEP stubs cell by cell, with a markdown pointer to the matching Copilot prompt; solution notebooks were executed end-to-end and ship with their real outputs embedded.
- The `.py` and `.ipynb` versions are **generated from the same source** — the notebooks are derived from the starter/solution scripts, and starters are derived from solutions by stubbing the STEP blocks, so the tracks cannot drift.
- If using Jupyter, install it in the venv too: `pip install notebook` (or use VS Code's built-in notebook support with `pip install ipykernel`).

---

## Part A — Environment setup (10 min, once)

**Step 1 — Check Python.** Open a terminal and run:
```bash
python --version
```
You need 3.9 or newer. (On macOS/Linux the command may be `python3`.)

**Step 2 — Create and activate a virtual environment** in the lab folder:
```bash
cd copilot_excel_lab
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

**Step 3 — Install the three libraries used in every exercise:**
```bash
pip install pandas openpyxl matplotlib
```

**Step 4 — Verify the install** by running the shipped solution:
```bash
cd solutions
python solution_1_flag_balances.py
```
Expected final line: `PASS: all 3 planted cases flagged correctly`.
If you see it, your environment is correct. If not, fix the environment *before* touching Copilot — do not debug environment problems through generated code.

**Step 5 — Copilot access.** Sign in to GitHub in VS Code and confirm the Copilot Chat panel opens. Whether you're on a paid plan or the Free tier, the prompts in this pack work as plain chat messages. **[VERIFY]** your organisation's Copilot policy and current Free-tier limits in the official docs before class — do not quote limits from memory.

---

## Part B — The lab flow (per prompt, ~8–10 min each)

Every prompt follows the same five-step loop. Teach the loop once; it is the whole habit.

**Step 1 — Paste the prompt** from `COPILOT_PROMPTS.md` into Copilot Chat, exactly as written. Note how specific it is: file name, sheet name, column names, output format.

**Step 2 — Read the generated code before running anything.** Say out loud (or write in a comment) what each line does. If any line is a mystery, ask Copilot Prompt 9-style: *"explain line 4 to me."*

**Step 3 — Save and run** it from the lab folder:
```bash
python my_script.py
```
Run from the `copilot_excel_lab` folder so the relative paths (`data/...`) resolve. The shipped solutions live in `solutions/` and therefore use `../data/...` — if you save your script at the top level, use `data/...` instead. Path errors are the #1 beginner failure; this is a teaching moment, not a defect.

**Step 4 — Check "done means."** Every prompt has an objective check (3 flagged rows, total = 60, etc.). If the check fails, the code is wrong even if it ran cleanly — go back to Step 2.

**Step 5 — Compare with the solution** in `solutions/` only after your version passes. Differences are discussion material: is Copilot's version more readable? More fragile?

### Suggested session sequencing (fits a 30-min individual exercise)

| Minutes | Activity |
|---|---|
| 0–3 | Prompt 0 + Prompt 1 (read the file) |
| 3–10 | Prompt 3 (flag the balances) — the core exercise |
| 10–15 | Hint checkpoint: reveal that exactly 3 rows must flag |
| 15–25 | Prompt 4 + Prompt 6 (counts + reconciled pivot) |
| 25–30 | Walkthrough against solutions; name common errors |

Prompts 7–8 (Excel export, chart) and Prompt 10 (planted bug) fit a team/extension block.

---

## Part C — Facilitator notes

- **Why the xlsx has a formula column:** `Balance` is `=D-E`, not a hardcoded value. pandas reads the *cached* value LibreOffice/Excel computed — good moment to explain that pandas reads values, not formulas.
- **Why planted cases:** an exercise without an objective check teaches "it ran" as success. The three planted IDs make correctness binary and self-checkable.
- **Why the reconciliation assert (Prompt 6):** this is the 70/30 thesis in one line of code — Copilot produces the analysis, Python proves it against the source. It foreshadows the Day 7 "trust but verify" session.
- **Regenerating the data:** the datasets were generated with a fixed random seed; if you need fresh variants (e.g., per-cohort answer sheets), ask for the generator script.
- **What was verified before shipping:** both solutions executed end-to-end in a clean environment; the xlsx recalculated with 0 formula errors across 20 formulas; the pivot grand total reconciles to 60 raw rows. What was **not** verified and must be checked pre-delivery: current Copilot Chat UI syntax (`#file`, slash commands) and Free-tier limits — both change frequently and are flagged **[VERIFY]** wherever referenced.
