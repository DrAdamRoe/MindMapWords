#### A neat way to generate a ton of A5 files from a list of words, one entry per file.
#### Built for a mindmap at the CODE Summer School


# keep it clean, several self-defined functions with lots of HTMl and EPS formatting
# import style adapted from solution 7 https://stackoverflow.com/questions/2349991/how-to-import-other-python-files

import sys
from genHTML import genHTML
from genSinglePDF import genSinglePDF
from getWords import getWords

def main():

    inp = "input/words.txt"

    print("""
    Generating a set of printable files with 1 word per page from %s         
    """ % inp)

    # read in text file
    words_list = getWords(inp)

    # generate html (for sharing)
    genHTML(words_list)

    # generate PDFs (for printing)
    for word in words_list:
        genSinglePDF(word)

    print("""
    Succesfully generated files to print. bye now.
    """)
    sys.exit(0)

if __name__== "__main__":
    main()