import csv


def binaryClassification(list):
    newList = []
    for answer in list:
        if answer == 'No':
            newList.append(0)
        elif answer == 'Yes':
            newList.append(1)
        else:
            newList.append(-1)
    return newList


def typeToList(list):
    typeList = []
    for answer in list:
        if answer == 'Domain Validation':
            typeList.append(1)
        elif answer == 'Organization Validation':
            typeList.append(2)
        elif answer == 'Extended Validation':
            typeList.append(3)
        else:
            typeList.append(0)
    return typeList


def keyLength(list):
    i = 0
    newList = []
    for answer in list:
        if answer and i > 0:
            newList.append(int(answer))
        else:
            newList.append(0)
        i += 1
    return newList


def dates(list):
    newList = []
    temp = []

    i = 0

    for date in list:
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
            newList.append(x)
            temp = []
        else:
            newList.append(0)
        i += 1
    return newList


def validDate(lista, listb):
    newList = []

    i = 0

    for date in lista:
        if listb[i] > 20180609:
            if 20180609 > date:
                newList.append(1)
            else:
                newList.append(0)
        else:
            newList.append(0)
        i += 1
    return newList


def scoring(listCert, listDNS, listType, listKeyLength, listValidDate):
    newList = []

    i = 0

    score = 0

    for n in listCert:
        score += n
        score += listDNS[i]
        score += listType[i]
        if listKeyLength[i] == 256:
            score += 1
        elif listKeyLength[i] == 384:
            score += 2
        elif listKeyLength[i] == 1024:
            score += 3
        elif listKeyLength[i] == 2048:
            score += 4
        elif listKeyLength[i] == 4096:
            score += 5
        if listValidDate[i] == 1:
            score += 1
        newList.append(score)
        score = 0
        i += 1

    return newList


def runProgram(domainList, list):
    var = "."
    while var != "!":
        var = input("enter a domain: ")
        i = 0
        for d in domainList:
            if var == d:
                print("score:", list[i])
            i += 1


def main():
    # Opens the csv file and saves the necessary rows in arrays
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

    # Certificate stores if a domain has a SSL certificate or not
    Certificate = binaryClassification(SSLCertificate)

    # DNSSEClist stores if a domain has DNSSEC or not
    DNSSEClist = binaryClassification(DNSSEC)

    # TypeList stores the type of SSL type a domain uses, with 1 for domain validation, 2 for organization validation,
    # and 3 for extended validation
    TypeList = typeToList(SSLType)

    # KeyLength stores the length of SSL RSA keys
    KeyLength = keyLength(SSLKeyLength)

    # startDateArray and endDateArray store the starting and ending dates for SSL certificates for each domain
    startDateArray = dates(startDate)
    endDateArray = dates(endDate)

    # isValidDate array stores whether or not an array has a valid date (meaning that it is in between the start and end
    # date
    isValidDate = validDate(startDateArray, endDateArray)

    # scoreArray assigns a security score for each domain, which is an indication of how secure it is
    scoreArray = scoring(Certificate, DNSSEClist, TypeList, KeyLength, isValidDate)

    # Runs program in an infinite loop, it asks for a domain name and prints its score. It ends if ! is used as input
    runProgram(Domain, scoreArray)


if __name__ == "__main__":
    main()
