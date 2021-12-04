from config import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_session():
    engine = f"postgresql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['db_name']}"
    engine = create_engine(engine)
    session = sessionmaker(bind = engine)()
    return session