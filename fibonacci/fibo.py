def fibo1(n):
    if n <= 1:
        return 1
    return fibo(n-1) + fibo(n - 2)

def fibo2(n):
    if n < 0:
        raise ValueError("Input value n can't be less than 0.")
    if n in [0, 1]:
        return 1

    prev = 1
    prev_prev = 0
    for _ in range(n):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
    return current

def fibo2_sequence(n):
    if n < 0:
        raise ValueError("Input value n can't be less than 0.")
    if n in [0, 1]:
        return 1

    prev_prev = 0
    prev = 1
    print prev,
    for _ in range(n):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
        print current,

    return current


if __name__ == "__main__":
    # print fibo1(8)
    # print fibo2(8)
    fibo2_sequence(8)

