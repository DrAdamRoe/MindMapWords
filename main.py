#### A neat way to generate a ton of A5 files from a list of words, one entry per file.
#### Built for a mindmap at the CODE Summer School


# keep it clean, several self-defined functions with lots of HTMl and EPS formatting
# import style adapted from solution 7 https://stackoverflow.com/questions/2349991/how-to-import-other-python-files

from genHTML import genHTML
from genSinglePDF import genSinglePDF


# read in external text file line by line.
# adapted from https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list

def getWords(filename):
    with open(filename) as file:
        content = file.read().splitlines()

    print("File %s opened and read" % filename)

    return content

def main():
    words_list = getWords("input/words.txt")
    genHTML(words_list)
    for word in words_list:
        genSinglePDF(word)

if __name__== "__main__":
    main()