import requests
import json
import logging
from urllib.parse import urljoin
from ratelimit import limits, sleep_and_retry
from .config import REGION, LOCALE, CLIENT_ID, CLIENT_SECRET
from .bnetcache import Cache

RATE_LIMITS = {'calls': 10, 'period': 1}


class Bnet(object):
    _access_token = None

    def __init__(self, credentials=(), region=None, locale=None):
        self.credentials = credentials or (CLIENT_ID, CLIENT_SECRET)
        self.region = region or REGION
        self.locale = locale or LOCALE

    @property
    def hostname(self):
        return f"https://{self.region}.api.blizzard.com"

    @property
    def access_token(self):
        if not self._access_token:
            url = f"https://{self.region}.battle.net/oauth/token"
            data = {'grant_type': 'client_credentials'}
            response = requests.post(url=url, data=data, auth=self.credentials)
            response.raise_for_status()
            self._access_token = response.json()['access_token']
        return self._access_token

    @ sleep_and_retry
    @ limits(**RATE_LIMITS)
    def get(self, href, namespace=None):
        if namespace is not None:
            href = urljoin(self.hostname, href) + \
                f"?namespace={namespace(self.region)}"
        print(href)
        params = {'region': self.region, 'locale': self.locale,
                  'access_token': self.access_token}
        with requests.get(url=href, params=params, stream=True) as response, Cache(href) as cache:
            if response.status_code == 200:
                cache.meta = dict(response.headers)
                cache.json = response.json
            else:
                logging.warn(
                    f"HTTP {response.status_code} {href} {response.reason}")
            return cache()


bnet = Bnet()
