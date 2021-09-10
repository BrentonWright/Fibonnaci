# Fibonacci Sequence - Brenton Wright 2021

fn = 10     # Define how many Fibonnaci numbers(fn) in the sequence.
seq = []

while len(seq) < fn:
    if len(seq) == 0 or len(seq) == 1:
        seq.append(len(seq))
    else:
        seq.append(seq[len(seq) - 1] + seq[len(seq) - 2])

print(seq)
