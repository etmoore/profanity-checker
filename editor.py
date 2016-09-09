import urllib

def read_text(path):
    quotes = open(path).read()
    return quotes

def check_profanity(text):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=' + text)
    return connection.read()

text = read_text('./movie_quotes.txt')
print check_profanity(text)
