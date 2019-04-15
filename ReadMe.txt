How to use the Scripts for the "They Fight Crime NLP Assignment" 

Script 1: TheyFightCrimeNLP.py

The first script merges all of the files from the students that 
posted on the discussion board into a single file. To do this, I
downloaded and saved the .html file of the webpage from canvas. 
Using BeautifulSoup package to convert to a class HTMLParser for
parsing text files formatted in HTML. So in short for a user to 
use this Script, they should download and save the HTML file of 
their "They Fight Crime" data into the python project script. The
script goes through the html page line by line and find the 
desired text in the 'a' string of the html. This script will 
convert the html text into a single txt file for both the "he" 
and "she" fight crime lines. Note that this file takes a while to 
generate due to the size of the text files on canvas. Notice how 
the four last lines in the txt file were not converted properly 
into the txt file due to the students filing this data not properly
formatting the "he" and "she" data into the txt files on the 
canvas discussion board. 

Script 2: Sentiment.py

To find the best and worst characters of each gender, sentiment 
analysis was performed. Running this script might again take a 
while to run due to the size of the allheros.txt file. To do this,
the nltk.sentiment.vader function was imported from the 
SentimentIntensityAnalyzer. VADER belongs to a type of sentiment 
analysis that is based on lexicons of sentiment-related words. In 
this approach, each of the words in the lexicon is rated as to 
whether it is positive or negative, and in many cases, how 
positive or negative.This function will go through each of 
lines in the allheros.txt file and decide if the word positive, 
negative or neutral and will generate a "score" to see which of the
three words are most represented in the sentence. A neutral word
is defined as a word that does not appear in the lexicon of the 
function. The compound score is the sum of all of the lexicon 
ratings which have been standardized to range between -1 and 1. 1
being very positive and -1 being very negative. Finally, the 
script will combine the most positive characteristics with the 
most negative characteristics and generate the sentence in the 
original format of the joke. 


Script 3: Description.py

The last script finds the 10 most common descriptions for the 
characters and lists them. We are using the allheros.txt file. 
Using a dictionairy and a counter function I cound the most 
commonly used descriptions within each of the "he" and "she" 
sentences. I defined as the description as the entire sentence 
after the "he" and "she" component of the sentence. As can be 
seen, the script outputs the 10 most common descriptions based 
on the counter generated in lines 5-15 in the python script. 
Again, we are using the allheros.txt file which was generated in 
the first script. So if you wanted to run this code, you would 
just have to make sure to utilize the first script to add all the
sentences with descriptions in one final allheros.txt text file. 
