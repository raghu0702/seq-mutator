import random
target_seq = input()

mutations = 'ARNDCQEGHILKMFPSTWYV'
a,b = list(map(int, input("enter boundary:")))
test_seq = target_seq[a:b]
for i in range(a,b):
    test_seq[i] = random.choice(mutations)

target_seq[a:b] = test_seq
print("Mutated")