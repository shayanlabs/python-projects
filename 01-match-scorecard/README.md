# 🏏 01 · Match Scorecard

> ✅ **Shipped 13 Nov 2026, the Rebuild way:** spec → AI draft → my plan from the code → I rebuilt it from my plan → same input, same output.

A cricket scorecard you type ball by ball. It adds up every over, keeps a running total, says how many runs are still needed for the target, finds the best over and counts fours and sixes.

## Files

- `match_scorecard.py`: the AI's first draft, written from my spec.
- `my_try.py`: my rebuild, written from my own plan with the draft closed. Both print the same thing on the same input.

## Run it

```bash
python3 my_try.py
```

## A real run

Overs `2`, target `15`, over 1: `0 4 1 1 6 0`, over 2: `1 1 4 7 0 2 0` (the `7` is turned away). Ball questions left out:

```text
🏏 Match Scorecard
📋 Over 1: 12 runs · Total 12 · 🎯 Need 3 more
⚠️ Type a whole number from 0 to 6.
📋 Over 2: 8 runs · Total 20 · ✅ Target reached
━━━━━━━━━━━━━━━━━━
🏏 Total: 20 runs in 2 overs
📈 Run rate: 10.0
⭐ Best over: over 1 (12 runs)
💥 Boundaries: 3 (fours 2, sixes 1)
```

## Ideas inside

- **A loop inside a loop:** overs on the outside, balls on the inside.
- **Running totals:** one resets every over, one never resets.
- **A keeper:** the best over's runs *and* which over it was, in two variables.
- **`round()`** for the run rate.
- **`.isdecimal()`:** letters, symbols and silly numbers are asked again, never crash it.

## Bugs I fixed in my rebuild

- `answer.isdecimal` without `()` never runs the check.
- `input()` gives text: it has to go through `int()` before comparing or returning it.
- Adding each ball to the total *and* the over's runs counted every run twice.
