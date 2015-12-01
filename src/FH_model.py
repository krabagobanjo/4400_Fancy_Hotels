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
        "cust_login" : "SELECT * FROM Customer WHERE username='{L[0]}'",
        "newcust" : "INSERT INTO Customer VALUES({L[0]}, {L[1]}, {L[2]})",
        "mgmt_login" : "SELECT * FROM Management WHERE username='{L[0]}'",
        "find_rooms" : """SELECT L.roomnum AS 'Room Number', L.category, L.numpeople, L.cpday, X.bedcost FROM Room L INNER JOIN Extra_Bed X ON L.roomnum = X.Rroomnum AND L.location = X.Rlocation LEFT JOIN Reservation_Has_Room M ON L.roomnum = M.Hroomnum LEFT JOIN Reservation R ON M.HreservationID = R.reservationID WHERE(M.HreservationID IS NULL OR '{L[0]}' > R.end_date OR '{L[1]}') AND L.location = "{L[2]}" """,
        "find_cardnums" : "SELECT * FROM Payment_Info WHERE Pusername='{L[0]}'",
        "add_reserv_1" : "INSERT INTO Reservation VALUES({L[0]}, {L[1]}, {L[2]}, {L[3]}, {L[4]})",
        "add_reserv_2" : "INSERT INTO Reservation_Has_Room VALUES({L[0]}, {L[1]}, {L[2]})",
        "add_reserv_3" : "INSERT INTO Select_Extra_Bed VALUES({L[0]}, {L[1]}, {L[2]});",
        "get_last_reservID" : "SELECT LAST_INSERT_ID() AS reservationID",
        "get_reserv_by_id" : "SELECT start_date, end_date FROM Reservation WHERE reservationID={L[0]}",
        "add_cardnum" : "INSERT INTO Payment_Info VALUES({L[0]}, '{L[1]}', '{L[2]}', {L[3]}, '{L[4]}')",
        "delete_cardnum" : "DELETE FROM Payment_Info WHERE cardnum={L[0]}",
        "get_update_reserv" : """SELECT Hroomnum, category, numpeople, cpday FROM Reservation R INNER JOIN Reservation_Has_Room H ON R.reservationID=H.HreservationID INNER JOIN Room M ON M.roomnum=H.Hroomnum WHERE R.reservationID<>{L[0]} AND M.roomnum in (SELECT M.roomnum FROM Reservation R INNER JOIN Reservation_Has_Room H ON R.reservationID=H.HreservationID INNER JOIN Room M ON M.roomnum = H.Hroomnum WHERE R.reservationID={L[0]}) AND ('{L[1]}' > R.end_date OR '{L[2]}' < R.start_date) """,
        "update_reserv" : """UPDATE Reservation SET start_date='{L[0]}', end_date='{L[1]}' WHERE reservationID='{L[2]}' """,
        "get_cancel_reserv" : "SELECT * FROM Reservation R INNER JOIN Reservation_Has_Room H ON R.reservationID=H.HreservationID INNER JOIN Room M ON M.roomnum=H.Hroomnum WHERE R.reservationID={L[0]}",
        "cancel_reserv_1" : """DELETE FROM Reservation WHERE reservationID='{L[0]}' """,
        "cancel_reserv_2" : """DELETE FROM Reservation_Has_Room WHERE HreservationID='{L[0]}' """,
        "get_reviews" : "SELECT rating, comment FROM Review WHERE location='{L[0]}' ORDER BY rating",
        "give_review" : "INSERT INTO Review VALUES({L[0]}, {L[1]})",
        "get_reserv_report" : """DROP VIEW myview; CREATE VIEW myview AS SELECT DISTINCT reservationID, DATE(start_date) as Month, hlocation FROM Reservation NATURAL JOIN Reservation_Has_Room WHERE cancelled = 0; SELECT *, count(*) from myview GROUP BY Month, hlocation;""",
        "get_rev_report" : """DROP VIEW brisview; CREATE VIEW brisview as SELECT SUM(tot_cost), DATE(start_date) as Month, hlocation FROM Reservation NATURAL JOIN Reservation_Has_Room WHERE cancelled = 0; SELECT *, count(*) from brisview GROUP BY Month, hlocation;"""

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
        if len(to_insert) > 0:
            to_query = to_query.format(L=to_insert)
            cursor.execute(to_query)
            self.cnx.commit()
            cursor.close()
        else:
            cursor.close()
            raise ValueError

    def get_data(self, query, to_get=None):
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
            print(to_query)
            cursor.execute(to_query)
            self.cnx.commit()
            results = list(cursor.fetchall())
            cursor.close()
            return results

    def del_data(self, query, to_del):
        cursor = self.cnx.cursor()
        to_query = self.queries.get(query)
        if len(to_del) > 0:
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
        if len(to_update) > 0:
            to_query = to_query.format(L=to_update)
            cursor.execute(to_query)
            self.cnx.commit()
            cursor.close()
        else:
            cursor.close()
            raise ValueError
