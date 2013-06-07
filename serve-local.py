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
    # findthis = s.decode("utf-8").replace(" ","+")
    (books,next) = post_get_books(s)
    pg = 1
    while next != None:
        pg += 1
        (tmp,next) = get_books("http://catalogue.nlb.gov.sg/" + next)
        books.extend(tmp)

    return (books,pg)

#oh, the code duplication...
def post_get_books(s):
    payload = {'ENTRY1_NAME':'BS', 'ENTRY1':s, 'ENTRY1_TYPE':'K', 'ENTRY1_OPER':'+','NRECS':'100',
        'SORTS':'DTE.DATE1.DESC]HBT.SOVR', 'SEARCH_FORM':'/cgi-bin/spydus.exe/MSGTRN/EXPNOS/COMB?HOMEPRMS=COMBPARAMS'}
    result = requests.post("http://catalogue.nlb.gov.sg/cgi-bin/spydus.exe/ENQ/EXPNOS/BIBENQ", data=payload)
    if result.status_code != 200:
        bad_stuff()

    soup = BeautifulSoup(result.content)
    books = soup.find_all("a", "results-title")
    next = soup.find("a","next")
    if next == None:
        return (books,None)
    else:
        return (books,next['href'])


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
        (books,pages) = search_for(f.d.findthis)
        return render.results(books,f.d.findthis,pages)

class error:
    def GET(self):
        return render.error()

class results:
    def GET(self,books,term,pages):
        return render.results(books,term,pages)


if __name__ == "__main__":
    web.debug = False
    app = web.application(urls, globals(),autoreload=False)
    app.run()
