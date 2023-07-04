#!/usr/bin/python3
import re
from WowApi import api
from WowApi.config import CONN_STRING
from WowApi.bnet import bnet

connected_realms = api.connected_realm_index().get()

for href in connected_realms.href:
    id = re.findall(r'\d+',href)[0]
    bnet.get(f"https://us.api.blizzard.com/data/wow/connected-realm/{id}/auctions?namespace=dynamic-us")

