# template file for 6.02 PS1, Python Task 4 (LZW Compression/Decompression)
import sys
from optparse import OptionParser
import struct
import array

def compress(filename):
    """
    Compresses a file using the LZW algorithm and saves output in another file.
    Arguments: 
        filename: filename of file to compress.
    Returns:
        None.
    """
    f = open(filename, 'rb')
    uncompressed = array.array("B", f.read())
    table = [chr(i) for i in range(256)]
    string = table[uncompressed[0]]
    compressed = array.array("H")
    try:
        for ascii_code in uncompressed[1:]:
            symbol = table[ascii_code]
            if string + symbol in table:
                string += symbol
            else:
                compressed.append(table.index(string))
                table.append(string + symbol)
                string = symbol
        compressed.append(table.index(string))
        outfile = open(filename + '.zl', 'wb')
        compressed.tofile(outfile)
    except OverflowError:
        print "This file needs more than 2**16 entries"

def uncompress(filename):
    """
    Decompresses a file using the LZW algorithm and saves output in another file.
    Arguments: 
        filename: filename of file to decompress.
    Returns:
        None.
    """
    f = open(filename, 'rb')
    compressed = array.array("H", f.read())
    table = [chr(i) for i in range(256)]
    code = compressed[0]
    string = table[code]
    outfile = open(filename + '.u', 'w')
    outfile.write(string)
    for code in compressed[1:]:
        if code >= len(table):
            entry = string + string[0]
        else:
            entry = table[code]
        outfile.write(entry)
        table.append(string + entry[0])
        string = entry

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--filename", type="string", dest="fname", 
                      default="test", help="file to compress or uncompress")
    parser.add_option("-c", "--compress", action="store_true", dest="uncomp", 
                      default=True, help="compress file")
    parser.add_option("-u", "--uncompress", action="store_true", dest="uncomp", 
                      default=False, help="uncompress file")

    (opt, args) = parser.parse_args()
    
    if opt.uncomp == True:
        uncompress(opt.fname)
    else:
        compress(opt.fname)
