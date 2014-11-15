# Yo, I am BORED.

Meetings are really boring.


## For users

1. Install the [Yo](http://www.justyo.co/) app or [make a Yo dev account](http://dev.justyo.co/).
1. Yo `YOIAMBORED` when you are bored.
1. Visit the boredom monitoring website, probably <http://yo-i-am-bored.ngrok.com/>, to see who else is bored.


## Server use

First, make some port available for http, say using [ngrok](http://ngrok.com):

    ngrok -subdomain="yo-i-am-bored" 8080

Then listen to that port:

    python listen.py 8080

Now that port will display a list of bored people.

You can also [set a custom Yo target](http://docs.justyo.co/v1.0/docs/receiving-a-yo-with-the-api): just use your publicly-facing URL as the callback address.
