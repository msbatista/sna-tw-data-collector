from sna_twitter.common.auth import TwitterAuth
from sna_twitter.stream.stream_handler import StreamHandler
from sna_twitter.stream.stream_listener import StreamListener

TRACK = ["covid", "covid-19", "covid19", "covid19brasil", "coronavirusbrasil", "Brasil", "coronavirus",
         "coronavirusbrasil"]


def main():
    auth = TwitterAuth().get_twitter_auth()
    listener = StreamListener(auth=auth, stream_handler=StreamHandler(), timeout=7 * 24 * 60 * 60)
    listener.stream_tweets(languages=["pt"], track=TRACK)


if __name__ == "__main__":
    main()
