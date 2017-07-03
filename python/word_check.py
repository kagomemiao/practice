import urllib

def read_file():
    q = open("/Users/katerina/Documents/practice/python/resources/movie_quotes.txt")
    r = q.read()
    print(r)
    q.close()
    check_file(r)
    
def check_file(f):
    c = urllib.urlopen("http://www.wdylike.appspot.com/?q="+f)
    v = c.read()
    print(v)
    c.close()

read_file()
    
