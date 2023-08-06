from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:gVLAQSbfCuoKVQl0vvSL@containers-us-west-131.railway.app:5689/railway"

engine = create_engine(DATABASE_URL ,echo=False)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()
