from create import *
from insert_data import *
from sell_houses import *

# set pandas float output to 2 decimal places
pd.options.display.float_format = '{:.2f}'.format

# change month here
month = 12
monthname = 'December'

# 1. Find the top 5 offices with the most sales for that month.
print("------------------------------------------")
print(f"Top 5 offices with the most sales for {monthname}.")
# we are going to check december, the 12th month of the year.
top_five = session.query(Sales.officeid, func.sum(Sales.finalprice), 
            func.extract('month', Sales.selldate)).group_by(Sales.officeid)\
                .order_by(func.sum(Sales.finalprice).desc()).filter(func.extract('month', Sales.selldate) == month).limit(5).statement

# convert into pandas table for readability
top_five = pd.read_sql(top_five, session.bind)
top_five.columns=['Office', 'Sales', 'Month']
print(top_five)

# to output without pandas:
# for row in top_five:
#   print(row)

# 2. Find the top 5 estate agents who have sold the most (include their contact details and their sales details so that it is easy contact them and congratulate them).

# find firstname, lastname, email
print("------------------------------------------")
print("Top 5 estate agents who have sold the most:")
top_five_agents = session.query(RealEstateAgents.firstname, RealEstateAgents.lastname, RealEstateAgents.email, func.sum(Sales.finalprice)).join(Sales, and_(RealEstateAgents.id == Sales.agentid))\
                    .group_by(RealEstateAgents.firstname).order_by(func.sum(Sales.finalprice).desc()).limit(5).statement

top_five_agents = pd.read_sql(top_five_agents, session.bind)
top_five_agents.columns=['First Name', 'Last Name', 'Email', 'Total Sales']
print(top_five_agents)



# 3. Calculate the commission that each estate agent must receive and store the results in a separate table.

print("------------------------------------------")
print("Top 5 estate agent commissions:")
top_five_commission = session.query(RealEstateAgents.firstname, RealEstateAgents.lastname, func.sum(Profits.commission)).join(Profits, and_(RealEstateAgents.id == Profits.agentid))\
                    .group_by(RealEstateAgents.firstname).order_by(func.sum(Profits.commission).desc()).limit(5).statement

top_five_commission = pd.read_sql(top_five_commission, session.bind)
top_five_commission.columns=['First Name', 'Last Name', 'Total Commission']
print(top_five_commission)



# 4. For all houses that were sold that month, calculate the average number of days that the house was on the market.

# We find the avg number of days that houses sold in December were on market.

print("------------------------------------------")
print(f"Houses sold in {monthname}:")
houses_sold_dates = session.query(Houses.id, Houses.datelisted, Sales.selldate).join(Houses, and_(Sales.houseid == Houses.id))\
                    .filter(func.extract('month', Sales.selldate) == month).statement

# show all houses sold in december for perspective
houses_sold_dates = pd.read_sql(houses_sold_dates, session.bind, parse_dates=[Houses.datelisted, Sales.selldate])
houses_sold_dates.columns=['House ID', 'Date Listed', 'Date Sold']
print(houses_sold_dates)

houses_sold_dates = session.query(Houses.datelisted, Sales.selldate).join(Houses, and_(Sales.houseid == Houses.id))\
                    .filter(func.extract('month', Sales.selldate) == month).all()

if len(houses_sold_dates) >= 1:
    # houses sold and calculate difference between sell date and listing date
    temp = []
    for day in houses_sold_dates:
        temp.append(day[1]-day[0])
    average_days = np.mean(temp).days
    print(f'Average days on market: {average_days}')
else:
    # no houses sold that month
    print('There were no houses sold that month!')



# 5. For all houses that were sold that month, calculate the average selling price
print("------------------------------------------")
print(f"Houses sold in {monthname}:")
houses_sold = session.query(Houses.id, Sales.finalprice, Sales.selldate).join(Houses, and_(Sales.houseid == Houses.id))\
                .order_by(Sales.finalprice).filter(func.extract('month', Sales.selldate) == month).statement

# convert into pandas table for readability and output all prices for houses sold in december
houses_sold = pd.read_sql(houses_sold, session.bind)
houses_sold.columns=['House ID', 'Final Sale Price', 'Date Sold']
print(houses_sold)

houses_sold = session.query(Houses.id, Sales.finalprice).join(Houses, and_(Sales.houseid == Houses.id))\
                .order_by(Sales.finalprice).filter(func.extract('month', Sales.selldate) == month).all()

# calculate average house sell price of houses sold in that month
if len(houses_sold) >= 1:
    temp = []
    for house in houses_sold:
        temp.append(house[1])
    average_price = np.mean(temp)
    print(f'Average selling price: {average_price}')
else:
    print('There were no houses sold that month!')



# 6. Find the zip codes with the top 5 average sales prices

print("------------------------------------------")
print(f"Zip codes with top 5 average sales prices:")
top_zip_codes = session.query(Houses.zipcode, func.avg(Houses.price))\
    .group_by(Houses.zipcode).order_by(func.avg(Houses.price).desc()).limit(5).statement

top_zip_codes = pd.read_sql(top_zip_codes, session.bind)
top_zip_codes.columns=['Zip Code', 'Average Sales Price']
print(top_zip_codes)

# close session
session.close()