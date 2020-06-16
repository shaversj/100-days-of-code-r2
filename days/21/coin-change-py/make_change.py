def change_making(cents: int) -> int:
    coins = [100, 50, 25, 10, 5, 1]
    num_coins = 0
    for coin in coins:
        num_coins += cents // coin
        cents %= coin

    return num_coins


def return_change(change_needed: float):
    currency = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, .50, .25, .10, .05, .01]
    names_of_currency = ['ONE HUNDRED', 'FIFTY', 'TWENTY', 'TEN', 'FIVE', 'TWO', 'ONE', 'HALF DOLLAR', 'QUARTER', 'DIME', 'NICKEL', 'PENNY']
    accumulated_change = 0.00
    for denomination, name in zip(currency, names_of_currency):
        num_of_coins = change_needed // denomination
        accumulated_change += num_of_coins * denomination
        change_needed -= num_of_coins * denomination
        if num_of_coins >= 1:
            print(f"{int(num_of_coins)}: {name}")
            print(accumulated_change)
        if accumulated_change == change_needed:
            break


print(return_change(528.00))