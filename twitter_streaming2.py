import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
 
access_token = "634989730-WSJJZQYAMw6Njbcj8g5MVbLMH2Agmvhkb0Xd1vbG"
access_secret = "jxmwpHWwvc4koQ0eJE40YjG3cEdXsPtpBiatkzD592Aa2"
consumer_key = "G7mOioDqoauCrelAe2OR1kEEN"
consumer_secret = "bDzLO3ABk53vVIdRcclliWZWw1jn08VS7Q76DaZxMkuAb76VfX"


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
  
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            # with open('python.json', 'a') as f:
            #     f.write(data + '\n\n')
            print data
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#NCWIT', '#PT', '#QCSummit'])
