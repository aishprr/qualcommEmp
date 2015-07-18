#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


#Variables that contains the user credentials to access Twitter API
access_token = "634989730-WSJJZQYAMw6Njbcj8g5MVbLMH2Agmvhkb0Xd1vbG"
access_token_secret = "jxmwpHWwvc4koQ0eJE40YjG3cEdXsPtpBiatkzD592Aa2"
consumer_key = "G7mOioDqoauCrelAe2OR1kEEN"
consumer_secret = "bDzLO3ABk53vVIdRcclliWZWw1jn08VS7Q76DaZxMkuAb76VfX"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print data
        return True
    
    def on_error(self, status):
        print status


if __name__ == '__main__':
    
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['#NCWIT', '#PT', '#QCSummit'])
    stream.filter(track=['#python'])
