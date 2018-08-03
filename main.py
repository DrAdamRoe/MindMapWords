#### A neat way to generate a ton of A5 files from a list of words, one entry per file.
#### Built for a mindmap at the CODE Summer School


# keep it clean, several self-defined functions with lots of HTMl and EPS formatting
# import style adapted from solution 7 https://stackoverflow.com/questions/2349991/how-to-import-other-python-files

from genHTML import genHTML
from genSinglePDF import genSinglePDF


# function to read external text file, clean, and return as list
def getWords(filename):

    # read in external text file line by line.
    # adapted from https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list

    with open(filename) as file:
        content = file.read().splitlines()

    # remove duplicates from words list
    #interesting regarding collections on https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
    #going with old fashined set approach because versioning hell
    content_set = list(set(content))

    # remove any trailing blank lines
    content_set.remove("")

    content_set.sort()

    print("File %s opened and read. Final list contains %i words." % (filename, len(content_set)))

    return content_set

def main():

    inp = "input/words.txt"
    print("""
    Generating a set of printable files with 1 word per page from %s         
    """ % inp)
    words_list = getWords(inp)
    genHTML(words_list)
    for word in words_list:
        genSinglePDF(word)

if __name__== "__main__":
    main()