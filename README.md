# Demographics from Twitter names

The motivation for this code was a presentation in the Berlin AWS User Group.
Python is a great programming language which enables one to realize great use cases with just a few lines of code.
Additionally, a bunch of machine learning and artificial intelligence libraries are available.

This code shows you how you can estimate the sex and the age of your audience based on the Twitter forenames.
There are a lot of companies (e.g. http://quantifind.com/) combining this method with a sentiment analysis to give you details about the audience using your product and if they like or dislike it.

* Important: You find a polished version regarding the code in the repo of my colleague Eike: *
https://github.com/eikevons/demographics-from-twitter-names

Install:

    pip install scrapy
    pip install twitter
    pip install tweepy

## Run the spider to get the names

    cd spider
    scrapy runspider spider_names.py 

## Use case I: Estimating demographics from Twitter replies

Add the Twitter data of your account to a file called config.py. 


    con_secret = "..."
    con_secret_key = "..."
    token_key = "..."
    token = "..."


You have to create an app on https://apps.twitter.com to get all the tokens you need.

    cd twitter
    python ./read_recent_twitter_replies.py 

## Use case II: Estimating from Twitter followers

    cd twitter
    python ./read_followers_of_user.py 

## Analytics

You have to install ipython notebook (http://ipython.org/notebook.htmlpa) and Pandas (http://pandas.pydata.org/). Then you can start it with:

    ipython notebook basic_analytics.ipynb
