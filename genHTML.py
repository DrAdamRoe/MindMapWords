# Generate an HTML file with all words passed in, for purposes of easy sharing e.g. using rawgit)

def genHTML(words_list):

    out_string="""
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Wordslist</title>
            <style>
               body {font-family: Verdana, Geneva, sans-serif}
               p {margin-left: 20px}
            </style>
        </head>
        <body>
        <h3> Words for a Software Engineering Mind Map </h3>
    """

    for word in range(len(words_list)):
       out_string+="""
       <p>%s</p>
       """ % words_list[word]

    out_string+="""
        
    </body>
    </html>

    """

    output_file = "test/out.html"
    fout = open(output_file, "w")
    fout.write(out_string)
    fout.close()

    print("File %s written" % output_file)