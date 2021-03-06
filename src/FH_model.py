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
        "newcust" : "INSERT INTO Customer VALUES('{L[0]}', '{L[1]}', '{L[2]}')",
        "mgmt_login" : "SELECT * FROM Management WHERE username='{L[0]}'",
        "find_rooms" : """SELECT L.roomnum AS 'Room Number', L.category, L.numpeople, L.cpday, X.bedcost FROM Room L INNER JOIN Extra_Bed X ON L.roomnum = X.Rroomnum AND L.location = X.Rlocation LEFT JOIN Reservation_Has_Room M ON L.roomnum = M.Hroomnum LEFT JOIN Reservation R ON M.HreservationID = R.reservationID WHERE(M.HreservationID IS NULL OR '{L[0]}' > R.end_date OR '{L[1]}') AND L.location = "{L[2]}" GROUP BY roomnum, category, numpeople, cpday, bedcost """,
        "find_cardnums" : "SELECT * FROM Payment_Info WHERE Pusername='{L[0]}'",
        "add_reserv_1" : "INSERT INTO Reservation(start_date, end_date, tot_cost, Rcardnum, Rusername) VALUES('{L[0]}', '{L[1]}', '{L[2]}', '{L[3]}', '{L[4]}')",
        "add_reserv_2" : "INSERT INTO Reservation_Has_Room VALUES('{L[0]}', '{L[1]}', '{L[2]}')",
        "add_reserv_3" : "INSERT INTO Select_Extra_Bed VALUES('{L[0]}', '{L[1]}', '{L[2]}');",
        "get_last_reservID" : "SELECT LAST_INSERT_ID() AS reservationID",
        "get_reserv_by_id" : "SELECT start_date, end_date FROM Reservation WHERE reservationID={L[0]} and Rusername='{L[1]}' and cancelled=0",
        "add_cardnum" : "INSERT INTO Payment_Info VALUES('{L[0]}', '{L[1]}', '{L[2]}', '{L[3]}', '{L[4]}')",
        "delete_cardnum" : "DELETE FROM Payment_Info WHERE cardnum='{L[0]}'",
        "get_update_reserv" : """SELECT Hroomnum, category, numpeople, cpday FROM Reservation R INNER JOIN Reservation_Has_Room H ON R.reservationID=H.HreservationID INNER JOIN Room M ON M.roomnum=H.Hroomnum WHERE R.reservationID<>{L[0]} AND M.roomnum in (SELECT M.roomnum FROM Reservation R INNER JOIN Reservation_Has_Room H ON R.reservationID=H.HreservationID INNER JOIN Room M ON M.roomnum = H.Hroomnum WHERE R.reservationID={L[0]}) AND ('{L[1]}' > R.end_date OR '{L[2]}' < R.start_date) R.Rusername='{L[3]}' AND cancelled=0 """,
        "update_reserv" : """UPDATE Reservation SET start_date='{L[0]}', end_date='{L[1]}', tot_cost='{L[3]}' WHERE reservationID='{L[2]}' """,

        "get_cancel_reserv" : "SELECT * FROM Reservation R INNER JOIN Reservation_Has_Room H ON R.reservationID=H.HreservationID INNER JOIN Room M ON M.roomnum=H.Hroomnum AND M.location=H.Hlocation LEFT JOIN Select_Extra_Bed G ON R.ReservationID=G.SreservationID WHERE R.reservationID={L[0]} and cancelled=0",
        "cancel_reserv_1" : """DELETE FROM Reservation WHERE reservationID='{L[0]}' """,
        "cancel_reserv_2" : """DELETE FROM Reservation_Has_Room WHERE HreservationID='{L[0]}' """,
        "cancel_reservation" : "UPDATE Reservation SET Reservation.cancelled=1 WHERE Reservation.reservationID={L[0]} AND cancelled=0",
        "get_reviews" : "SELECT rating, comment FROM Review WHERE location='{L[0]}' ORDER BY rating",
        "reserv_report_view_update" : """DROP VIEW myview; CREATE VIEW myview AS SELECT reservationID, start_date, hlocation FROM Reservation JOIN Reservation_Has_Room on reservationID = HreservationID WHERE cancelled = 0 ORDER BY start_date;""",
        "get_reserv_report":"""SELECT MONTHNAME(start_date), hlocation, count(*) from myview GROUP BY start_date, hlocation ORDER BY start_date;""",
        "pop_report_view_update": """DROP VIEW popularview;CREATE VIEW popularview
        AS SELECT * FROM Room;

        DROP VIEW popularview_two;
        CREATE VIEW popularview_two AS
        SELECT * FROM Reservation as r JOIN Reservation_Has_Room as c ON r.reservationID = c.HreservationID;

        DROP VIEW popularview_three;
        CREATE VIEW popularview_three AS
        SELECT * FROM popularview as s JOIN popularview_two as d ON s.roomnum = d.Hroomnum and s.location = d.Hlocation;

        DROP VIEW popularview_four;
        CREATE VIEW popularview_four AS
        SELECT MONTHNAME(start_date) as Month, category, location, count(*) as reservations  FROM popularview_three GROUP BY category, Location, Month ORDER BY start_date; """,
        "get_pop_report":"""SELECT * FROM popularview_four as s
        WHERE s.reservations = (
        SELECT MAX(s2.reservations) from popularview_four as s2
        WHERE s.Month = s2.Month AND s.location = s2.location );""",
        "give_review" : "INSERT INTO Review (rating,location,comment,Rusername) VALUES('{L[0]}', '{L[1]}', '{L[2]}', '{L[3]}')",

        "rev_report_view_update": """ DROP view brisview; CREATE VIEW brisview AS SELECT tot_cost, start_date, hlocation FROM Reservation JOIN Reservation_Has_Room on reservationID = HreservationID WHERE cancelled = 0 ORDER BY start_date;""",
        "get_rev_report" : """SELECT MONTHNAME(start_date), hlocation, SUM(tot_cost) from brisview GROUP BY start_date, hlocation ORDER BY start_date;""",

        "update_reserv_view_update":"""DROP VIEW update_reservation_one;
        CREATE VIEW update_reservation_one AS
        SELECT * FROM Reservation R
        INNER JOIN
        Reservation_Has_Room H
        ON R.reservationID=H.HreservationID;
        DROP VIEW update_reservation_two;
        CREATE VIEW update_reservation_two AS
        SELECT * FROM Room M
        INNER JOIN
        Extra_Bed P
        ON M.roomnum = P.Rroomnum and M.location = P.Rlocation;
        DROP VIEW update_reservation_three;
        CREATE VIEW update_reservation_three AS
        SELECT * FROM update_reservation_two t2
        LEFT JOIN
        update_reservation_one t1
        ON t1.Hroomnum = t2.roomnum and t1.Hlocation = t2.location;

        DROP VIEW update_reservation_three_half;
        CREATE VIEW update_reservation_three_half AS
        SELECT * FROM update_reservation_three t1
        LEFT JOIN
        Select_Extra_Bed t2
        ON t1.reservationID = t2.SreservationID;


        DROP VIEW update_reservation_four;""",

        "update_reserv_view_update_two":"""CREATE VIEW update_reservation_four AS
        SELECT roomnum, location FROM update_reservation_three_half t1
        WHERE start_date > {L[0]} AND end_date < {L[1]} OR start_date < {L[0]} AND end_date > {L[1]} OR start_date > {L[0]} AND start_date < {L[1]} AND end_date > {L[1]} OR start_date < {L[0]} AND end_date > {L[0]} AND end_date < {L[1]};""",

        "update_reserv_view_update_three":"""DROP VIEW update_reservation_five;
        CREATE VIEW update_reservation_five AS
        SELECT * FROM update_reservation_three_half t1
        WHERE NOT EXISTS (SELECT 1 FROM update_reservation_four t2 WHERE t1.roomnum = t2.roomnum AND t1.location = t2.location);""",

        "update_reserv_view_update_four":"""SELECT * FROM update_reservation_five WHERE reservationID='{L[0]}' and Rusername='{L[1]}'""",



        }

    def close_connection(self):
        self.cnx.close()

    def mult_queries(self,query):
        cursor = self.cnx.cursor()
        to_query = self.queries.get(query)
        statements = to_query.split(";")
        for i in range (len(statements)-1):
            print(statements[i])
            cursor.execute(statements[i] + ";")
        self.cnx.commit()
        cursor.close

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
