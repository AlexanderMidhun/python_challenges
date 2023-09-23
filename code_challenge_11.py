#method 1 (fibonacci using recursive)
def fibonacci_re(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci_re(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

n = 13
fibonacci_seq = fibonacci_re(n)
print(fibonacci_seq)
print('___________________________________________________________')
#method 2
def fibonacci_sequence(n):
    fib_seq = [0, 1]
    while True:
        next_num = fib_seq[-1] + fib_seq[-2]
        if next_num > n:
            break
        fib_seq.append(next_num)
    return fib_seq

n = 144
fib_seq = fibonacci_sequence(n)
print(fib_seq)

