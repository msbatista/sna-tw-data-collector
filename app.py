from sna_twitter.infrastructure.twitter.auth.twitter_auth_factory import TwitterAuthFactory
from sna_twitter.infrastructure.twitter.handler.stream_handler import StreamHandler
from sna_twitter.services.twitter_stream_listener_service import TwitterStreamListenerService

TRACK = ["covid", "covid-19", "covid19", "covid19brasil", "coronavirusbrasil", "Brasil", "coronavirus",
         "coronavirusbrasil"]


def main():
    auth = TwitterAuthFactory().get_twitter_auth()
    listener = TwitterStreamListenerService(auth=auth, stream_handler=StreamHandler(), timeout=7 * 24 * 60 * 60)
    listener.stream_tweets(languages=["pt"], track=TRACK)


if __name__ == "__main__":
    main()
