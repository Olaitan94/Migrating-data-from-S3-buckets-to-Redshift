import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

# This file contains commands for establishing connections to the warehouse, loading data into staging tables and inserting data from staging tables into the dimensional tables

def load_staging_tables(cur, conn):
    """
    This function iterates over list of queries in copy_table_queries. The queries transfer the data from the S3 
    buckets to the stage tables via 'COPY'. 
    """
    
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    This function iterates over list of queries in insert_table_queries. This moves data from the 
    staging tables to the final tables.
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():

    """
    This function reads credentials from the config file, establish connection with the warehouse and calls the load and insert functions.
    """
    config = configparser.ConfigParser()
    config.read('aws_cred.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
