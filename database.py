from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://hillary:eGs2BuHMzFoIWBDrTQ3V1zia0m6yVmcn@dpg-cm090ida73kc73c2atmg-a.frankfurt-postgres.render.com/lecturehalls", echo =True)

localSession =sessionmaker(bind=engine)

def get_db():
    db =localSession()
    try:
        yield db
    finally:
        db.close()