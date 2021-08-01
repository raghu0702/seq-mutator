import random
target_seq = input()   #input from user(amino acid seq.)

mutations = 'ARNDCQEGHILKMFPSTWYV'
a,b = list(map(int, input("enter boundary:"))) #obtain a boundary as start AA, stop AA
test_seq = target_seq[a:b]
#mutations start
for i in range(a,b):
    test_seq[i] = random.choice(mutations)

target_seq[a:b] = test_seq
print("Mutated")
print(f"new sequence={target_seq}")
