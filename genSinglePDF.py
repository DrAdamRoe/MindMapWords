import subprocess


def genSinglePDF(word):


    print("generating output for %s" % word )
    out_string="""
%%!
/Helvetica findfont 50 scalefont setfont
100 200 moveto
(%s) show

showpage

%%EOF
    """ % word

    output_file = "print/temp.eps"
    fout = open(output_file, "w")
    fout.write(out_string)
    fout.close()

    return_val = subprocess.call("ps2pdf print/temp.eps print/%s.pdf" % word.replace(" ", ""), shell=True)

   # print(out_string)

