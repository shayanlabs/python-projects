# 🏪 02 · Shop Tycoon

> 🛠️ **Building, one lesson at a time.** ✅ Lesson 1: dictionaries (26 Nov 2026). Next: functions.

A small shop game. You start with Rs 100 and buy from a menu until you type `done`. The shop checks that it sells the item, that it's in stock and that you can afford it. At the end you get a receipt.

## How this one is made

This game is how I'm learning Python. Every lesson brings in **one new idea**, which Claude teaches with a small example that isn't about shops. Then **I write every line** of the game myself. When I'm stuck, the AI asks me a question that points at the bug and never writes the fix. The game grows lesson by lesson, in freeCodeCamp's order: dictionaries, functions, error handling, classes, then saving to a file.

## Run it

```bash
python3 shop.py
```

## A real run

Bought apple, apple, bread, then tried pizza and milk, then typed `done`. The repeated menus are left out after the first:

```text
🏪 Welcome to the shop! You have Rs 100.
apple - Rs 20 (5 left)
bread - Rs 50 (3 left)
milk - Rs 120 (2 left)
juice - Rs 30 (4 left)
What do you want to buy? You picked apple
✅ Bought apple. Money left: Rs 80
What do you want to buy? You picked apple
✅ Bought apple. Money left: Rs 60
What do you want to buy? You picked bread
✅ Bought bread. Money left: Rs 10
What do you want to buy? 🤷 We don't sell that.
What do you want to buy? You picked milk
❌ Not enough money for milk.
What do you want to buy? Money left: Rs 10
apple × 2
bread × 1
```

## Ideas inside (lesson 1)

- **Dictionaries:** `prices` and `stock` store pairs, an item and its number, and look values up by key.
- **`in` before a lookup:** check that a key exists before using it, or the program crashes with a `KeyError`.
- **`.items()`:** loop over each key and its value together to print the menu.
- **Changing a value:** `stock[item] = stock[item] - 1` takes one off the shelf.
- **Counting with a dictionary:** `bag` starts empty; a new item gets 1, an item already in it goes up by 1.
- **Nested `if`s in the right order:** sells it? → in stock? → enough money? Only then does anything change.
- **`while True` and `break`:** keep shopping until `done`.
- **`.lower().strip()`:** `  APPLE ` still means `apple`.

## Bugs I fixed on the way

- I wrote `price[question]` instead of `prices[question]`. `price` was the loop's leftover number, not the dictionary.
- My money check sat outside the "shop sells it" `if`, so typing `pizza` crashed with a `KeyError`. Indenting it inside fixed it.
- `bag.update({"question": 1})` stored the word "question", not the item. A variable's name goes in **without** quotes.
- `bag = bag[question] + 1` replaced the whole dictionary with a number. It had to be `bag[question] = ...`.
