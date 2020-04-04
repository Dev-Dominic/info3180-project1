#!/usr/bin/python

import os
import psycopg2
import json

def setup(): 
    """Setups project database 

    Creates database and special user associated with database.
    Make connnection to default postgres database to create 
    project database.

    Args: 
        None

    Returns: 
        None

    """

    # Getting path of config folder 
    # Collection of database credentials from file

    ROOTDIR = os.getenv('INFO3180_PROJECT1_ROOTDIR')  
    credentialsFile = os.path.join(ROOTDIR, "config", "database_credentials.json")

    with open(credentialsFile) as fptr:
        db = json.load(fptr) 

    conn = psycopg2.connect(
        user="postgres",
        password="password"
    ) # Connecting to database  

    with conn: 
        # TODO explain this
        autocommit = psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
        conn.set_isolation_level(autocommit)

        cur = conn.cursor()

        try:
            cur.execute(f'DROP DATABASE IF EXISTS "{db["DB_NAME"]}" ')  
            cur.execute(f'CREATE DATABASE "{db["DB_NAME"]}" ')


            cur.execute(f'DROP USER IF EXISTS "{db["DB_USER"]}" ')
            cur.execute(f"CREATE USER {db['DB_USER']} WITH PASSWORD '{db['DB_PASSWORD']}' ")

            cur.execute(f'GRANT ALL PRIVILEGES ON DATABASE "{db["DB_NAME"]}" to "{db["DB_USER"]}" ')

            conn.commit()  
        except e:
            print(f"An Error occured during setup: {e}")
    
if __name__ == "__main__":
    setup()


