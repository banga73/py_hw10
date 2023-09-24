import random
data_r = ['robot']
data_h = ['human']
for i in range(10):
    data_r.append(random.randint(0,1))
    if data_r[i] == 0:
        data_h.append(1)
    else:
        data_h.append(0)
one_hot = [list(a) for a in zip(data_r, data_h)]
print(one_hot)