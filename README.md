## Singapore NLB catalogue scraper<br/>
This uses requests/Beautiful Soup to scrape NLB's catalogue, and web.py to serve it up. At the moment, it only does the bog-standard search, which means (I think) search by keyword, no limiting by branch or whatnot.<br/>

---
###Advantages:
Uh... well, for waiting a little longer, you get a plaintext list of _all_ results for your keyword(s). I don't believe this is possible on the NLB catalogue site proper, which is kind of annoying because their keyword search is not very good and so it can be useful to be able to Ctrl+F the results. I don't think there are any other advantages, lol, unless you particularly enjoy looking at absolutely bare pages over fancy ones. I have other ideas for this, but we'll see if I ever get around to implementing any of them...<br/>

---
###Usage:<br/>
```
python serve.py
```
Then visit ```127.0.0.1:8080``` in your browser.