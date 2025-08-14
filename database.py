from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

# Create database connection URL
DATABASE_URL = URL.create(
    drivername='postgresql+psycopg2',
    username='avnadmin',
    password='AVNS_v9SFYDrs9ynRR_7je8m',
    host='pg-2c2d487-backstract-5efe.f.aivencloud.com',
    port=17155,
    database='testdb'
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
