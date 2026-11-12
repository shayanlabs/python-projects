# 🏏 Match Scorecard — project 01, written by me
# Built the Rebuild way: I wrote it with the AI's draft (ai_draft.py) closed, and both print the same.
# Run: python3 ~/python-projects/01-match-scorecard/match_scorecard.py


BALLS_PER_OVER = 6

def ask_number(question, lowest, highest):
    answer = input(question)
    while not answer.isdecimal() or int(answer) < lowest or int(answer) > highest:
        print(f"⚠️ Type a whole number from {lowest} to {highest}.")
        answer = input(question)
    return int(answer)

print("🏏 Match Scorecard")
overs = ask_number("Overs: ", 1, 50)
target = ask_number("Target: ", 1, 999)

total = 0
fours = 0
sixes = 0
best_over = 1
best_runs = 0

for over in range(1, overs + 1):
    over_runs = 0
    for ball in range(1, BALLS_PER_OVER + 1):
        runs = ask_number(f"Over {over}, ball {ball}: ", 0, 6)
        over_runs += runs
        if runs == 4:
            fours += 1
        elif runs == 6:
            sixes += 1
    total += over_runs
    if over_runs > best_runs:
        best_runs = over_runs
        best_over = over
    need = target - total
    if need > 0:
        print(f"📋 Over {over}: {over_runs} runs · Total {total} · 🎯 Need {need} more")
    else:
        print(f"📋 Over {over}: {over_runs} runs · Total {total} · ✅ Target reached")

run_rate = round(total/overs, 2)
print("━━━━━━━━━━━━━━━━━━")
print(f"🏏 Total: {total} runs in {overs} overs")
print(f"📈 Run rate: {run_rate}")
print(f"⭐ Best over: over {best_over} ({best_runs} runs)")
print(f"💥 Boundaries: {fours + sixes} (fours {fours}, sixes {sixes})")
