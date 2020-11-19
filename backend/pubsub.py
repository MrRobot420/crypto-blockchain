import time
from typing import List
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

subscribe_key = "sub-c-a830ad62-2aaa-11eb-9d95-7ab25c099cb1"
publish_key = "pub-c-c6c3062a-383d-4305-b0af-ed22ec1fe0c9"

pnconfig = PNConfiguration()
pnconfig.publish_key = publish_key
pnconfig.subscribe_key = subscribe_key

pubnub = PubNub(pnconfig)


TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()


class Listener(SubscribeCallback):

    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message_object: {message_object}')
        

pubnub.add_listener(Listener())


def main():
    time.sleep(1)
    pubnub.publish().channel(TEST_CHANNEL).message({ 'foo': 'bar' }).sync()


if __name__ == "__main__":
    main()