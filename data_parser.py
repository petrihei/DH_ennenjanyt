import re


# data_parser.py parses the articles that deal with digital topics

# Input data is ennenjanyt.net articles 2001-2016 (https://korp.csc.fi/download/lehdet90-00/) from Kielipankki

fileIn = 'teksti.txt'
inputfile = open(fileIn, 'r', encoding="utf-8")
document = inputfile.read()


# Split to separate articles
profilesList = re.split(r'<text title=', document)


word = "digita"
text_file = open("Ennenjanyt_output_data.txt", "w")

# Write output file that includes articles that include string "digita"
for line in profilesList:
    line_str = str(line)
    line_lower = line_str.lower()
    if word in line_lower:
        text_file.write(line)
text_file.close()