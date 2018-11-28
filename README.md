# Installation

```sh
pip3 install -r requirements.txt
```

Note that python 3 is required.


# Run

```sh
./app.py
```


# GUI

Browse to http://127.0.0.1:5000


# REST

With [httpie](https://httpie.org/):

```sh
$ http 127.0.0.1:5000/api/k-means-clustering/10
HTTP/1.0 200 OK
Content-Length: 2137
Content-Type: application/json
Date: Wed, 28 Nov 2018 15:05:30 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

{
    "0": [
        "Hot Air",
        "Wonkette",
        "The Huffington Post | Raw Feed",
        "Jeremy Zawodny's blog",
        "lifehack.org",
        "Talking Points Memo: by Joshua Micah Marshall",
        "Gawker",
        "Kotaku",
        "Signal vs. Noise",
        "NewsBusters.org - Exposing Liberal Media Bias",
        "Gothamist",
        "Gizmodo",
        "The Blotter",
        "Shoemoney - Skills to pay the bills",
        "MetaFilter",
        "we make money not art",
        "Deadspin",
        "Instapundit.com",
        "flagrantdisregard",
        "Daily Kos",
        "ongoing",
        "Little Green Footballs",
        "WWdN: In Exile",
        "Eschaton",
        "Andrew Sullivan | The Daily Dish",
        "Go Fug Yourself",
        "plasticbag.org",
        "Michelle Malkin",
        "Joel on Software",
        "SpikedHumor",
        "Dave Shea's mezzoblue",
        "Think Progress",
        "Crooks and Liars",
        "Schneier on Security",
        "PerezHilton.com",
        "kottke.org",
        "Derek Powazek",
        "Joho the Blog",
        "Neil Gaiman's Journal",
        "The Superficial - Because You're Ugly",
        "Power Line",
        "Captain's Quarters"
    ],
    "1": [
        "John Battelle's Searchblog",
        "Publishing 2.0",
        "Official Google Blog",
        "Google Operating System",
        "GigaOM",
        "Lifehacker",
        "Wired News: Top Stories",
        "TechCrunch",
        "456 Berea Street",
        "Slashdot",
        "Search Engine Roundtable",
        "O'Reilly Radar",
        "Read/WriteWeb",
        "Topix.net Weblog",
        "Micro Persuasion",
        "A Consuming Experience (full feed)",
        "Google Blogoscoped",
        "PaulStamatiou.com",
        "Techdirt",
        "Matt Cutts: Gadgets, Google, and SEO",
        "Search Engine Watch Blog",
        "Valleywag"
    ],
    "2": [
        "Engadget",
        "TMZ.com",
        "Quick Online Tips",
        "TechEBlog",
        "43 Folders"
    ],
    "3": [
        "Download Squad",
        "Blog Maverick",
        "The Unofficial Apple Weblog (TUAW)",
        "CoolerHeads Prevail",
        "Joystiq"
    ],
    "4": [
        "Bloglines | News",
        "BuzzMachine",
        "SimpleBits",
        "Joi Ito's Web",
        "Signum sine tinnitu--by Guy Kawasaki",
        "Scobleizer - Tech Geek Blogger",
        "Bloggers Blog: Blogging the Blogsphere",
        "Autoblog",
        "ScienceBlogs : Combined Feed",
        "Creating Passionate Users",
        "Treehugger",
        "Copyblogger",
        "Oilman",
        "MAKE Magazine",
        "Pharyngula",
        "ProBlogger Blog Tips",
        "Boing Boing",
        "The Viral Garden",
        "Seth's Blog",
        "Steve Pavlina's Personal Development Blog",
        "Cool Hunting",
        "Sifry's Alerts",
        "gapingvoid: \"cartoons drawn on the back of business cards\"",
        "Online Marketing Report",
        "Mashable!"
    ]
}
```
