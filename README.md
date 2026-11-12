# 🐍 Python Projects

**Python builds, learnt the AI-era way: AI drafts, I turn its code into my own plan, then rebuild it from that plan. One new idea at a time.**

| # | Project | What it does | Python it uses | Status |
|---|---|---|---|---|
| 01 | [🏏 Match Scorecard](01-match-scorecard/) | A cricket scorecard you type ball by ball: totals every over, says how many runs are still needed, finds the best over and counts boundaries | a function, `input()`, a `while` check with `.isdecimal()`, nested `for` loops with `range(1, n + 1)`, running totals, a running max, `round()`, f-strings | ✅ shipped 13 Nov 2026 |

## 🔧 How every project is made

AI writes the first draft. I do the understanding:

1. **Spec:** I write exactly what the program must do.
2. **Draft:** AI writes the first version.
3. **Plan:** I read the code and write it as a plan in plain English.
4. **Rebuild:** I close the code and write the program again from my plan, in my own file.
5. **Same input, same output:** both versions must print the same thing.

**The rule:** if I can't explain a line, it doesn't ship. AI never debugs for me.

## 🚀 Wild ideas

Side builds in `wild/` (the first one is coming): AI gives me a wild idea, I research how it works and write the brief, AI writes the code, and I question it until I understand every part.

## ▶️ Run a project

Plain Python 3, nothing to install:

```bash
python3 01-match-scorecard/match_scorecard.py
```
