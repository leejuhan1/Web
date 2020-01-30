import urllib.request
 
url_1 = 'http://www.wechall.net/challenge/training/programming1/index.php?action=request'
url_2 = 'http://www.wechall.net/challenge/training/programming1/index.php?answer='
 
header = {"WC":"12402894-0-7KLHoUqJUnoUuLE3"}
 
req = urllib.request.Request(url_1,headers = header)
req.add_header('Cookie','Name=Value')
the_message = urllib.request.urlopen(req).read().decode('utf-8')
print(the_message)
 
url_2 = url_2+the_message
req = urllib.request.Request(url_2,headers = header)
req.add_header('Cookie','Name=Value')
html = urllib.request.urlopen(req).read().decode('utf-8')
print(html)