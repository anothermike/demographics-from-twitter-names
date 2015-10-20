# Demographics from Twitter names

Install:

    pip install scrapy
		pip install twitter
		pip install tweepy

## Run the spider to get the names

    cd spider
		scrapy runspider spider_names.py 

## Use case I: Estimating demographics from Twitter replies

Add the Twitter data of your account. You have to create an app on https://apps.twitter.com to get all the tokens you need.

    cd twitter
		python ./read_recent_twitter_replies.py 

## Use case II: Estimating from Twitter followers

    cd twitter
		python ./read_followers_of_user.py 
