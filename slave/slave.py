import urllib.request


print("Hi from client")

fp = urllib.request.urlopen("http://localhost:1234/")

encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

# Display the server file: 'index.html'.
print(decodedContent)

# Close the server connection.
fp.close()
