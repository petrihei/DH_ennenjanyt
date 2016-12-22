from stop_words import get_stop_words
from nltk.tokenize import RegexpTokenizer
from operator import itemgetter
import plotly
from plotly.graph_objs import Scatter, Layout


#Import default FI stop word list from stop_words package

stop_words = get_stop_words('finnish')

# Update stop word list based on output of the script. Exclude words that don't add information.

stop_words_update = ['paragraph', 'myös', '8211', "kuten", 'varsin', 'juuri', 'esimerkiksi', 'eli', 'vielä',
                     'toki', 'vain', 'kuitenkin', 'jo', 'text', 'asti', "auml", "ouml", "voi", "the", "rdquo",
                     "voidaan", "näin", "samalla", "miten", "eri", "and", "lisäksi", "usein", "tulee", "amp",
                     "muun", "http", "hyvin", "aina", "avulla", "kautta", "siis", "eikä", "kuinka", "kannalta", "jopa",
                     "ett", "ndash", "koko", "kaikki", "ennen", "olevan", "toisaalta", "kuitenkaan", "paljon",
                     "erityisesti", "vasta", "voivat", "ettei", "sek", "edelleen", "kohdalla", "muassa", "jolloin",
                     "taas", "mukana", "voisi", "joten"]


for i in stop_words_update:
    stop_words.append(i)

# Use output file from data_parser.py as input file

fileIn = "Ennenjanyt_output_data.txt"
inputfile = open(fileIn, 'r', encoding="utf-8")
document = inputfile.read()

# Tokenize text

tokenizer = RegexpTokenizer(r'\w+')
tokens = [i.lower() for i in tokenizer.tokenize(document) if i.lower() not in stop_words]

try:

    x = tokens

    t = {}
    avain_list = []
    arvo_list = []

# Calculate word frequency
    for word in x:
        t.update({word: x.count(word)})

# Create list for word as avain and frequency as arvo. Include first 100 words.
    for avain, arvo in sorted(t.items(), key=itemgetter(1), reverse=True)[:99]:
        if len(avain) > 2:
            avain_list.append(avain)
            arvo_list.append(arvo)

except IOError:
    print('Input file does not exist')
    quit()


# Create plot.ly bar chart visualization based on data

plotly.offline.plot({
"data": [
    plotly.graph_objs.Bar(x=avain_list,y=arvo_list)],
"layout": Layout(title="Suosituimmat sanat ennenjanyt.net-verkkolehden artikkeleissa 2001-2016, "
                       "joissa mainitaan digitaalisuus")
})


