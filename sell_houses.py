from create import *
from insert_data import *

session.commit()

###################################################################
# Update the status of some houses being sold from False to True.
# Add a corresponding entry to the sales table
# Calculate commission and add to profit table.
# finalise sales in Summary Table.
###################################################################

# create a function that allows mulitple selling of houses
def house_selling(i, houseid, selldate, finalprice, buyerid):
    
    # Update the status of inputted houses being sold from False to True.
    session.query(Houses).filter(Houses.id == houseid).update({Houses.sold: True})

    agentid = session.query(Houses.agentid).filter(Houses.id == houseid)
    officeid = session.query(Houses.officeid).filter(Houses.id == houseid)

    # Add a corresponding entry to the sales table
    session.add(
        Sales(id = i, selldate = selldate, finalprice = finalprice,
        houseid = houseid, buyerid = buyerid, officeid = officeid, agentid = agentid)
        )
    
    # Calculate commission and add to Profits table.

    if finalprice < 100000:
        comms = finalprice * 0.1
    elif finalprice >= 100000 and finalprice < 200000:
        comms = finalprice * 0.075
    elif finalprice >= 200000 and finalprice < 500000:
        comms = finalprice * 0.06
    elif finalprice >= 500000 and finalprice < 1000000:
        comms = finalprice * 0.05
    else:
        comms = finalprice * 0.04

    session.add(
        Profits(id = i, saleid = i, commission = comms, agentid = agentid)
        )

# houses to be sold
sold_house_data = [
    [1, 1, date(2018,2,13), 1300000.00, 1],
    [2, 3, date(2019,12,10), 800000.00, 2],
    [3, 4, date(2020,1,5), 900000.00, 3],
    [4, 5, date(2019,12,5), 1200000.00, 4],
    [5, 7, date(2018,12,3), 6500000.00, 5],
    [6, 10, date(2019,5,2), 150000.00, 6],
    [7, 11, date(2018,6,29), 110000.00, 7],
    [8, 12, date(2019,12,30), 3500000.00, 8],
    [9, 14, date(2020,3,21), 7350000.00, 9],
    [10, 16, date(2019,12,25), 645000.00, 10],
    [11, 19, date(2020,1,17), 1000000.00, 11],
    [12, 20, date(2020,4,6), 5020000.00, 12]
]

# iterate through data, selling houses
for house in sold_house_data:
    house_selling(*house)

# Fill in Summary Table
sumofsales = session.query(func.sum(Sales.finalprice))
totalcommission = session.query(func.sum(Profits.commission))
session.add(
        Summary(id = 1, sumofsales = sumofsales, totalcommission = totalcommission)
        )

# commit and close session
session.commit()
session.close()