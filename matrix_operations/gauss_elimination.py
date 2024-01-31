import numpy as np


def change_line(col, index, A, P):
    maxel = abs(col[0])
    change = 0

    for i in range(1, len(col)):
        if maxel < abs(col[i]):
            maxel = abs(col[i])
            change = i

    if change != 0:
        temp = A[change, index:].copy()  # Αντιγραφή γραμμής σε temp μεταβλητή

        A[change, index:] = A[index, index:].copy()
        # Αντιμετάθεση γραμμών, χρησιμοποιώ την .copy() για να κάνω deep copy
        A[index, index:] = temp

        temp2 = P[change, index:].copy()

        P[change, index:] = P[index, index:].copy()

        P[index, index:] = temp2


def eliminate_col(A, index, L):
    for i in range(index + 1, A.shape[0]):
        L[i, index] = A[i, index] / A[index, index]  # ΟΡΙΣΜΟΣ ΣΤΟΙΧΕΊΩΝ ΤΟΥ ΠΙΝΑΚΑ L
        A[i, index:] -= A[i, index] / A[index, index] * A[index, index:]  # ΔΙΑΓΡΑΦΗ ΣΤΟΙΧΕΙΩΝ


def gauss_elimination(n):
    A = np.random.rand(n, n)

    b = np.random.rand(n)

    print(A)
    print("----------------")

    print(b)
    print("----------------")

    P = np.eye(n)

    L = P.copy()

    U = A.copy()

    for j in range(n):
        col = A[j:, j]
        change_line(col, j, A, P)
        eliminate_col(A, j, L)

    print(A)
    print("-------------")
    print(P)
    print("-------------")
    print(L)

    temp = U.copy()  # ΑΛΛΑΓΗ ΤΩΝ ΠΙΝΑΚΩΝ Α, U
    U = A
    A = temp

    y = forward_subtitution(L, b)

    x = backward_subtitution(U, y)

    print("-----------------")

    print(x)


def forward_subtitution(L, b):
    n = len(b)  # παίρνω μέγεθος του συστήματος
    x = np.empty(n)  # παίρνω μέγεθος του συστήματος
    for i in range(n):
        if L[i][i] == 0:  # Αν η διαγώνιος ειναι 0 τότε
            x[i] = 0
            continue
        # Υπολογισμος της τιμής της i-οστης μεταβλητής:
        timh = b[i]
        for j in range(i):
            timh -= L[i][j] * x[j]
        # Διαιρώ με τον συντελεστή απο τον πίνακα L
        timh /= L[i][i]
        # αποθηκέυω την τιμή στο διάνυσμα x
        x[i] = timh
    return x


# Δέχεται τον U και τον y και επιστρτρέφει το διάνυσμα x, σχεδόν ίδια με forward, μονο που αντι να πάει απο πάνω -> κάτω
# πάει απο κάτω -> πανω
def backward_subtitution(U, b):
    n = len(b)
    x = np.empty(n)
    for i in range(n - 1, -1, -1):
        if U[i][i] == 0:
            x[i] = 0
            continue
        timh = b[i]
        for j in range(i + 1, n, 1):
            timh -= U[i][j] * x[j]
        timh /= U[i][i]
        x[i] = timh
    return x
