def gen_fibonacci_num():
    num_1 = 0
    num_2 = 1
    count = 1
    while True:
        if count == 1:
            count += 1
            yield 0
        elif count == 2:
            count += 1
            yield 1
        else:
            num_1, num_2 = num_2, num_1 + num_2
            yield num_2


if __name__ == '__main__':
    fibo_gen = gen_fibonacci_num()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
