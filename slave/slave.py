import urllib.request


print("Hi from client")
fp = urllib.request.urlopen("http://localhost:1234/")

print(fp)



fp.close()
