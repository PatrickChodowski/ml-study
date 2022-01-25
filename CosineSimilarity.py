
from typing import Tuple
from math import sqrt, acos, degrees


class CosineSimilarity:
    def __init__(self, a: Tuple[float], b: Tuple[float]):
        """
        Cosine Similarity object
        Given two vectors of attributes, A and B, the cosine similarity, cos(θ),
        is represented using a dot product and magnitude as
        similarity(A, B)  = cos(alpha) = (A*B)/(|A|x|B|)

        Can have values from -1 (exactly different) to 1 (identical vectors)
        :param a: Tuple A of floats
        :param b: Tuple B of floats
        """
        self.a = a
        self.b = b

        self.dp = None
        self.m_a = None
        self.m_b = None
        self.cos_alpha = None
        self.alpha = None
        self.rad_alpha = None

    def _validate(self):
        """
        Validates if provided vectors will work
        """
        if isinstance(self.a, tuple) & isinstance(self.a, tuple):
            pass
        else:
            raise AttributeError(f"A is of type {type(self.a)} B is of type {type(self.b)}. Both should be tuples")

        if self.a.__len__() == self.b.__len__():
            pass
        else:
            raise ValueError(f"Length of a {self.a.__len__()} has to be equal to length of b {self.b.__len__()}")

        if (set(self.a) == {0}) | (set(self.b) == {0}):
            raise ValueError(f"Vectors cant be only 0s vectors")

    def calculate(self) -> float:
        """
        Calculates similarity between two vectors. Called on initialization
        :return: Similarity
        """
        self._validate()
        self.dp = self._get_dot_product()
        self.m_a = self._get_vector_norm(self.a)
        self.m_b = self._get_vector_norm(self.b)

        self.cos_alpha = self.dp/(self.m_a*self.m_b)
        self.rad_alpha = acos(self.cos_alpha)
        self.alpha = degrees(self.rad_alpha)

        print(f"Cosine similarity between vectors is {self.cos_alpha}")
        print(f"(Radians) Angle between vectors is {self.rad_alpha}")
        print(f"(Degrees) Angle between vectors is {self.alpha}")
        return self.cos_alpha

    def _get_dot_product(self) -> float:
        """
        Calculate dot product
        Formula dp = a1*b1 + a2*b2 + an*bn
        :return: Dot product value
        """
        dp = 0.0
        for a, b in zip(self.a, self.b):
            dp += a*b
        print(f"Dot product of provided vectors is {dp}")
        return dp

    @staticmethod
    def _get_vector_norm(v: Tuple[float]) -> float:
        """
        Calculates vectors magnitude. Magnitude is a length of the vector
        Formula: sqrt(a1^2 +  a2^2 + an^2)
        :param v: Set of floats to calculate magnitude for
        :return: Magnitude of the vector
        """
        t = 0.0
        for f in v:
            t += f**2
        m = sqrt(t)
        print(f"Norm of the vector is {m}")
        return m
