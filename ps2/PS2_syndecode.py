# 6.02 PS: Syndrome decoding of a linear block code
from numpy import *
import PS2_tests

# Replace each entry of a matrix A with its modulo 2 value 
# and return that matrix.  All your base are belong to 2. :-)
def mod2(A):
    for i in range(2):
        A[A%2==i] = i
    return A

# True iff two matrices are identical element-by-element.
def equal(a, b):
    if (a == b).all():
        return True
    return False

# Assume that the code has Hamming distance 3, 
# i.e., correct all patterns of 1-bit errors in the n-bit codeword.
# n and k are positive integers; n > k and G is a numpy matrix for the code.
# Return a numpy array of length k, each entry either 0 or 1, 
# corresponding to the k decoded *message* bits.  We return codeword[:k] 
# in the template; you can preserve that, or change it as you wish.
def syndrome_decode(codeword, n, k, G):
    # construct the parity check matrix (H)
    H = concatenate((G[:, k:].transpose(), identity(n-k, int)), axis=1)
    
    # compute syndromes
    syndromes = []
    for i in range(k):
        syndromes.append(H[:, i]) # append the ith column of H
    
    c = mod2(H * matrix(codeword).transpose())
    if not equal(c, zeros((n-k, 1), int)):
        for i in range(k):
            if equal(c, syndromes[i]):
                codeword[i] = int(not codeword[i]) # flip bit
                break
    
    return codeword[:k]

if __name__ == '__main__':
    # (7,4,3) Hamming code
    G1 = matrix('1 0 0 0 1 1 0; 0 1 0 0 1 0 1; 0 0 1 0 0 1 1; 0 0 0 1 1 1 1', 
                dtype=int)
    PS2_tests.test_linear_sec(syndrome_decode, 7, 4, G1)

    # (8,4,3) rectangular parity code
    G2 = matrix('1 0 0 0 1 0 1 0; 0 1 0 0 1 0 0 1; 0 0 1 0 0 1 1 0; 0 0 0 1 0 1 0 1', dtype=int)
    PS2_tests.test_linear_sec(syndrome_decode, 8, 4, G2)

     # (6,3,3) pairwise parity code
    G3 = matrix('1 0 0 1 1 0; 0 1 0 0 1 1; 0 0 1 1 0 1', dtype=int)
    PS2_tests.test_linear_sec(syndrome_decode, 6, 3, G3)
    
    # (15,11,3) Hamming code
    G4 = matrix('1 0 0 0 0 0 0 0 0 0 0 0 1 1 1; 0 1 0 0 0 0 0 0 0 0 0 1 0 1 1; 0 0 1 0 0 0 0 0 0 0 0 1 1 0 1; 0 0 0 1 0 0 0 0 0 0 0 1 1 1 0; 0 0 0 0 1 0 0 0 0 0 0 1 1 1 1; 0 0 0 0 0 1 0 0 0 0 0 1 1 0 0; 0 0 0 0 0 0 1 0 0 0 0 1 0 1 0; 0 0 0 0 0 0 0 1 0 0 0 1 0 0 1; 0 0 0 0 0 0 0 0 1 0 0 0 1 1 0; 0 0 0 0 0 0 0 0 0 1 0 0 1 0 1; 0 0 0 0 0 0 0 0 0 0 1 0 0 1 1')
    PS2_tests.test_linear_sec(syndrome_decode, 15, 11, G4)
