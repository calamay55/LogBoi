Documentation is Teal's job, I'm outta here

So far, this logs into Mibbit and navigates to the logs tab. It doesn't download logs yet.

This requires a few things:

- chromedriver in the PATH (on Windows, just plop chromedriver into the same folder as logboi.py)

- A properties.py file in the following format:
ON LINE 1: username = "(your username)"
ON LINE 2: password = "(your password)"

As long as there are no nickname conflicts, it should go right to the log tab. From there we have to figure out how to iterate through the various channels and dates. Challenges here include:
- the fact that a "DELETE ALL LOGS FOR THIS CHANNEL" button is right next to the channel name, for some reason
- the links aren't arranged in a proper list
