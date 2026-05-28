import torch as t
words = open('names.txt').read().splitlines()
n = t.zeros(27, 27, dtype=t.int32)
chars = sorted(list(set(''.join(words))))
stoi = {s:i+1 for i,s in enumerate(chars)}
stoi['.'] = 0

print(stoi)
for w in words:
    chs = ['.']+ list(w) + ['.']
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2] 
        n[ix1, ix2] += 1
print(n)
itos = {i:s for s,i in stoi.items()}