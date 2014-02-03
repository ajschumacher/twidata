#!/usr/bin/env python

from config import *
from TwitterAPI import TwitterAPI

api = TwitterAPI(consumer_key, consumer_secret,
                 access_token_key, access_token_secret)

r = api.request('statuses/filter', {'track':'data'})

with open(file_location, "a") as output:
    for item in r.get_iterator():
        output.write(str(item) + "\n")
