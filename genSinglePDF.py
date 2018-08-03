# Generate a single A5 Landscape PDF with a word/phrase on it, which has been passed in.
# lots of postscript love from http://paulbourke.net/dataformats/postscript/

import subprocess
import sys

def genSinglePDF(word):

    print("Processsing: %s" % word )

    # split phrases onto multiple lines, if needed

    firstline=""
    secondline=""

    #identify need
    if (len(word) > 20):

        #print("word: %s splitting needed" % word)

        last_space = word.rfind(" ") # find last occurence of blank space
        firstline = word[0:last_space]
        secondline = word[last_space:]

        #print("first: %s second %s" % (firstline, secondline))
    else:
        firstline=word


    #center a bit better for tiny words.
    movex = 100
    if (len(word)<=5):
        movex = 200

    ## start PS string
    out_string="""
%%!
/Helvetica findfont 
50 scalefont 
setfont
90 rotate
%i -222 moveto
(%s) show
    """ % (movex,firstline)

    # add another line, if needed.
    if (secondline!=""):
        out_string+="""
114 -282 moveto 
(%s) show         
""" % secondline


    ## end PS string
    out_string+="""
showpage

%%EOF
    """

    output_file = "print/temp.eps"
    fout = open(output_file, "w")
    fout.write(out_string)
    fout.close()

    command = "ps2pdf -sPAPERSIZE=a5 print/temp.eps print/%s.pdf" % word.replace(" ", "") #replace blanks with nothing

    return_val = subprocess.call(command, shell=True)

    #throw an error and retain eps
    if (return_val):
        print("""Error: "%s" returned %s. """ % (command,return_val))
        print("Exiting.")
        sys.exit(1)



   # print(out_string)

