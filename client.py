"""Pauli Algebra and Commutator Engine.
100% Python Standard Library.
"""

class PauliAlgebra:
    """Pauli group algebra matrices and commutation relations."""
    I = [[complex(1, 0), complex(0, 0)], [complex(0, 0), complex(1, 0)]]
    X = [[complex(0, 0), complex(1, 0)], [complex(1, 0), complex(0, 0)]]
    Y = [[complex(0, 0), complex(0, -1)], [complex(0, 1), complex(0, 0)]]
    Z = [[complex(1, 0), complex(0, 0)], [complex(0, 0), complex(-1, 0)]]

    @staticmethod
    def matmul(m1, m2):
        res = [[complex(0, 0), complex(0, 0)], [complex(0, 0), complex(0, 0)]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    res[i][j] += m1[i][k] * m2[k][j]
        return res

    @classmethod
    def commutator(cls, m1, m2):
        ab = cls.matmul(m1, m2)
        ba = cls.matmul(m2, m1)
        return [[ab[i][j] - ba[i][j] for j in range(2)] for i in range(2)]
