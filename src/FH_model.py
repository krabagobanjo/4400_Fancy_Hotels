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
        "cust_login" : "SELECT * FROM Customer WHERE username={L[0]}",
        "newcust" : "INSERT INTO Customer VALUES({L[0]})",
        "mgmt_login" : "SELECT * FROM Management WHERE username={L[0]}",
        "find_rooms" : """SELECT L.roomnum AS 'Room Number', L.category, L.numpeople, L.cpday, X.bedcost FROM Room L INNER JOIN Extra_Bed X ON L.roomnum = X.Rroomnum AND L.location = X.Rlocation LEFT JOIN Reservation_Has_Room M ON L.roomnum = M.Hroomnum LEFT JOIN Reservation R ON M.HreservationID = R.reservationID WHERE(M.HreservationID IS NULL OR '{L[0]}' > R.end_date OR '{L[1]}') AND L.location = "{L[2]}" """,
        "find_cardnums" : "SELECT * FROM 'Payment_Info' WHERE name={L[0]}",
        "add_reserv_1" : "INSERT INTO Reservation VALUES({L[0]})",
        "add_reserv_2" : "INSERT INTO Reservation_Has_Room VALUES({L[0]})",
        "get_reservID" : "SELECT LAST_INSERT_ID() AS reservationID",
        "add_cardnum" : "INSERT INTO Payment_Info VALUES({L[0]})",
        "delete_cardnum" : "DELETE FROM Payment_Info WHERE {L[0]}",
        "confirm_rooms" : """SELECT * FROM Reservation R INNER JOIN Reservation_Has_Room H ON R.reservationID=H.HreservationID INNER JOIN Room M ON M.roomnm=H.Hroomnum WHERE {L[0]} in (SELECT M.roomnum FROM Reservation R INNER JOIN Reservation_Has_Room H ON R.reservationID=H.HreservationID INNER JOIN Room M ON M.roomnum = H.Hroomnum WHERE R.reservationID={L[1]}) AND ('{L[2]}' > R.end_date OR '{L[3]}' < R.start_date) """,
        "update_reserv" : """UPDATE Reservation SET start_date='{L[0]}', end_date='{L[1]}' WHERE reservationID='{L[1]}' """,
        "cancel_reserv_1" : """DELETE FROM Reservation WHERE reservationID='{L[0]}' """,
        "cancel_reserv_2" : """DELETE FROM Reservation_Has_Room WHERE HreservationID='{L[0]}' """,
        "get_reviews" : "SELECT rating, comment FROM Review ORDER BY rating",
        "give_review" : "INSERT INTO Review VALUES({L[0]})"
        }

    def close_connection(self):
        self.cnx.close()

    def insert_data(self, query, to_insert):
        """Insert data into the database.
        Arguments:
            query - type of insertion query
            to_insert - list of data to insert
        Returns:
            error code (if any)
        """
        cursor = self.cnx.cursor()
        to_query = self.queries.get(query)
        if to_insert:
            to_query = to_query.format(L=to_insert)
            cursor.execute(to_query)
            self.cnx.commit()
            cursor.close()
        else:
            cursor.close()
            raise ValueError

    def get_data(self, query, to_get):
        cursor = self.cnx.cursor()
        to_query = self.queries.get(query)
        if to_get:
            to_query = to_query.format(L=to_get)
            print(to_query)
            cursor.execute(to_query)
            self.cnx.commit()
            results = list(cursor.fetchall())
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

    def update_data(self, query, to_update):
        cursor = self.cnx.cursor()
        to_query = self.queries.get(query)
        if to_update:
            to_query = to_query.format(L=to_update)
            cursor.execute(to_query)
            self.cnx.commit()
            cursor.close()
        else:
            cursor.close()
            raise ValueError
