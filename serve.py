#!/usr/bin/python2.7
import requests
import web
from web import form
from bs4 import BeautifulSoup

def bad_stuff():
    raise web.redirect('/error')

def get_books(url):
    result = requests.get(url)
    if result.status_code != 200:
        bad_stuff()

    soup = BeautifulSoup(result.content)
    books = soup.find_all("a", "results-title")
    # option types plz
    next = soup.find("a", "next")
    #I should look up exception handling or something. awkz. so obvious I know no python lol.
    if next == None:
        return (books,None)
    else:
        return (books,next['href'])
    


def search_for(s):
    findthis = s.decode("utf-8").replace(" ","+")
    # result = requests.get("http://catalogue.nlb.gov.sg/cgi-bin/spydus.exe/ENQ/EXPNOS/BIBENQ?ENTRY=" +
    #     findthis + "&ENTRY_NAME=BS&ENTRY_TYPE=K&SORTS=DTE.DATE1.DESC]HBT.SOVR")

    # soup = BeautifulSoup(result.content)
    (books,next) = get_books("http://catalogue.nlb.gov.sg/cgi-bin/spydus.exe/ENQ/EXPNOS/BIBENQ?ENTRY=" +
        findthis + "&ENTRY_NAME=BS&ENTRY_TYPE=K&SORTS=DTE.DATE1.DESC]HBT.SOVR")
    pg = 1
    while next != None:
        pg += 1
        (tmp,next) = get_books("http://catalogue.nlb.gov.sg/" + next)
        books.extend(tmp)

    return (books,pg)



urls = (
    '/', 'index',
    '/error','error',
)
render = web.template.render('templates/')

searchfor_form = form.Form(
    form.Textbox("findthis", description="Search for"),
    form.Button("submit", type="submit", description="Search"),
    validators = [form.Validator("blah", lambda x: True)]
)

class index:
    def GET(self):
        f = searchfor_form()
        return render.index(f)

    def POST(self):
        f = searchfor_form()
        f.validates()
        return render.results(*search_for(f.d.findthis))

class error:
    def GET(self):
        return render.error()

class results:
    def GET(self,books,pages):
        return render.results(books,pages)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()