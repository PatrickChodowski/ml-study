import unittest
from CosineSimilarity import CosineSimilarity
from numpy import dot
from numpy.linalg import norm


class CosineSimilarityTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CosineSimilarityTests, self).__init__(*args, **kwargs)

    def test_result_ab_1(self):
        A = (0, 1, 10)
        B = (90, 0, 10)
        cs = CosineSimilarity(A, B)
        assert dot(A, B)/(norm(A)*norm(B)) == cs.calculate()

    def test_result_ab_2(self):
        A = (0, 1, 10, 0, 5, 10, 20, 99)
        B = (90, 0, 10, 1, 1, 1, 1, 1)
        cs = CosineSimilarity(A, B)
        assert dot(A, B)/(norm(A)*norm(B)) == cs.calculate()

    def test_result_ab_3(self):
        A = (1, 2)
        B = (6, 0)
        cs = CosineSimilarity(A, B)
        assert dot(A, B)/(norm(A)*norm(B)) == cs.calculate()
