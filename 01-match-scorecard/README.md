# 🏏 01 · Match Scorecard

> 🛠️ **Building.** The sample run below is what it's built to print.

A cricket scorecard you type ball by ball. It adds up every over, keeps a running total, finds the best over, counts fours and sixes, and tells you whether the target was chased.

## Run it

```bash
python3 match_scorecard.py
```

## What it prints

```text
🏏 Match Scorecard
Overs: 2
Target: 20
Over 1, ball 1: 1
...
📋 Over 1: 9 runs · Total 9 · 🎯 Need 11 more
...
📋 Over 2: 14 runs · Total 23 · ✅ Target passed
━━━━━━━━━━━━━━━━━━
🏏 Total: 23 runs in 2 overs
📈 Run rate: 11.5
⭐ Best over: over 2 (14 runs)
💥 Boundaries: 3 (fours 2, sixes 1)
🏆 Target chased by 3 runs!
```

## Ideas inside

- **A loop inside a loop:** overs on the outside, balls on the inside.
- **Running totals:** one resets every over, one never resets.
- **A keeper:** the best over's runs *and* which over it was, in two variables.
- **`round()`** for the run rate.
