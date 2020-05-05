def gauss_elimination(A, B):
    n = len(A)

    if len(A) != len(A[0]):
        return None

    for i in range(n):
        if A[i][i] == 0:
            return None

    for row in range(n - 1):
        for i in range(row + 1, n):
            factor = A[i][row] / A[row][row]
            for j in range(row, n):
                A[i][j] -= factor * A[row][j]
            B[i] -= factor * B[row]

    result = [0] * n
    result[n - 1] = B[n - 1] / A[n - 1][n - 1]
    for row in range(n - 2, -1, -1):
        sum = B[row]
        for j in range(row + 1, n):
            sum -= A[row][j] * result[j]
        result[row] = sum / A[row][row]
    return result


def gauss_elimination_pivoting(A, B):
    n = len(A)

    if len(A) != len(A[0]):
        return None

    M = A
    i = 0

    for x in M:
        x.append(B[i])
        i += 1

    for row in range(n):
        for i in range(row, n):
            if abs(M[i][row]) > abs(M[row][row]):
                M[row], M[i] = M[i], M[row]
            else:
                pass

        for i in range(row + 1, n):
            factor = M[i][row] / M[row][row]
            for j in range(row, n + 1):
                M[i][j] -= factor * M[row][j]

    x = [0] * n

    x[n - 1] = M[n - 1][n] / M[n - 1][n - 1]
    for i in range(n-1, -1, -1):
        z = 0
        for j in range(i + 1, n):
            z += float(M[i][j]) * x[j]
        x[i] = float(M[i][n] - z)/M[i][i]
    return x


if __name__ == '__main__':
    A = [[0.00000000000000012, 4200, 34],
         [0.5, 69, 2320],
         [1, 17, 7]]
    B = [7, 3.901, 6]
    x = gauss_elimination(A, B)
    print('Gauss result is x = %s' % x)

    A = [[0.00000000000000012, 4200, 34],
         [0.5, 69, 2320],
         [1, 17, 7]]
    B = [7, 3.901, 6]
    x = gauss_elimination_pivoting(A, B)
    print('Gauss result is x = %s' % x)