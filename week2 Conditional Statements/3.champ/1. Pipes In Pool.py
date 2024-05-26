V = int(input())
P1 = int(input())
P2 = int(input())
N = float(input())

filled_up = N * (P1 + P2)
filled_up_p = filled_up / V * 100
P1_p = P1 * N / filled_up * 100
P2_p = P2 * N / filled_up * 100
if V >= filled_up:
    print(f"The pool is {filled_up_p:.2f}% full. Pipe 1: {P1_p:.2f}%. Pipe 2: {P2_p:.2f}%.")
else:
    print(f"For {N} hours the pool overflows with {filled_up - V:.2f} liters.")
