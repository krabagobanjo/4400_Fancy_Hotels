import mysql.connector

class FH_dbmodel(object):
    def __init__(self):
        self.cnx = mysql.connector.connect(user="cs4400_Group_76", password="YlVIp1tI",
                host="academic-mysql.cc.gatech.edu", database="cs4400_Group_76")
        self.cursor = self.cnx.cursor()

    def close_connection(self):
        self.cnx.close()

    """Insert data into the database.
    Arguments:
        query - type of insertion query
        to_insert - list of data to insert
    Returns:
        error code (if any)
    """
    def insert_data(self, query, to_insert):
        pass

    def get_data(self, query, to_get):
        pass

    def del_data(self, query, to_get):
        pass
