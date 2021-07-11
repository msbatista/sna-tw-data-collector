from sna_twitter.infrastructure.twitter.auth.twitter_auth_factory import TwitterAuthFactory
from sna_twitter.infrastructure.twitter.handler.stream_handler import StreamHandler
from sna_twitter.services.twitter_stream_listener_service import TwitterStreamListenerService
from sna_twitter.settings import Settings

TRACK = ["covid",
         "covid-19",
         "covid19",
         "covid19brasil",
         "coronavirusbrasil",
         "Brasil",
         "coronavirus",
         "coronavirusbrasil"]


def main():
    auth = TwitterAuthFactory(
        consumer_key=Settings.TWITTER_AUTH_KEYS["CONSUMER_KEY"],
        consumer_secret=Settings.TWITTER_AUTH_KEYS["CONSUMER_SECRET"],
        access_token=Settings.TWITTER_AUTH_KEYS["ACCESS_TOKEN"],
        access_token_secret=Settings.TWITTER_AUTH_KEYS["ACCESS_TOKEN_SECRET"]
    ).get_twitter_auth()

    listener = TwitterStreamListenerService(
        auth=auth,
        stream_handler=StreamHandler(),
        timeout=7 * 24 * 60 * 60
    )

    listener.stream_tweets(
        languages=["pt"],
        track_terms=TRACK
    )


if __name__ == "__main__":
    main()
