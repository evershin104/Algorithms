openner = open("lcs.in", "r")
file = openner.readlines()
# Reads length of 1st and 2nd seq
n = int(file[0])
m = int(file[2])
# If length of seq = 0 ==> length of subseq = 0
if (m == 0) or (n == 0):
    f = open("lcs.out", "w")
    f.write("0")
    f.close()
    openner.close()
else:
    # Fills seqs of numbers
    a = file[1].split()
    b = file[3].split()
    openner.close()

    # Fills matrix with zeros
    F = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    # print(F[n][m])
    f = open("lcs.out", "w")
    f.write(str(F[n][m]))
    f.close()
