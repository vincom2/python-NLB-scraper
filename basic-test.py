#!/usr/bin/python3.2
import readline
import requests
import sys
from bs4 import BeautifulSoup

def nlb_server_error():
    print("Error in response from NLB server!\n", file=sys.stderr)
    sys.exit(1)

def get_search_string():
    name = input("Enter something to search for (empty input to exit): ")
    if name == '':
        sys.exit(0)
    return name.replace(" ","+")

def print_booklist(books):
    for b in books:
        print(b.text.strip())

def print_page_number(n):
    part1 = "on the "
    part3 = " page of results, we have:\n"
    m = n % 10
    if m == 1:
        part2 = "st"
    elif m == 2:
        part2 = "nd"
    else:
        part2 = "rd"
    print(part1 + str(n) + part2 + part3)

def print_page(pg,books):
    print_page_number(pg)
    print_booklist(books)

while True:
    findthis = get_search_string()
    result = requests.get("http://catalogue.nlb.gov.sg/cgi-bin/spydus.exe/ENQ/EXPNOS/BIBENQ?ENTRY=" +
        findthis + "&ENTRY_NAME=BS&ENTRY_TYPE=K&SORTS=DTE.DATE1.DESC]HBT.SOVR")
    if result.status_code != 200:
        nlb_server_error()

    soup = BeautifulSoup(result.content)
    books = soup.find_all("a", "results-title")
    pg = 1

    print_page(pg,books)

    next = soup.find("a", "next")
    while next != None:
        pg += 1
        input("press enter to see next page of results... ")

        result = requests.get("http://catalogue.nlb.gov.sg/" + next['href'])
        if result.status_code != 200:
            nlb_server_error()
        soup = BeautifulSoup(result.content)
        books = soup.find_all("a", "results-title")
        print_page(pg,books)

        next = soup.find("a", "next")


    print("No more results!\n")
