CREATE TABLE Management (
    username  varchar(25)  NOT NULL,
    password  varchar(25)  NOT NULL,
    PRIMARY KEY(username)
);

CREATE TABLE Customer (
    username  varchar(25)  NOT NULL UNIQUE,
    password  varchar(25)  NOT NULL,
    email     varchar(25)  NOT NULL,
    PRIMARY KEY(username),
);

CREATE TABLE Review (
    rev_num  int           NOT NULL,
    rating   int           NOT NULL,
    location varchar       NOT NULL,
    comment  varchar(500)  NOT NULL,
    Rusername   varchar(25)   NOT NULL,
    PRIMARY KEY(rev_num),
    FOREIGN KEY(Rusername) REFERENCES Customer(username) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Payment_Info (
    cardnum  int          NOT NULL,
    name     varchar(20)  NOT NULL,
    expdate  DATE         NOT NULL, --DATE CONSTRAINT
    CVV      int          NOT NULL,
    Pusername   varchar(25)  NOT NULL,
    PRIMARY KEY(cardnum)
    FOREIGN KEY(Pusername) REFERENCES Customer(username) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Reservation (
    reservationID  int   NOT NULL,
    start_date     DATE  NOT NULL,
    end_date       DATE  NOT NULL CHECK(end_date > start_date),
    tot_cost       DEC(6,2)   NOT NULL,
    Rcardnum       int   NOT NULL,
    Rusername      varchar(25)  NOT NULL,
    PRIMARY KEY(reservationID),
    FOREIGN KEY(Rcardnum) REFERENCES Payment_Info(cardnum),
    FOREIGN KEY(Rusername) REFERENCES Customer(username)
);

CREATE TABLE Room (
    roomnum  int  NOT NULL,
    location int  NOT NULL,
    category int  NOT NULL,
    numpeople int  NOT NULL,
    cpday  DEC(6,2)  NOT NULL,
    PRIMARY KEY(roomnum, location)
);

CREATE TABLE Extra_Bed (
    Rroomnum  int  NOT NULL,
    Rlocation  int  NOT NULL,
    bedcost  DEC(4,2)  NOT NULL,
    PRIMARY KEY(Rroomnum, Rlocation),
    FOREIGN KEY(Rroomnum) REFERENCES Room(roomnum)
);

CREATE TABLE Select_Extra_Bed (
    SreservationID  int  NOT NULL,
    Sroomnum        int  NOT NULL,
    Slocation       int  NOT NULL,
    PRIMARY KEY(SreservationID, Sroomnum, Slocation),
    FOREIGN KEY(Sroomnum) REFERENCES Room(roomnum),
    FOREIGN KEY(Slocation) REFERENCES Room(location)
);

CREATE TABLE Reservation_Has_Room (
    HreservationID  int  NOT NULL,
    Hroomnum        int  NOT NULL,
    Hlocation       varchar  NOT NULL,
    PRIMARY KEY(HreservationID, Hroomnum, Hlocation),
    FOREIGN KEY(HreservationID) REFERENCES Reservation(reservationID),
    FOREIGN KEY(Hroomnum) REFERENCES Room(roomnum),
    FOREIGN KEY(Hlocation) REFERENCES Room(location)
);
