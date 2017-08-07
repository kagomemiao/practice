import urllib

def read_file():
    q = open("D:/Dev/practice/python/resources/movie_quotes.txt")
    r = q.read()
    print(r)
    q.close()
    check_file(r)
    
def check_file(f):
    #because i am here in china so i need proxy to access google
    p = {"http":"http://127.0.0.1:1080"}
    c = urllib.urlopen("http://www.wdylike.appspot.com/?q="+f, proxies = p)
    v = c.read()
    print(v)
    c.close()

read_file()
