""" Contains project paths """
import os
import json

# Root Dir
ROOTDIR = os.getenv('INFO3180_PROJECT1_ROOTDIR')  

def getCredentials(): 
    """Get's json of database credentials

    Args: 
        None

    Return:
        dbCredentials: Json object containing database credentials

    """

    dbCredentials = None

    if ROOTDIR == None: # Checks that ROOTDIR path is set
        print("Project path variable not set! Please Set first!")

    credentialsFile = os.path.join(ROOTDIR, "config", "database_credentials.json")

    with open(credentialsFile) as fptr: # Extracting json object 
        dbCredentials = json.load(fptr) 

    return dbCredentials


