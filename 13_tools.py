import itertools 


def to_bin_ip(n):
    n = n.split(".")

    for i in range(4):
        n[i] = bin(int(n[i]))[2:].rjust(8, "0")
    return ".".join(n)


print(to_bin_ip("117.191.37.176"))
print(to_bin_ip("117.191.37.160"))

can_to_change = 11
base_was_symbols = 7
count = 0
s = itertools.product([0,1],repeat = can_to_change)
for i in s:
    if (base_was_symbols + sum(i)) % 2 !=0:
        count += 1
print(count)
print(int("11100000", 2))
