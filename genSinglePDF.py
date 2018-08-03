import subprocess
import sys


def genSinglePDF(word):


    #TODO: set size to A5, figure out how to print this..

    print("Processsing: %s" % word )
    out_string="""
%%!
/Helvetica findfont 
50 scalefont 
setfont
90 rotate
100 -222 moveto
(%s) show

showpage

%%EOF
    """ % word

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

