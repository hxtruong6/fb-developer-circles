bills = [500, 200, 100, 50, 20, 10, 5, 2, 1]


def exchange(money, sorted_bills):
    changes = [0] * len(sorted_bills)
    due = money
    for i, bill in enumerate(sorted_bills):
        if (due > 0):
            changes[i] = due // bill
            due -= changes[i] * bill
    return changes


print(exchange(2300, bills))
print(exchange(54322, bills))
