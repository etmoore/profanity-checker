import urllib

def read_text(path):
    quotes = open(path).read()
    return quotes

def check_profanity(text):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=' + text)
    result = connection.read()
    connection.close()
    return result

text = read_text('./movie_quotes.txt')
print check_profanity(text)
