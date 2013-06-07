## Singapore NLB catalogue scraper<br/>
This uses requests/Beautiful Soup to scrape NLB's catalogue, and web.py to serve it up. At the moment, it only does the bog-standard search, which means (I think) search by keyword, no limiting by branch or whatnot.<br/>
serve-local.py is for non-WSGI use. serve.py is for WSGI use (well, I _think_. Bear in mind I don't actually know what I'm talking about; I pieced this shit together after frustrating minutes googling for a lot of different crap). Yes, there probably is a better way of sticking them in the same file, or at least, if they're going to be different files, avoid the complete copypasta, but I'm lazy and don't know how ifdefs (do they exist for this stuff?) or Python modules work. So thar :P<br/>

---
###Advantages:
Uh... well, for waiting a little longer, you get a plaintext list of _all_ results for your keyword(s). I don't believe this is possible on the NLB catalogue site proper, which is kind of annoying because their keyword search is not very good and so it can be useful to be able to Ctrl+F the results. I don't think there are any other advantages, lol, unless you particularly enjoy looking at absolutely bare pages over fancy ones. I have other ideas for this, but we'll see if I ever get around to implementing any of them...<br/>

---
###Usage:<br/>
#### Non-WSGI:<br/>
Put serve-local.py and templates/ (and yes, the .html files inside templates/, obviously) into the same directory. Then
```
python serve-local.py
```
Then visit ```127.0.0.1:8080``` in your browser.<br/>
<br/>
#### WSGI/App Engine (I don't actually know):<br/>
Just... upload it? Everything's here already, lol. Oh, but you have to take note of silly things like [this](http://webpy.org/cookbook/templates_on_gae). Meh.<br/>
<br/>
Oh, also, Python 2.7, preferably.<br/>

---
Try it for yourself! [http://nlbcatalogue.appspot.com/]