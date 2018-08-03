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
