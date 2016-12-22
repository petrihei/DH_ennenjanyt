# Hands-on assignment

The assignment was done for the course Introduction to methods in digital humanities at the University of Helsinki, Autumn 2016.

THE TASK

I wanted to study Finnish peer-reviewed history online journal Ennenjanyt.net. The exact question was to gather information about
what topics do the articles that mention "digital" cover. This was done with Python scripting and Plotly visualization.

THE DATASET

The dataset was ennenjanyt.net articles 2001-2016 (https://korp.csc.fi/download/lehdet90-00/) from Kielipankki. I downloaded the txt-file including all articles to my laptop.

PYTHON SCRIPT AND PLOTLY VISUALIZATION

I created two Python scripts. The first one was for data parsing. I needed to filter only the articles that included string "digita" in the text.

Second Python script was to find the most popular words that had meaningful information about the content of the articles.

Second script does the following:

-Use the output file of data_parser.py as input file

-Import and update the Finnish stop words. Updating the stop word list was done after the first version of the visualization.
-Tokenize the data

-Calculate the word frequencies and create sorted lists based on frequency

-Create Plotly bar chart visualization for top-100 words with highest frequency. I tested other visualizations like word cloud, but good old bar chart was best for the purpose.

ANALYSIS

After the cleaning with stop words update, the visualization actually shows quite interesting data.


-Word "suomi" and its other forms are the most popular words in the articles. Probably digital history research covers mostly national topics like history studies in general.

-Word "1800" has frequency of 77 and word "1700" frequency of 27. Probably 19th century is more popular topic in these articles than 18th century.

-Words like "aineisto", "elokuva" and "kuva" are in the top-100. Probably articles cover quite a lot visual digital archive topics.

-There are few words in the top-100 that are related to war. For instance "sodan" and "luutnantti". Probably war history is also digitalizing.

-Word "aatehistoria" is mentioned 24 times. There is at least one article covering intellectual history and its relation to digital.

-Word "mit" is mentioned 29 times. It can be either MIT university or some data error. Needs further inspection.

Word frequency visualization is a very crude method and it is very hard to make final conclusions based on only that. However, it's also very efficient method.
The input data included hundreds of articles and reading it would have taken long time. With this script, I was able to get harsh understanding of the most popular topics very fast.
It could beneficial to combine this kind of computational distant reading with close reading in real research.
