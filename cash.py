def get_non_negative_float():
    while True:
        try:
            change = float(input("Change owed: "))
            if change >= 0:
                return change
            else:
                print("Please enter a non-negative value.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    coins_count = 0
    coins = [25, 10, 5, 1]
    change = get_non_negative_float() * 100  # Convertendo para centavos

    for coin in coins:
        coins_count += change // coin
        change %= coin

    print(int(coins_count))

if __name__ == "__main__":
    main()
