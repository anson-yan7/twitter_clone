Route:
From the splash page, you can log in or sign up. After logging in or signing up, you arrive at home page where you see the tweets. There is a function to tweet, a function to like a tweet, a function to go to a profile page of an author of a tweet, a function to go to a hashtag page that includes all tweets with that hashtag, and a function to delete a tweet if you are owner of a tweet. In all pages except splash page, there is a log out button to sign out.


Design considerations: 
In profile page, it includes all tweets from that user.

For the tweet function, each tweet can have at most 280 chars. Tweet displays the name of the author, text of the tweet, date, and number of likes.

For the hashtag function, it supports only 1 hashtag per tweet. The hashtag must be in form ' #abcd' with space before # if # is not the first char. hashtag can have at most 140 chars

I combined the splash page and the login/signup page so my splash page does not look empty.

You can delete your tweet in any page if you are owner of the tweet. If this tweet is part of a hashtag group and after deleting the tweet, the hashtag group has no more tweet, the hashtag is also deleted when visiting home page.

How to run server:

Download the file and place it in whereever you desire. Open console or terminal. cd into the file. Run server by calling "python manage.py runserver". Use any browser and go to "localhost:8000".