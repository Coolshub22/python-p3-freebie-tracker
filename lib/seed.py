#!/usr/bin/env python3

# Script goes here!
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Company, Dev, Freebie

# Create engine and session
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Clear old data and recreate tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create new companies
c1 = Company(name="CodeCraft", founding_year=2010)
c2 = Company(name="BugSquashers Inc.", founding_year=2005)

# Create new developers
d1 = Dev(name="Charlie")
d2 = Dev(name="Dana")

# Create new freebies
f1 = Freebie(item_name="USB Drive", value=12, dev=d1, company=c1)
f2 = Freebie(item_name="Notebook", value=5, dev=d1, company=c2)
f3 = Freebie(item_name="Coffee Mug", value=8, dev=d2, company=c1)
f4 = Freebie(item_name="Hoodie", value=25, dev=d2, company=c2)

# Add all to the session and commit
session.add_all([c1, c2, d1, d2, f1, f2, f3, f4])
session.commit()
