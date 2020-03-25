from bs4 import BeautifulSoup
import re


def extractSA(soup):
    results = soup.findAll("span", {"class": "display-counter"})
    numTested = results[0].attrs.get('data-value')
    numPos = results[1].attrs.get('data-value')
    return numTested, numPos


def extractLatvia(soup):
    results = soup.findAll("span", {"style": "font-family:inherit"})
    numTested = re.findall('\d{1,5}', str(results[0]))[3]
    numPos = re.findall('\d{1,5}', str(results[0]))[5]
    return numTested, numPos


def extractKO(soup):
    results = soup.findAll("span")
    numTested = re.findall('\d{1,5}.{0,2}\d{1,5}', str(results[33]))
    numTested = numTested[0].replace(',', '')
    numPos = re.findall('\d{1,5}.{0,2}\d{0,5}', str(results[18]))
    numPos = numPos[0].replace(',', '')
    return numTested, numPos


def extractPH(soup):
    results = soup.findAll("font", {"face": "Arial"})
    numPos = re.findall('\d{1,5}', str(results[1]))[0]
    results = soup.findAll("font", {"face": "Arial"})
    numNeg = re.findall('\d{1,5}', str(results[0]))[0]
    numTested = str(float(numPos) + float(numNeg))
    return numTested, numPos


def extractMY(soup):
    result = soup.findAll("span", {"style": "font-size:16px;"})[2]
    numTested = re.findall('\d{5,10}', str(result))[0]
    result = soup.findAll("span", {"style": "font-size:16px;"})[1]
    numPos = re.findall('\d{3,10}', str(result))[0]
    return numTested, numPos
