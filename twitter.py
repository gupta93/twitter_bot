#Import the necessary methods from tweepy library

from tweepy.streaming import StreamListener
from tweepy import Stream
import time,queue
from tweepy import OAuthHandler
from config import consumer_secret, consumer_key, access_token, access_token_secret

class StdOutListener(StreamListener):

    def on_data(self, data):
        channel.basic_publish(exchange='', routing_key='twitter', body=data)
        return True

    def on_error(self, status):
        print status
        return True

    def on_exception(self, exception):
        return True

    def on_disconnect(self, notice):
        return True

    def on_timeout(self):
        print "timeout"
        return True  # To continue listening



if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    channel = queue.channel
    print "Starting .."
    while True:
        try:
            stream.sample()
        except Exception,e:
            print str(e)
            print 'sleeping'
            time.sleep(10)

