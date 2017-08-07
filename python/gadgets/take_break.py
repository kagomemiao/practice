import time
import webbrowser

count = 0
while (count <= 2):
    time.sleep(10)
    webbrowser.open("https://www.baidu.com/")
    count = count + 1
