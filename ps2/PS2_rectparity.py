# template for 6.02 rectangular parity decoding using error triangulation
import PS2_tests
import numpy

def rect_parity(codeword,nrows,ncols):
    # construct rectangle
    rectangle = []
    for row in range(nrows):
        rectangle.append(codeword[row*ncols:row*ncols+ncols])
    # add row parity bits
    row = 0
    for row_parity_bit in codeword[nrows*ncols:nrows*ncols+nrows]:
        rectangle[row].append(row_parity_bit)
        row += 1
    # add column parity bits
    rectangle.append(codeword[nrows*ncols+nrows:])
    
    # calculate parity
    rows_with_error = []
    cols_with_error = []
    # row parity
    for row in range(nrows):
        if not PS2_tests.even_parity(rectangle[row][:ncols+1]):
            rows_with_error.append(row)
    # column parity
    for col in range(ncols):
        if not PS2_tests.even_parity([rectangle[row][col] for row in range(nrows+1)]):
            cols_with_error.append(col)
    
    # correct errors
    if len(rows_with_error) == 1 and len(cols_with_error) == 1:
        row = rows_with_error[0]
        col = cols_with_error[0]
        rectangle[row][col] = int(not rectangle[row][col]) # flip bit
    
    # return the corrected data
    message_sequence = []
    for row in range(nrows):
        for col in range(ncols):
            message_sequence.append(rectangle[row][col])
    return message_sequence

if __name__ == '__main__':
    PS2_tests.test_correct_errors(rect_parity)
