from .config import CONN_STRING
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.orm import deferred, Session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime as dt

Base = declarative_base()
engine = sa.create_engine(CONN_STRING, echo=False)
session = Session(engine)


class Cache():
    def __init__(self, href):
        self.href = href
        self._meta = None
        self._json = {}
        self._json_lazy_evaluator = None

    def __enter__(self):
        self.session = session
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.commit()
        # self.session.close()

    def __call__(self):
        T = BnetCache
        data = (self.session.query(T)
                .filter(T.href == self.href, T.last_modified >= self.last_modified)
                .order_by(T.last_modified.desc())
                .first())
        if self.last_modified > dt.min and data is None:
            data = T(href=self.href, last_modified=self.last_modified,
                     meta=self.meta, json=self.json)
            self.session.add(data)
        if data is None:
            data = T(href=self.href, last_modified=dt.min, meta={}, json={})
        return data

    @property
    def last_modified(self):
        try:
            d = dt.strptime(dict.get(self.meta, 'Last-Modified'),
                            '%a, %d %b %Y %H:%M:%S %Z')
        except ValueError:
            d = dt.min
        return d

    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, obj):
        self._meta = obj

    @property
    def json(self):
        if self._json_lazy_evaluator is not None:
            self._json = self._json_lazy_evaluator()
            self._json_lazy_evaluator = None
        return self._json

    @json.setter
    def json(self, obj):
        if callable(obj):
            self._json_lazy_evaluator = obj
        else:
            self._json = obj


class BnetCache(Base):
    __tablename__ = 'bnet_cache'
    id = Column(Integer, primary_key=True, autoincrement=True)
    href = Column(String(255), index=True)
    last_modified = Column(DateTime, index=True)
    meta = deferred(Column(JSON))
    json = deferred(Column(JSON))


if __name__ == "__main__":
    import sqlalchemy
    from .config import CONN_STRING
    engine = sqlalchemy.create_engine(CONN_STRING, echo=True)
    #Base.metadata.drop_all(engine)
    #Base.metadata.create_all(engine)
