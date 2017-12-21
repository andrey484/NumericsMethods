import numpy as np


class Utils(object):
    matrix_order = 0
    vectors = []
    input_array = [[]]
    coef_polinom = []

    @staticmethod
    def is_digit(event):
        if chr(event.GetKeyCode()) in "-1234567890'\b'":
            event.Skip()
            return
        else:
            return False

    @staticmethod
    def trace(arr):
        trace = 1
        for i in range(Utils.matrix_order):
            trace *= arr[i][i]
        return trace

    @staticmethod
    def krylov(arr):
        arr = np.array(arr)
        y = np.copy(np.zeros((4,4)))
        # y.append(np.copy(np.identity(Utils.matrix_order)[0, :]))
        y[0] = (np.copy(np.identity(4)[0, :]))
        for k in range(1, 4):
            y[k] = arr.dot(y[k - 1])
        y[0] = arr.dot(y[3])
        y = np.copy(y.transpose())
        answers = np.copy(y[:, 0])

    @staticmethod
    def fadeev(arr):
        Utils.input_array = np.copy(arr)
        res = []
        q = np.zeros(Utils.matrix_order)
        B = np.zeros((Utils.matrix_order, Utils.matrix_order))
        B1 = np.zeros((Utils.matrix_order, Utils.matrix_order))
        vector_znach_matr = []
        vector_znach_matr.append(np.copy(np.identity(Utils.matrix_order)[0, :]))
        A = np.copy(arr)
        A1 = np.copy(arr)
        q[0] = np.trace(A)
        for i in range(Utils.matrix_order):
            for j in range(Utils.matrix_order):
                if i != j:
                    B[i][j] = A1[i][j]
                else:
                    B[i][j] = A1[i][j] + (-1 * q[0])
                B1[i][j] = A[i][j]
        vector_znach_matr.append(np.copy(B[0, :]))

        for i in range(1, Utils.matrix_order):
            for i1 in range(Utils.matrix_order):
                for j1 in range(Utils.matrix_order):
                    A1[i1][j1] = 0
            for i1 in range(Utils.matrix_order):
                for j1 in range(Utils.matrix_order):
                    for k1 in range(Utils.matrix_order):
                        A1[i1][j1] += A[i1][k1] * B[k1][j1]
            q[i] = np.trace(A1) / (i + 1)

            for i1 in range(Utils.matrix_order):
                for j1 in range(Utils.matrix_order):
                    if i1 != j1:
                        B[i1][j1] = A1[i1][j1]
                    else:
                        B[i1][j1] = A1[i1][j1] - 1 * q[i]
            if i < Utils.matrix_order - 1:
                vector_znach_matr.append(np.copy(B[0, :]))
            if i == Utils.matrix_order - 2:
                for i1 in range(Utils.matrix_order):
                    for j1 in range(Utils.matrix_order):
                        B1[i1][j1] = B[i1][j1]

        for i in range(Utils.matrix_order):
            for j in range(Utils.matrix_order):
                B1[i][j] *= (1 / q[Utils.matrix_order - 1])
        lambda_s = Utils.root(q)
        res.append(q)
        res.append(Utils.root(q))
        # own_vectors = Utils.own_vector_fadeev(lambda_s, vector_znach_matr)
        # res.append(Utils.norm_vector(own_vectors))
        # res.append(B1)
        return res

    @staticmethod
    def norm_vector(own_vectors):
        own_vectors.pop(0)
        for i in range(0, Utils.matrix_order):
            len_vector = 0
            for j in range(0, Utils.matrix_order):
                len_vector += own_vectors[i][j] ** 2
            for k in range(0, Utils.matrix_order):
                own_vectors[i][k] = own_vectors[i][k] / np.sqrt(len_vector)
        return own_vectors

    @staticmethod
    def own_vector_fadeev(lambdas, bk_matrix):
        own_vectors = [[]]
        for i in range(Utils.matrix_order):
            res = np.zeros((Utils.matrix_order, Utils.matrix_order))
            res[0] = np.copy(bk_matrix)[0, :]
            for k in range(1, Utils.matrix_order):
                res[k] = (lambdas[i] * res[k - 1]) + bk_matrix[k]
                if k == Utils.matrix_order - 1:
                    own_vectors.append(np.copy(res[Utils.matrix_order - 1]))
        return own_vectors

    @staticmethod
    def first_matrix_norm():
        norms = np.zeros(Utils.matrix_order)
        for i in range(Utils.matrix_order):
            for j in range(Utils.matrix_order):
                norms[i] += abs(Utils.input_array[i][j])
        max_norm = abs(norms[0])
        for i in range(Utils.matrix_order):
            if max_norm < norms[i]:
                max_norm = norms[i]
        return max_norm

    @staticmethod
    def root(coef):
        roots = np.zeros(Utils.matrix_order)
        border = Utils.first_matrix_norm()
        count = 0
        for i in np.arange(-border, border, 0.001):
            if Utils.sign(Utils.polinom(coef, -border)) != Utils.sign(Utils.polinom(coef, i)):
                roots[count] = Utils.half_div(-border, i, coef)
                coef = Utils.gorn(coef, -roots[count])
                count += 1
                i = -border
            if len(coef) == 2:
                kv = Utils.kvadr(coef)
                roots[count] = kv[0]
                roots[count + 1] = kv[1]
                break
        return roots

    @staticmethod
    def polinom(coefs, border):
        x1 = border
        res = -coefs[len(coefs) - 1]
        for i in range(len(coefs) - 2, -1, -1):
            res -= coefs[i] * x1
            x1 = x1 * border
        res += x1
        return res

    @staticmethod
    def sign(val):
        if val < 0:
            return -1
        elif val == 0:
            return 0
        elif val > 0:
            return 1

    @staticmethod
    def half_div(a, b, k):
        c = (a + b) / 2
        while abs(a - b) > 0.0001:
            if Utils.sign(Utils.polinom(k, c)) == Utils.sign(Utils.polinom(k, a)):
                a = c
            else:
                b = c
            c = (a + b) / 2
        return a

    @staticmethod
    def gorn(p, n_root):
        res = np.zeros(len(p))
        res[0] = 1
        for i in range(1, len(p)):
            res[i] = -n_root * res[i - 1] - p[i - 1]
        n_res = np.zeros(len(p) - 1)
        for i in range(1, len(p)):
            n_res[i - 1] = -res[i]
        return n_res

    @staticmethod
    def kvadr(p):
        p[0] *= -1.0
        p[1] *= -1.0
        D = p[0] * p[0] - 4 * p[1]
        res = np.zeros(2)
        res[0] = ((-1.0) * p[0] + np.sqrt(D)) / 2.0
        res[1] = ((-1.0) * p[0] - np.sqrt(D)) / 2.0
        return res


if __name__ == "__main__":
    arr = [[2.2, 1, 0.5, 2],
           [1, 1.3, 2, 1],
           [0.5, 2, 0.5, 1.6],
           [2, 1, 1.6, 2]]
    print(Utils.krylov(arr))
