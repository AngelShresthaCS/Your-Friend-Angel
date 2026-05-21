import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
# String Format = 'postgresql://<username>:<password>@<ip-addressorhostname>/<database_name>'
SQLALCHEMY_DATABASE_URL = (
	f"postgresql://{os.getenv('DBUSER')}:{os.getenv('MY_SECRET_PASSWORD')}@{os.getenv('HOST')}/{os.getenv('DATABASE')}"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)

Base = declarative_base()