# from decouple import config
# from sqlalchemy import MetaData, create_engine
# from sqlalchemy.orm import declarative_base
#
# metadata = MetaData()
# Base = declarative_base(metadata=metadata)
# engine = create_engine(config('DB_URI', default='sqlite:///api.db'))
# Base.metadata.create_all(engine, checkfirst=True)
# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
