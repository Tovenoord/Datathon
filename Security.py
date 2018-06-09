import csv
from PIL import Image
import math
import numpy as np

with open('Dataset.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    Domain = []
    SSLCertificate = []
    SSLKeyLength = []
    SSLType = []
    startDate = []
    endDate = []
    DNSSEC = []
    for row in readCSV:
        Domain.append(row[17])
        SSLCertificate.append(row[25])
        SSLKeyLength.append(row[30])
        SSLType.append(row[32])
        startDate.append(row[28])
        endDate.append(row[29])
        DNSSEC.append(row[24])

Certificate = []

for answer in SSLCertificate:
    if answer == 'No':
        Certificate.append(0)
    elif answer == 'Yes':
        Certificate.append(1)
    else:
        Certificate.append(-1)

print(Certificate)

DNSSEClist = []

for answer in DNSSEC:
    if answer == 'No':
        DNSSEClist.append(0)
    elif answer == 'Yes':
        DNSSEClist.append(1)
    else:
        DNSSEClist.append(-1)

print(DNSSEClist)

Type = []

for answer in SSLType:
    if answer == 'Domain Validation':
        Type.append(1)
    elif answer == 'Organization Validation':
        Type.append(2)
    elif answer == 'Extended Validation':
        Type.append(3)
    else:
        Type.append(0)

print(Type)

KeyLength = []

i = 0

for answer in SSLKeyLength:
    if answer and i > 0:
        KeyLength.append(int(answer))
    else:
        KeyLength.append(0)
    i += 1

print(KeyLength)

startDateArray = []

temp = []

i = 0

for date in startDate:
    if date and i != 0:
        temp.append(int(date[0]))
        temp.append(int(date[1]))
        temp.append(int(date[2]))
        temp.append(int(date[3]))
        x = temp[0] * 1000
        x += temp[1] * 100
        x += temp[2] * 10
        x += temp[3]
        x *= 10000
        temp.append(int(date[5]))
        temp.append(int(date[6]))
        y = temp[4] * 10
        y += temp[5]
        y *= 100
        temp.append(int(date[8]))
        temp.append(int(date[9]))
        z = temp[6] * 10
        z += temp[7]
        x = x + y + z
        startDateArray.append(x)
        temp = []
    else:
        startDateArray.append(0)
    i += 1

print(startDateArray)


endDateArray = []

temp = []

i = 0

for date in endDate:
    if date and i != 0:
        temp.append(int(date[0]))
        temp.append(int(date[1]))
        temp.append(int(date[2]))
        temp.append(int(date[3]))
        x = temp[0] * 1000
        x += temp[1] * 100
        x += temp[2] * 10
        x += temp[3]
        x *= 10000
        temp.append(int(date[5]))
        temp.append(int(date[6]))
        y = temp[4] * 10
        y += temp[5]
        y *= 100
        temp.append(int(date[8]))
        temp.append(int(date[9]))
        z = temp[6] * 10
        z += temp[7]
        x = x + y + z
        endDateArray.append(x)
        temp = []
    else:
        endDateArray.append(0)
    i += 1

print(endDateArray)

isValidDate = []

i = 0

for date in startDateArray:
    if endDateArray[i] - 20180609 > 0:
        if 20180609 < date:
            isValidDate.append(1)
        else:
            isValidDate.append(0)
    else:
        isValidDate.append(-1)
    i += 1

print("Size is ", i)
print(isValidDate)

uniqueKeys = []
boolean = 0


for n in KeyLength:
    for element in uniqueKeys:
        if n == element:
            boolean = 1
    if boolean == 0:
        uniqueKeys.append(n)
    boolean = 0

print(uniqueKeys)

scoreArray = []

i = 0
j = 0

score = 0

for n in Certificate:
    score += n
    score += DNSSEClist[i]
    score += Type[i]
    if KeyLength[i] == 256:
        score += 1
    elif KeyLength[i] == 384:
        score += 2
    elif KeyLength[i] == 1024:
        score += 3
    elif KeyLength[i] == 2048:
        score += 4
    elif KeyLength[i] == 4096:
        score += 5
    if isValidDate[i] == 1:
        score += 1
    scoreArray.append(score)
    score = 0
    i += 1

var = "start"

while var != "!":
    var = input("enter a domain: ")
    i = 0
    for d in Domain:
        if var == d:
            print("score:", scoreArray[i])
        i += 1

i = 0
for d in Domain:
    print("<tr><td>" + d + "</td><td>" + str(scoreArray[i]) + "<\\td><\\tr>")
    i += 1
