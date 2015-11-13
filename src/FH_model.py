import pymysql

#execute, then commit
class FH_dbmodel(object):
    def __init__(self):
        self.cnx = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_76",
            passwd="YlVIp1tI", db="cs4400_Group_76")
        #Assuming we have a view defined as:
        #CREATE VIEW users AS SELECT username, password FROM Customer UNION SELECT * FROM Management;
        self.queries = {"login" : "SELECT * FROM users WHERE ", "newcust" : "INSERT INTO Customer VALUE"}

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
        cursor = self.cnx.cursor()
        to_query = self.queries.get(query)
        to_query += "("
        for i in range(len(to_insert)-1):
            to_query += '"' + to_insert[i] + '",'
        to_query += '"' + to_insert[len(to_insert)-1] + '")'
        cursor.execute(to_query)
        self.cnx.commit()
        cursor.close()

    def get_data(self, query, to_get):
        cursor = self.cnx.cursor()
        to_query = self.queries.get(query)
        to_query += "("
        for i in range(len(to_insert)-1):
            to_query += '"' + to_insert[i] + '",'
        to_query += '"' + to_insert[len(to_insert)-1] + '")'
        cursor.execute(to_query)

    def del_data(self, query, to_get):
        pass
