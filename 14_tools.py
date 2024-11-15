def to_ss(n, m):
    string = ''
    while n > 0:
        string += str(n % m)
        n //= m
    return string[::-1]

def num_to_appearance(n):
    out = {}
    for i in str(n):
        if out.get(i):
            out[i] += 1
            continue
        out[i] = 1
    return dict(sorted(out.items(), key=lambda x: x[0]))

def sum_of_num(n):
    out = 0
    for i in n:
        out += int(i)
    return out

def find_n_base_with_sum_of_num(m, r): #ищет основание m, при котором выражение == r
    for i in range(2, 100):
        n = i
        t = eval(m) 
        if r == sum_of_num(to_ss(t, n)):
            return i
    return False

def x_for_problem_equal(): #ищет мин х для решения уравнения, возвращает r2 в десятичной сс
    for x in range(0, 100):
        r1 = int(f"{x}1418", 13) + int(f"1{x}037", 14)
        r2 = int(f"2{x}209", 19)
        if r1 == r2:
            return r2
    return False

def x_for_problem_by_multip(): #ищет макс х для решения уравнения по кратности, возврат частное от деления
    for x in alphabhet_of_ss(15)[::-1]:
        r1 = int(f"67845{x}65", 15) + int(f"1{x}23456", 15)

        if r1 % 14 == 0:
            return r1 / 14
    return False   

def alphabhet_of_ss(n):
    import string
    alphas = list(string.ascii_uppercase)
    if n <= 10:
        return [str(i) for i in range(0, n)]
    return [str(i) for i in range(0, 10)] + alphas[:n - 10]

def x_for_problem_num_of_els(m, n, figure, times): #ищет min х для того, чтобы в выражение в n CC было X цифр c
    for i in range(1, 3000):
        x = i
        t = to_ss(eval(m), n)
        if t.count(figure) == times:
            return i
    return False

#t = to_ss((3*16**int("46", 8) + 5*4**int("40", 16) - 8**(int("47", 8) - int("1B", 16)) - 2**64 + 15   ), 16)
t = to_ss( ( 4**1103 + 3*4**1444 - 2*4**144 + 66    ), 4)
g = num_to_appearance(t)



#print(x_for_problem_num_of_els("4**2015 + 2**x - 2**2015 + 15", 2, "1", 500))

for i in range(1, 50000000):
    t = to_ss( ( 27**7 -3**11 + 36 - i   ), 3)
    print(sum_of_num(t))
    if sum_of_num(t) == 22:
        print(i)
        break