from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from tornado.options import define, options

define("mysql_uri", default="mysql://test:password@localhost/vimcanvas")

engine = create_engine(options.mysql_uri)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Model = declarative_base()
Model.query = db_session.query_property()

def init_db():
    import vimcanvas.models
    vimcanvas.models #shut up unused import warning
    Model.metadata.create_all(bind=engine)