from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

hesent = 0
hephrase = ''

shesent = 0
shephrase = ''

for sentence in open('allheros.txt'):
    if sentence != '':
        ss = sid.polarity_scores(sentence)

        if sentence.split(' ')[0] == "He's":
            if ss['pos'] > hesent:
                hesent = ss['pos']
                hephrase = sentence
        elif sentence.split(' ')[0] == "She's":
            if ss['pos'] > shesent:
                shesent = ss['pos']
                shephrase = sentence

final = hephrase.replace('\n', ' ') + shephrase.replace('\n', ' ') + 'They fight crime!'
print(final)