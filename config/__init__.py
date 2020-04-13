""" Contains project paths """
import os

def getCredentials(): 
    """Get's environment variables containing database credentials

    Args: 
        None

    Return:
        dbCredentials: dictionary containing database credentials 

    """
    
    dbCredentials = {
            'DB_NAME' : os.getenv('DB_NAME'),
            'DB_USER' : os.getenv('DB_USER'),                
            'DB_PASSWORD' : os.getenv('DB_PASSWORD')
            }
    return dbCredentials

def getDatabaseURI():
    """Retrieves database URI

    Args:
        None

    Return:
        uri: Database URI

    """
    uri = os.getenv('INFO3180_PROJECT1_DATABASE_URL')
    return uri 

