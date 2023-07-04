
import functools as ft
from operator import getitem
from .bnet import bnet
import pandas as pd


def endpoint(namespace=None, *, schema=None, index=None):
    options = locals()

    def _endpoint(template):
        @ft.wraps(template)
        def wrapper(**parameters):
            return Endpoint(template, parameters, **options)
        return wrapper
    return _endpoint


class Endpoint(object):
    def __init__(self, template, parameters, *, namespace=None,  schema=None, index=None):
        self.parameters = parameters
        self.href = template(**parameters)
        self.namespace = namespace
        self.schema = schema
        self.index = index

    def __repr__(self):
        return self.href

    @property
    def cached(self):
        return self

    def get(self):
        data = bnet.get(self.href, self.namespace)
        df = (pd.json_normalize(data.json, record_path=self.index, sep="_")
              .assign(last_modified=data.last_modified, **self.parameters))
        return df
