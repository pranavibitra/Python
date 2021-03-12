def count_change(money, coins):
    combinations = [1] + [0] * money
    for denominations in coins:
        for i in range(denominations, money + 1):
            combinations[i] += combinations[i - denominations]
    return combinations[money]

print(count_change(4, [1,2])) # => 3
print(count_change(10, [5,2,3])) # => 4
print(count_change(11, [5,7])) # => 0