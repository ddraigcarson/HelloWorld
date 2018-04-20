import urllib.request
import os
import csv

print("Hello World")

urlOfFileName = "http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2018-part1.csv"

localFilePath = "C:/Users/Greg/IdeaProjects/HelloWorld/resources/pp-2018-p1.csv"

webRequest = urllib.request.Request(urlOfFileName)

try:
    page = urllib.request.urlopen(webRequest)
    content = page.read()
    output = open(localFilePath, "wb")
    output.write(content)
    output.close()
except urllib.request.HTTPError as err:
    print(err.fp.read())

if os.path.exists(localFilePath):
    print("file exists")
    lineNum = 0
    listOfLists = []

    with open(localFilePath, "r") as csvFile:
        lineReader = csv.reader(csvFile)
        for row in lineReader:
            price = int(row[1])
            date = row[2]
            postcode = row[3]
            oneResultRow = [price, date, postcode]
            listOfLists.append(oneResultRow)
    print("done with file")

    listOfListsSorted = sorted(listOfLists, key=lambda x:x[0], reverse=True)
    print(listOfListsSorted)
else:
    print("no file")


