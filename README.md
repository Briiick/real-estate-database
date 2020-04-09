# Real Estate Database Webapp

This project was mainly coded in SQLAlchemy and uses fictitious data to emulate a real estate company relational database.

## To Run

Make sure `virtualenv` is installed

```bash
pip3 install virtualenv
```

Set up your virtual environment

```bash
virtualenv venv
source venv/bin/activate
```

Install requirements

```bash
pip3 install -r requirements.txt
```

And then run the following Python scripts in order:

1. create.py
2. insert_data.py
3. sell_houses.py
4. query_data.py

These should create the `realestate.db` database, insert data, simulate selling houses, and then query the data following the prompts below.

```bash
python3 create.py
python3 insert_data.py
python3 sell_houses.py
python3 query_data.py
```

## Files

```bash
./create.py
./insert_data.py
./sell_houses.py
./query_data.py
./README.md
./requirements.txt
```

## Details

The database, insertion of data, and the  queries have been written to satisfy features such as:


### Data Normalization

In the real estate database we have 8 tables.
    - Sellers
    - RealEstateAgents
    - Offices
    - Houses
    - Buyers
    - Sales
    - Profits
    - Summary

Most tables are populated using `insert_data.py`. However, using the additional `sell_houses.py` file we populate Sales, Profits, and Summary.

Data Normalization is used here to structure the relational database to reduce data redundancy, increase query time where possible, and improve the integrity of dependencies.

#### First Normal Form

This has been accomplished by making each table atomic. Each cell is single-valued. There are no repeating groups of columns and entries in any given column is of the same type as the other entries in that column. Finally, rows are uniquely identified using an ID.

#### Second Normal Form

First norm is satisfied, so we also satisfy second normal form upon making sure the columns of our relational database are dependent on the primary key of any given table. For example, Houses.id is used as the primary key for the Houses table.

#### Third Normal Form

First and second norms are satisfied, so we also satisfy third normal form by keeping all columns not transitively dependent. This means fields can only be accessed upon reference to their primary key. For example, Buyer firstname, lastname, and email could only be referenced through the Buyer.id.

#### Fourth Normal Form

First, second, and third norms are satisfied, so we also satisfy fourth normal form by having no multi-valued dependencies. For example, our Sales and Houses tables are separate so each Sale has a corresponding house. This maintains the one-to-one relationship present here.

### Indices

We know that SQLAlchemy, and as an extension, SQLite3, automatically maintains indices for improving query time of databases. By including `index=True` in my assignments of IDs in my tables, I set the position for SQLite3 to create efficient indices. I understood that this was the case and hence did not have to implement manual indexing.

The key concept for me to maintain efficient indexing was to have all my entries arranged in a well-defined order. Finding data in an ordered data set is fast and easy because the sort order determines each entry's position. Hence, I did this using primary key and foreign key constraints.


### Transactions

A transaction is a sequence of operations (in SQL) performed on a database as a single logical unit work. We know that a transaction must be:
    - Atomic: a logical unit of work which must be either completed with all of its data modifications, or none of them is performed.
    - Consistent: At the end of the transaction, all data must be left in a consistent state.
    - Isolated: Modifications of data performed by a transaction must be independent of another transaction. Unless this happens, the outcome of a transaction may be erroneous.
    - Durable: When the transaction is completed, effects of the modifications performed by the transaction must be permanent in the system & stored in non-volatile memory.

I made sure to implement ACID transactions by using the `sqlalchemy.orm sessionmaker` library. By using commands like `Session = sessionmaker(bind=engine)`, `session = Session()`, `session.commit()` and `session.close()` I was able to control transactions and cancel a session commit before closing if an error occurred.


### Other Features

- Organized Python scripts that are separated based on their respective utility.
- Ways of changing the month queried and checking if that month doesn't have any sales.
- Use of Pandas and Numpy to output the query results in nice formatting.
- Ability to re-run Python scripts to overwrite database instead of having to delete it every time.
- Separation of the `sell_houses.py` file.

## Queries

The queries written do the following:

1. Find the top 5 offices with the most sales for that month.
2. Find the top 5 estate agents who have sold the most (include their contact details and their sales details so that it is easy contact them and congratulate them).
3. Calculate the commission that each estate agent must receive and store the results in a separate table.
4. For all houses that were sold that month, calculate the average number of days that the house was on the market.
5. For all houses that were sold that month, calculate the average selling price.
6. Find the zip codes with the top 5 average sales prices.
