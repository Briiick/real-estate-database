from create import *

# Add entries to the session
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# add to Sellers Table
session.add_all([
    Sellers(id = 1, firstname='John', lastname='Doe', email='jsmith@example.com', phone='704-129-4823'),
    Sellers(id = 2, firstname='Sally', lastname='Smith', email='sally@example.com', phone='707-234-0235'),
    Sellers(id = 3, firstname='Beth', lastname='Igloo', email='beth.i@example.com', phone='706-987-4864'),
    Sellers(id = 4, firstname='George', lastname='Paper', email='paperg@example.com', phone='704-598-1823'),
    Sellers(id = 5, firstname='Kim', lastname='Tree', email='kimtree@example.com', phone='703-493-0054')
])

# add to RealEstateAgents Table
session.add_all([
    RealEstateAgents(id = 1, firstname='Robert', lastname='Warren', email='RobertDWarren@telecom.us'),
    RealEstateAgents(id = 2, firstname='Vincent', lastname='Brown', email='VincentHBrown@rhyta.com'),
    RealEstateAgents(id = 3, firstname='Martina', lastname='Krushner', email='MartinaMKershner@rhyta.com'),
    RealEstateAgents(id = 4, firstname='Raoul', lastname='Baumgartender', email='Baum@raoul.com'),
    RealEstateAgents(id = 5, firstname='Morgan', lastname='Freeman', email='morgan@freeman.com')
])

# add to Offices Table
session.add_all([
    Offices(id = 1, region='Center'),
    Offices(id = 2, region='North'),
    Offices(id = 3, region='East'),
    Offices(id = 4, region='South'),
    Offices(id = 5, region='West')
])

# add to Houses Table
session.add_all([
    Houses(id=1, bedrooms=3, bathrooms=5, zipcode='30041', price=1250000.00, datelisted=date(2017,12,24), sellerid=1, agentid=1, officeid=1, sold=False),
    Houses(id=2, bedrooms=1, bathrooms=2, zipcode='30041', price=300000.00, datelisted=date(2018,3,22), sellerid=2, agentid=1, officeid=1, sold=False),
    Houses(id=3, bedrooms=4, bathrooms=1, zipcode='30041', price=720000.00, datelisted=date(2019,5,8), sellerid=3, agentid=1, officeid=1, sold=False),
    Houses(id=4, bedrooms=3, bathrooms=3, zipcode='30042', price=800000.00, datelisted=date(2019,4,17), sellerid=4, agentid=2, officeid=2, sold=False),
    Houses(id=5, bedrooms=2, bathrooms=2, zipcode='30042', price=1300000.00, datelisted=date(2019,9,19), sellerid=5, agentid=3, officeid=2, sold=False),
    Houses(id=6, bedrooms=2, bathrooms=4, zipcode='30042', price=1700000.00, datelisted=date(2018,4,3), sellerid=1, agentid=3, officeid=2, sold=False),
    Houses(id=7, bedrooms=5, bathrooms=6, zipcode='30042', price=4500000.00, datelisted=date(2018,7,5), sellerid=2, agentid=3, officeid=3, sold=False),
    Houses(id=8, bedrooms=10,bathrooms= 13, zipcode='30042', price=25000000.00, datelisted=date(2019,2,5), sellerid=3, agentid=1, officeid=2, sold=False),
    Houses(id=9, bedrooms=5, bathrooms=3, zipcode='30043', price=10250000.00, datelisted=date(2020,3,19), sellerid=4, agentid=5, officeid=5, sold=False),
    Houses(id=10, bedrooms=2, bathrooms=1, zipcode='30043', price=150000.00, datelisted=date(2019,4,12), sellerid=5, agentid=4, officeid=2, sold=False),
    Houses(id=11, bedrooms=1, bathrooms=0, zipcode='30043', price=90000.00, datelisted=date(2018,6,11), sellerid=1, agentid=5, officeid=3, sold=False),
    Houses(id=12, bedrooms=4, bathrooms=5, zipcode='30043', price=3000000.00, datelisted=date(2019,12,20), sellerid=2, agentid=4, officeid=4, sold=False),
    Houses(id=13, bedrooms=3, bathrooms=1, zipcode='30043', price=130000.00, datelisted=date(2018,2,27), sellerid=3, agentid=4, officeid=3, sold=False),
    Houses(id=14, bedrooms=4, bathrooms=7, zipcode='30043', price=5700000.00, datelisted=date(2020,1,30), sellerid=4, agentid=3, officeid=1, sold=False),
    Houses(id=15, bedrooms=3, bathrooms=1, zipcode='30043', price=250000.00, datelisted=date(2019,4,12), sellerid=5, agentid=1, officeid=3, sold=False),
    Houses(id=16, bedrooms=2, bathrooms=4, zipcode='30044', price=600000.00, datelisted=date(2019,10,2), sellerid=1, agentid=1, officeid=5, sold=False),
    Houses(id=17, bedrooms=9, bathrooms=4, zipcode='30044', price=1340000.00, datelisted=date(2018,11,15), sellerid=2, agentid=5, officeid=4, sold=False),
    Houses(id=18, bedrooms=1, bathrooms=1, zipcode='30044', price=500000.00, datelisted=date(2018,1,29), sellerid=3, agentid=4, officeid=4, sold=False),
    Houses(id=19, bedrooms=4, bathrooms=2, zipcode='30045', price=760000.00, datelisted=date(2019,3,21), sellerid=4, agentid=5, officeid=4, sold=False),
    Houses(id=20, bedrooms=4, bathrooms=4, zipcode='30045', price=5230000.00, datelisted=date(2020,2,13), sellerid=5, agentid=1, officeid=5, sold=False)
])

# add to Buyers Table
session.add_all([
    Buyers(id=1, firstname='Janet', lastname='Prettyman', email='janet@gmail.com'),
    Buyers(id=2, firstname='Harold', lastname='Grimes', email='grimeyharold@rhyta.com'),
    Buyers(id=3, firstname='Gregory', lastname='Fafa', email='gregthedog@applemail.com'),
    Buyers(id=4, firstname='Kelean', lastname='Dixie', email='Keeelean200@example.co.uk'),
    Buyers(id=5, firstname='Peter', lastname='Jungle', email='peter@oxford.edu'),
    Buyers(id=6, firstname='Jim', lastname='Yeti', email='jim@minerva.edu'),
    Buyers(id=7, firstname='Fred', lastname='Keiran', email='Freddie32@kk.com'),
    Buyers(id=8, firstname='Bob', lastname='Yasuo', email='yassbob@example.com'),
    Buyers(id=9, firstname='Kath', lastname='Akali', email='katherine@akali.co.uk'),
    Buyers(id=10, firstname='Nat', lastname='Heresay', email='Natalie@duke.edu'),
    Buyers(id=11, firstname='Sean', lastname='Bottle', email='Seanie@mghm.edu'),
    Buyers(id=12, firstname='Hugh', lastname='Slam', email='SlamH@google.com')
])

# commit to database
session.commit()
session.close()