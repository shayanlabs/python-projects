# 🏪 Shop Tycoon — build 01: dictionaries
# Steps are in Obsidian: 3_Resources/worksheets/python/shop-tycoon-build-01.md
# Run after every step:  python3 ~/python-projects/02-shop-tycoon/shop.py
# You write every line below the STEP comments yourself.

money = 100   # given: the player's starting money, in rupees

# STEP 1 — make the prices dictionary, then print it

prices = {"apple": 20, "bread": 50, "milk": 120, "juice": 30} 
stock = {"apple": 5, "bread": 3, "milk": 2, "juice": 4}
bag = { }
print(f"🏪 Welcome to the shop! You have Rs {money}.")

# STEP 2 — print the menu, one line per item

while True:
    for item, price in prices.items():
        print(f"{item} - Rs {price} ({stock[item]} left)")

    # STEP 3 — ask what to buy, and check the shop sells it
    question = input("What do you want to buy? ").lower().strip()
    if question in prices:
        if stock[question] > 0:
            print(f"You picked {question}")
            if money >= prices[question]:
                money = money - prices[question]
                stock[question] = stock[question] - 1
                if question in bag:
                    bag[question] = bag[question] + 1
                else:
                    bag.update({question: 1})
                print(f"✅ Bought {question}. Money left: Rs {money}")
            else:
                print(f"❌ Not enough money for {question}.")
        else:
            print(f"📦 Sold out: {question}.")
    elif question == "done":
        break
    else:
        print("🤷 We don't sell that.")
# STEP 4 — pay for it (only if there is enough money)


# STEP 5 — a stock dictionary: buying takes one off the shelf


# STEP 6 — keep shopping until the player types done
print(f"Money left: Rs {money}")
# 👑 BOSS — a bag dictionary that counts what you bought, printed as a receipt
for i, k in bag.items():
    print(f"{i} × {k}")
