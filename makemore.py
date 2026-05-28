import torch 
words = open('names.txt').read().splitlines()
n = torch.zeros(27, 27, dtype=torch.int32)
chars = sorted(list(set(''.join(words))))
stoi = {s:i+1 for i,s in enumerate(chars)}
stoi['.'] = 0


for w in words:
    chs = ['.']+ list(w) + ['.']
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2] 
        n[ix1, ix2] += 1

itos = {i:s for s,i in stoi.items()}

g = torch.Generator().manual_seed(2147483647)
for i in range (20):
    out = []
    ix = 0
    while True:
        p = n[ix].float()
        p = p / p.sum()
        ix = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()
        out.append(itos[ix])
        if ix == 0:
            break
    print(''.join(out))