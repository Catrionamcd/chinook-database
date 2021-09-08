from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Country" table
class Country(base):
    __tablename__ = "Country"
    id = Column(Integer, primary_key=True)
    country_name = Column(String)
    capital = Column(String)
    population = Column(Integer)
    language = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on a Country table
ireland = Country(
    country_name="Ireland",
    capital="Dublin",
    population=5002851,
    language="English",
)


france = Country(
    country_name="France",
    capital="Paris",
    population=65273511,
    language="French",
)

germany = Country(
    country_name="Germany",
    capital="Berlin",
    population=83783942,
    language="German",
)

spain = Country(
    country_name="Spain",
    capital="Madrid",
    population=46754778,
    language="Spanish",
)

uk = Country(
    country_name="UK",
    capital="London",
    population=67886011,
    language="English",

)

# add each instance of each country to our session
# session.add(ireland)
# session.add(france)
# session.add(germany)
# session.add(spain)
# session.add(uk)

# updating a single record
# country = session.query(Country).filter_by(id=1).first()
# country.language = "Irish"

# commit our session to the database
# session.commit()

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()


# deleting a single record
cname = input("Enter a Country Name: ")
country = session.query(Country).filter_by(country_name=cname).first()
# defensive programming
if country is not None:
    print("Country Found: ", country.country_name)
    confirmation = input("Are you sure you want to delete this record? (y/n) ")
    if confirmation.lower() == "y":
        session.delete(country)
        session.commit()
        print("Country has been deleted") 
    else:
        print("Country not deleted")
else:
    print("No records found")

# query the database to find all Countries
countries = session.query(Country)
for country in countries:
    print(
        country.id,
        country.country_name,
        country.capital,
        country.population,
        country.language,
        sep=" | "
    )
