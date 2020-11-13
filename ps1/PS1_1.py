# template file for 6.02 PS1, Python Task 1
import PS1_tests

class Node:
    
    def __init__(self, value, left_child = None, right_child = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        
    def is_leaf(self):
        return self.value is not None

def get_codes(rootNode, codes, prefix = []):
    if rootNode.is_leaf():
        codes[rootNode.value] = prefix
        return codes
    get_codes(rootNode.left_child, codes, prefix + [0])
    get_codes(rootNode.right_child, codes, prefix + [1])
    return codes

# arguments:
#   plist -- sequence of (probability,object) tuples
# return:
#   a dictionary mapping object -> binary encoding
def huffman(pList):
    """
    Example:
    plist: ((0.50,'A'),(0.25,'B'),(0.125,'C'),(0.125,'D'))
    returns: {'A': [0], 'B': [1, 0], 'C': [1, 1, 0], 'D': [1, 1, 1]} 
    """
    nodeList = [(element[0], Node(element[1])) for element in pList]
    sortedList = sorted(nodeList)
    while len(sortedList) > 1:
        # combine the two tuples with the smallest probabilities
        sortedList[1] = (sortedList[0][0] + sortedList[1][0], Node(None, sortedList[0][1], sortedList[1][1]))
        # delete first element
        del sortedList[0]
        sortedList.sort(key=lambda x: x[0])
    rootNode = sortedList[0][1]
    return get_codes(rootNode, {})

if __name__ == '__main__':
    # test case 1: four symbols with equal probability
    PS1_tests.test_huffman(huffman,
                           # symbol probabilities
                           ((0.25,'A'),(0.25,'B'),(0.25,'C'),
                            (0.25,'D')),
                           # expected encoding lengths
                           ((2,'A'),(2,'B'),(2,'C'),(2,'D')))

    # test case 2: example from section 22.3 in notes
    PS1_tests.test_huffman(huffman,
                           # symbol probabilities
                           ((0.34,'A'),(0.5,'B'),(0.08,'C'),
                            (0.08,'D')),
                           # expected encoding lengths
                           ((2,'A'),(1,'B'),(3,'C'),(3,'D')))

    # test case 3: example from Exercise 5 in notes
    PS1_tests.test_huffman(huffman,
                           # symbol probabilities
                           ((0.07,'I'),(0.23,'II'),(0.07,'III'),
                            (0.38,'VI'),(0.13,'X'),(0.12,'XVI')),
                           # expected encoding lengths
                           ((4,'I'),(3,'II'),(4,'III'),
                            (1,'VI'),(3,'X'),(3,'XVI')))

    # test case 4: 3 flips of unfair coin
    phead = 0.9
    plist = []
    for flip1 in ('H','T'):
        p1 = phead if flip1 == 'H' else 1-phead
        for flip2 in ('H','T'):
            p2 = phead if flip2 == 'H' else 1-phead
            for flip3 in ('H','T'):
                p3 = phead if flip3 == 'H' else 1-phead
                plist.append((p1*p2*p3,flip1+flip2+flip3))
    expected_sizes = ((1,'HHH'),(3,'HTH'),(5,'TTT'))
    PS1_tests.test_huffman(huffman,plist,expected_sizes)
