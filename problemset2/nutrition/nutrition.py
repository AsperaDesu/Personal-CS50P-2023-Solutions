fruits = [
    {"name": "apple", "value": 130},
    {"name": "avocado", "value": 50},
    {"name": "banana", "value": 110},
    {"name": "cantaloupe", "value": 50},
    {"name": "grapefruit", "value": 60},
    {"name": "grapes", "value": 90},
    {"name": "honeydewmelon", "value": 50},
    {"name": "kiwifruit", "value": 90},
    {"name": "lemon", "value": 15},
    {"name": "lime", "value": 20},
    {"name": "nectarine", "value": 60},
    {"name": "orange", "value": 80},
    {"name": "peach", "value": 60},
    {"name": "pear", "value": 100},
    {"name": "pineapple", "value": 70},
    {"name": "plums", "value": 70},
    {"name": "strawberries", "value": 50},
    {"name": "sweet cherries", "value": 100},
    {"name": "tangerine", "value": 50},
    {"name": "watermelon", "value": 80}
]

item = input("Item: ")

for fruit in fruits:
    if item.lower() == fruit["name"]:
        print("Calories:", fruit["value"])
