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


# K-means REST

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


# Hierarchical REST

With [httpie](https://httpie.org/) (note that it will take quite some
time to compute the hierarchical cluster):

```sh
$ http --timeout 600 127.0.0.1:5000/api/hierarchical-clustering
HTTP/1.0 200 OK
Content-Length: 6138
Content-Type: application/json
Date: Wed, 28 Nov 2018 22:35:34 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

{
    "root": {
        "blog": "",
        "left": {
            "blog": "gapingvoid: \"cartoons drawn on the back of business cards\""
        },
        "right": {
            "blog": "",
            "left": {
                "blog": "",
                "left": {
                    "blog": "Schneier on Security"
                },
                "right": {
                    "blog": "Instapundit.com"
                }
            },
            "right": {
                "blog": "",
                "left": {
                    "blog": "The Blotter"
                },
                "right": {
                    "blog": "",
                    "left": {
                        "blog": "",
                        "left": {
                            "blog": "MetaFilter"
                        },
                        "right": {
                            "blog": "",
                            "left": {
                                "blog": "SpikedHumor"
                            },
                            "right": {
                                "blog": "",
                                "left": {
                                    "blog": "Captain's Quarters"
                                },
                                "right": {
                                    "blog": "",
                                    "left": {
                                        "blog": "Michelle Malkin"
                                    },
                                    "right": {
                                        "blog": "",
                                        "left": {
                                            "blog": "",
                                            "left": {
                                                "blog": "NewsBusters.org - Exposing Liberal Media Bias"
                                            },
                                            "right": {
                                                "blog": "",
                                                "left": {
                                                    "blog": "",
                                                    "left": {
                                                        "blog": "Hot Air"
                                                    },
                                                    "right": {
                                                        "blog": "Crooks and Liars"
                                                    }
                                                },
                                                "right": {
                                                    "blog": "",
                                                    "left": {
                                                        "blog": "Think Progress"
                                                    },
                                                    "right": {
                                                        "blog": "Power Line"
                                                    }
                                                }
                                            }
                                        },
                                        "right": {
                                            "blog": "",
                                            "left": {
                                                "blog": "Andrew Sullivan | The Daily Dish"
                                            },
                                            "right": {
                                                "blog": "",
                                                "left": {
                                                    "blog": "Little Green Footballs"
                                                },
                                                "right": {
                                                    "blog": "",
                                                    "left": {
                                                        "blog": "Eschaton"
                                                    },
                                                    "right": {
                                                        "blog": "",
                                                        "left": {
                                                            "blog": "Talking Points Memo: by Joshua Micah Marshall"
                                                        },
                                                        "right": {
                                                            "blog": "Daily Kos"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "right": {
                        "blog": "",
                        "left": {
                            "blog": "43 Folders"
                        },
                        "right": {
                            "blog": "",
                            "left": {
                                "blog": "TechEBlog"
                            },
                            "right": {
                                "blog": "",
                                "left": {
                                    "blog": "",
                                    "left": {
                                        "blog": "Signum sine tinnitu--by Guy Kawasaki"
                                    },
                                    "right": {
                                        "blog": "Mashable!"
                                    }
                                },
                                "right": {
                                    "blog": "",
                                    "left": {
                                        "blog": "",
                                        "left": {
                                            "blog": "",
                                            "left": {
                                                "blog": "Slashdot"
                                            },
                                            "right": {
                                                "blog": "",
                                                "left": {
                                                    "blog": "Boing Boing"
                                                },
                                                "right": {
                                                    "blog": "MAKE Magazine"
                                                }
                                            }
                                        },
                                        "right": {
                                            "blog": "",
                                            "left": {
                                                "blog": "",
                                                "left": {
                                                    "blog": "Oilman"
                                                },
                                                "right": {
                                                    "blog": "",
                                                    "left": {
                                                        "blog": "Online Marketing Report"
                                                    },
                                                    "right": {
                                                        "blog": "",
                                                        "left": {
                                                            "blog": "Treehugger"
                                                        },
                                                        "right": {
                                                            "blog": "",
                                                            "left": {
                                                                "blog": "SimpleBits"
                                                            },
                                                            "right": {
                                                                "blog": "",
                                                                "left": {
                                                                    "blog": "Cool Hunting"
                                                                },
                                                                "right": {
                                                                    "blog": "",
                                                                    "left": {
                                                                        "blog": "Steve Pavlina's Personal Development Blog"
                                                                    },
                                                                    "right": {
                                                                        "blog": "",
                                                                        "left": {
                                                                            "blog": "",
                                                                            "left": {
                                                                                "blog": "ScienceBlogs : Combined Feed"
                                                                            },
                                                                            "right": {
                                                                                "blog": "Pharyngula"
                                                                            }
                                                                        },
                                                                        "right": {
                                                                            "blog": "",
                                                                            "left": {
                                                                                "blog": "BuzzMachine"
                                                                            },
                                                                            "right": {
                                                                                "blog": "",
                                                                                "left": {
                                                                                    "blog": "Copyblogger"
                                                                                },
                                                                                "right": {
                                                                                    "blog": "",
                                                                                    "left": {
                                                                                        "blog": "",
                                                                                        "left": {
                                                                                            "blog": "The Viral Garden"
                                                                                        },
                                                                                        "right": {
                                                                                            "blog": "Seth's Blog"
                                                                                        }
                                                                                    },
                                                                                    "right": {
                                                                                        "blog": "",
                                                                                        "left": {
                                                                                            "blog": "",
                                                                                            "left": {
                                                                                                "blog": "Bloggers Blog: Blogging the Blogsphere"
                                                                                            },
                                                                                            "right": {
                                                                                                "blog": "",
                                                                                                "left": {
                                                                                                    "blog": "Sifry's Alerts"
                                                                                                },
                                                                                                "right": {
                                                                                                    "blog": "ProBlogger Blog Tips"
                                                                                                }
                                                                                            }
                                                                                        },
                                                                                        "right": {
                                                                                            "blog": "",
                                                                                            "left": {
                                                                                                "blog": "",
                                                                                                "left": {
                                                                                                    "blog": "Valleywag"
                                                                                                },
                                                                                                "right": {
                                                                                                    "blog": "Scobleizer - Tech Geek Blogger"
                                                                                                }
                                                                                            },
                                                                                            "right": {
                                                                                                "blog": "",
                                                                                                "left": {
                                                                                                    "blog": "",
                                                                                                    "left": {
                                                                                                        "blog": "456 Berea Street"
                                                                                                    },
                                                                                                    "right": {
                                                                                                        "blog": "O'Reilly Radar"
                                                                                                    }
                                                                                                },
                                                                                                "right": {
                                                                                                    "blog": "",
                                                                                                    "left": {
                                                                                                        "blog": "Lifehacker"
                                                                                                    },
                                                                                                    "right": {
                                                                                                        "blog": "",
                                                                                                        "left": {
                                                                                                            "blog": "Quick Online Tips"
                                                                                                        },
                                                                                                        "right": {
                                                                                                            "blog": "",
                                                                                                            "left": {
                                                                                                                "blog": "Publishing 2.0"
                                                                                                            },
                                                                                                            "right": {
                                                                                                                "blog": "",
                                                                                                                "left": {
                                                                                                                    "blog": "Micro Persuasion"
                                                                                                                },
                                                                                                                "right": {
                                                                                                                    "blog": "",
                                                                                                                    "left": {
                                                                                                                        "blog": "A Consuming Experience (full feed)"
                                                                                                                    },
                                                                                                                    "right": {
                                                                                                                        "blog": "",
                                                                                                                        "left": {
                                                                                                                            "blog": "John Battelle's Searchblog"
                                                                                                                        },
                                                                                                                        "right": {
                                                                                                                            "blog": "",
                                                                                                                            "left": {
                                                                                                                                "blog": "Search Engine Watch Blog"
                                                                                                                            },
                                                                                                                            "right": {
                                                                                                                                "blog": "",
                                                                                                                                "left": {
                                                                                                                                    "blog": "Read/WriteWeb"
                                                                                                                                },
                                                                                                                                "right": {
                                                                                                                                    "blog": "",
                                                                                                                                    "left": {
                                                                                                                                        "blog": "Official Google Blog"
                                                                                                                                    },
                                                                                                                                    "right": {
                                                                                                                                        "blog": "",
                                                                                                                                        "left": {
                                                                                                                                            "blog": "Search Engine Roundtable"
                                                                                                                                        },
                                                                                                                                        "right": {
                                                                                                                                            "blog": "",
                                                                                                                                            "left": {
                                                                                                                                                "blog": "Google Blogoscoped"
                                                                                                                                            },
                                                                                                                                            "right": {
                                                                                                                                                "blog": "Google Operating System"
                                                                                                                                            }
                                                                                                                                        }
                                                                                                                                    }
                                                                                                                                }
                                                                                                                            }
                                                                                                                        }
                                                                                                                    }
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            },
                                            "right": {
                                                "blog": "",
                                                "left": {
                                                    "blog": "",
                                                    "left": {
                                                        "blog": "",
                                                        "left": {
                                                            "blog": "",
                                                            "left": {
                                                                "blog": "Blog Maverick"
                                                            },
                                                            "right": {
                                                                "blog": "",
                                                                "left": {
                                                                    "blog": "Download Squad"
                                                                },
                                                                "right": {
                                                                    "blog": "",
                                                                    "left": {
                                                                        "blog": "CoolerHeads Prevail"
                                                                    },
                                                                    "right": {
                                                                        "blog": "",
                                                                        "left": {
                                                                            "blog": "The Unofficial Apple Weblog (TUAW)"
                                                                        },
                                                                        "right": {
                                                                            "blog": "Joystiq"
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        },
                                                        "right": {
                                                            "blog": "",
                                                            "left": {
                                                                "blog": "Autoblog"
                                                            },
                                                            "right": {
                                                                "blog": "",
                                                                "left": {
                                                                    "blog": "Engadget"
                                                                },
                                                                "right": {
                                                                    "blog": "TMZ.com"
                                                                }
                                                            }
                                                        }
                                                    },
                                                    "right": {
                                                        "blog": "",
                                                        "left": {
                                                            "blog": "Matt Cutts: Gadgets, Google, and SEO"
                                                        },
                                                        "right": {
                                                            "blog": "",
                                                            "left": {
                                                                "blog": "PaulStamatiou.com"
                                                            },
                                                            "right": {
                                                                "blog": "",
                                                                "left": {
                                                                    "blog": "",
                                                                    "left": {
                                                                        "blog": "TechCrunch"
                                                                    },
                                                                    "right": {
                                                                        "blog": "GigaOM"
                                                                    }
                                                                },
                                                                "right": {
                                                                    "blog": "",
                                                                    "left": {
                                                                        "blog": "",
                                                                        "left": {
                                                                            "blog": "Creating Passionate Users"
                                                                        },
                                                                        "right": {
                                                                            "blog": "Techdirt"
                                                                        }
                                                                    },
                                                                    "right": {
                                                                        "blog": "",
                                                                        "left": {
                                                                            "blog": "Joho the Blog"
                                                                        },
                                                                        "right": {
                                                                            "blog": "",
                                                                            "left": {
                                                                                "blog": "",
                                                                                "left": {
                                                                                    "blog": "PerezHilton.com"
                                                                                },
                                                                                "right": {
                                                                                    "blog": "Jeremy Zawodny's blog"
                                                                                }
                                                                            },
                                                                            "right": {
                                                                                "blog": "",
                                                                                "left": {
                                                                                    "blog": "Joi Ito's Web"
                                                                                },
                                                                                "right": {
                                                                                    "blog": "",
                                                                                    "left": {
                                                                                        "blog": "ongoing"
                                                                                    },
                                                                                    "right": {
                                                                                        "blog": "",
                                                                                        "left": {
                                                                                            "blog": "Joel on Software"
                                                                                        },
                                                                                        "right": {
                                                                                            "blog": "",
                                                                                            "left": {
                                                                                                "blog": "",
                                                                                                "left": {
                                                                                                    "blog": "we make money not art"
                                                                                                },
                                                                                                "right": {
                                                                                                    "blog": "",
                                                                                                    "left": {
                                                                                                        "blog": "plasticbag.org"
                                                                                                    },
                                                                                                    "right": {
                                                                                                        "blog": "",
                                                                                                        "left": {
                                                                                                            "blog": "Signal vs. Noise"
                                                                                                        },
                                                                                                        "right": {
                                                                                                            "blog": "",
                                                                                                            "left": {
                                                                                                                "blog": "kottke.org"
                                                                                                            },
                                                                                                            "right": {
                                                                                                                "blog": "",
                                                                                                                "left": {
                                                                                                                    "blog": "Neil Gaiman's Journal"
                                                                                                                },
                                                                                                                "right": {
                                                                                                                    "blog": "",
                                                                                                                    "left": {
                                                                                                                        "blog": "",
                                                                                                                        "left": {
                                                                                                                            "blog": "The Huffington Post | Raw Feed"
                                                                                                                        },
                                                                                                                        "right": {
                                                                                                                            "blog": "",
                                                                                                                            "left": {
                                                                                                                                "blog": "Wonkette"
                                                                                                                            },
                                                                                                                            "right": {
                                                                                                                                "blog": "",
                                                                                                                                "left": {
                                                                                                                                    "blog": "Gawker"
                                                                                                                                },
                                                                                                                                "right": {
                                                                                                                                    "blog": "",
                                                                                                                                    "left": {
                                                                                                                                        "blog": "Go Fug Yourself"
                                                                                                                                    },
                                                                                                                                    "right": {
                                                                                                                                        "blog": "The Superficial - Because You're Ugly"
                                                                                                                                    }
                                                                                                                                }
                                                                                                                            }
                                                                                                                        }
                                                                                                                    },
                                                                                                                    "right": {
                                                                                                                        "blog": "",
                                                                                                                        "left": {
                                                                                                                            "blog": "Deadspin"
                                                                                                                        },
                                                                                                                        "right": {
                                                                                                                            "blog": "Gothamist"
                                                                                                                        }
                                                                                                                    }
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                }
                                                                                            },
                                                                                            "right": {
                                                                                                "blog": "",
                                                                                                "left": {
                                                                                                    "blog": "Gizmodo"
                                                                                                },
                                                                                                "right": {
                                                                                                    "blog": "Kotaku"
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                },
                                                "right": {
                                                    "blog": "",
                                                    "left": {
                                                        "blog": "Shoemoney - Skills to pay the bills"
                                                    },
                                                    "right": {
                                                        "blog": "",
                                                        "left": {
                                                            "blog": "flagrantdisregard"
                                                        },
                                                        "right": {
                                                            "blog": "",
                                                            "left": {
                                                                "blog": "WWdN: In Exile"
                                                            },
                                                            "right": {
                                                                "blog": "",
                                                                "left": {
                                                                    "blog": "Derek Powazek"
                                                                },
                                                                "right": {
                                                                    "blog": "",
                                                                    "left": {
                                                                        "blog": "Dave Shea's mezzoblue"
                                                                    },
                                                                    "right": {
                                                                        "blog": "lifehack.org"
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "right": {
                                        "blog": "",
                                        "left": {
                                            "blog": "Wired News: Top Stories"
                                        },
                                        "right": {
                                            "blog": "",
                                            "left": {
                                                "blog": "Topix.net Weblog"
                                            },
                                            "right": {
                                                "blog": "Bloglines | News"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
```
