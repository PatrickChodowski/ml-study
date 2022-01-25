# cosine distance -> recommendation engine
from CosineSimilarity import CosineSimilarity
A = (0, 1, 10)
B = (90, 0, 10)
C = (90, 0, 1)
D = (90, 0, 0)

cs = CosineSimilarity(A,D)
cs.calculate()