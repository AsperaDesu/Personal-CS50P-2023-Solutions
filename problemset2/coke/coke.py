due = 50
coin = 0
sum = 0

while sum < 50:
    print("Amount Due: ", due)
    coin = int(input("Insert Coin: "))
    if coin not in [25,10,5]:
        continue
    sum = sum + coin
    due = due - coin

print(f"Change Owed: {abs(due)}")