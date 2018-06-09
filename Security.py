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
    for row in readCSV:
        Domain.append(row[17])
        SSLCertificate.append(row[25])
        SSLKeyLength.append(row[30])
        SSLType.append(row[32])

print(Domain)
print(SSLCertificate)
print(SSLKeyLength)
print(SSLType)

trust = []

for answer in SSLCertificate:
    a = answer
    if a is 'No':
        trust.append(0)
    elif a is 'Yes':
        trust.append(1)
    else:
        trust.append(-1)

print(trust)
