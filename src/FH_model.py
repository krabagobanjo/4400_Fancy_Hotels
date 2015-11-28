import pymysql
import json

# mysql login info
# username: cs4400_Group_76
# password: YlVIp1tI
# https://academic-mysql.cc.gatech.edu/phpmyadmin/

#execute, then commit

class FH_dbmodel(object):
    def __init__(self):
        self.cnx = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_76",
            passwd="YlVIp1tI", db="cs4400_Group_76")
        self.queries = {
        "cust_login" : "SELECT * FROM Customer WHERE {L[0]}",
        "newcust" : "INSERT INTO Customer VALUES({L[0]})",
        "mgmt_login" : "SELECT * FROM Management WHERE {L[0]}"
        "find_rooms" : "SELECT L.roomnum AS 'Room Number', L.category, L.numpeople, L.cpday, X.bedcost FROM Room L INNER JOIN Extra_Bed X ON L.roomnum = X.Roomnum AND L.location = X.Rlocation LEFT JOIN Reservation_Has_Room M ON L.roomnum = M.Hroomnum LEFT JOIN Reservation R ON M.HreservationID = R.reservationID WHERE {L[0]}"
        "find_cardnums" : "SELECT * FROM 'Payment_Info' WHERE {L[0]}"
        "add_reserv_1" : "INSERT INTO Reservation VALUES({L[0]})"
        "add_reserv_2" : "INSERT INTO Reservation_Has_Room VALUES({L[0]})"
        "add_cardnum" : "INSERT INTO Payment_Info VALUES({L[0]})"
        "delete_cardnum" : "DELETE FROM Payment_Info WHERE {L[0]}"
        "find_avail_rooms" : "SELECT * FROM Reservation R INNER JOIN Reservation_Has_Room H ON R.reservationID=H.HreservationID INNER JOIN Room M ON M.roomnm=H.Hroomnum WHERE {L[0]} in (SELECT M.roomnum FROM Reservation R INNER JOIN Reservation_Has_Room H ON R.reservationID=H.HreservationID INNER JOIN Room M ON M.roomnum = H.Hroomnum WHERE {L[1]})"
        }

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
        to_query = to_query.format(L=to_insert)
        cursor.execute(to_query)
        self.cnx.commit()
        cursor.close()

    def get_data(self, query, to_get):
        cursor = self.cnx.cursor()
        to_query = self.queries.get(query)
        if to_get:
            to_query = to_query.format(L=to_get)
            cursor.execute(to_query)
            results = cursor.fetchall()
            cursor.close()
            return results
        else:
            cursor.close()
            raise ValueError

    def del_data(self, query, to_del):
        cursor = self.cnx.cursor()
        to_query = self.queries.get(query)
        if to_del:
            to_query = to_query.format(L=to_del)
            cursor.execute(to_query)
            self.cnx.commit()
            cursor.close()
        else:
            cursor.close()
            raise ValueError
