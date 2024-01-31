import numpy as np

A = np.loadtxt('input', usecols=range(0, 15))

q = 0.15

G = np.zeros((15, 15), dtype='double')

nj = np.zeros(15)

for i in range(15):
    for j in range(15):
        nj[i] += A[i, j]


for i in range(15):
    for j in range(15):
        if j != 9:
            G[i, j] = q / G.shape[0] + (A[j, i] * (1 - q)) / nj[j]
        else:
            G[9, 0:G.shape[1]] = 0

sum = np.zeros(15)

for j in range(15):
    for i in range(15):
        sum[j] += G[i, j]


b = np.random.rand(15)

eigvalues = []

i = 0

for i in range(10000):
    b = np.matmul(G, b)

    div = b[0]
    eigvalues.append(div)
    sum = 0
    for j in range(15):
        sum += abs(b[j])
    b = (1 / b[0]) * b
    if i >= 1:
        if abs(eigvalues[i] - eigvalues[i - 1]) < 0.5 * 10 ** -16:
            break

    i += 1

print(b/sum)






