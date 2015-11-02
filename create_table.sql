CREATE TABLE Management (
    username  varchar(5)  NOT NULL,
    password  varchar(25)  NOT NULL,
    PRIMARY KEY(username)
)Engine=InnoDB;

CREATE TABLE Customer (
    username  varchar(5)  NOT NULL,
    password  varchar(25)  NOT NULL,
    email     varchar(25)  NOT NULL,
    PRIMARY KEY(username),
    UNIQUE(email)
)Engine=InnoDB;

CREATE TABLE Review (
    rev_num  int           NOT NULL AUTO_INCREMENT,
    rating   varchar(10)           NOT NULL CHECK(rating in ('Excellent', 'Good', 'Bad', 'Very Bad', 'Neutral')),
    location varchar(10)   NOT NULL CHECK(location in ('Atlanta', 'Charlotte', 'Savannah', 'Orlando', 'Miami')),
    comment  varchar(500)  NOT NULL,
    Rusername   varchar(25)   NOT NULL,
    PRIMARY KEY(rev_num),
    FOREIGN KEY(Rusername) REFERENCES Customer(username)
)Engine=InnoDB;

CREATE TABLE Payment_Info (
    cardnum  int          NOT NULL,
    name     varchar(20)  NOT NULL,
    expdate  DATE         NOT NULL,
    CVV      int          NOT NULL CHECK(CVV>99 AND CVV<1000),
    Pusername   varchar(25)  NOT NULL,
    PRIMARY KEY(cardnum),
    FOREIGN KEY(Pusername) REFERENCES Customer(username)
)Engine=InnoDB;

CREATE TABLE Reservation (
    reservationID  int   NOT NULL AUTO_INCREMENT,
    start_date     DATE  NOT NULL,
    end_date       DATE  NOT NULL CHECK(end_date > start_date),
    tot_cost       DEC(6,2)   NOT NULL,
    Rcardnum       int   NOT NULL,
    Rusername      varchar(25)  NOT NULL,
    PRIMARY KEY(reservationID),
    FOREIGN KEY(Rcardnum) REFERENCES Payment_Info(cardnum),
    FOREIGN KEY(Rusername) REFERENCES Customer(username)
)Engine=InnoDB;

CREATE TABLE Room (
    roomnum   int  NOT NULL,
    location  varchar(10)   NOT NULL CHECK(location in ('Atlanta', 'Charlotte', 'Savannah', 'Orlando', 'Miami')),
    category  int  NOT NULL,
    numpeople int  NOT NULL,
    cpday     DEC(6,2)  NOT NULL,
    PRIMARY KEY(roomnum, location)
)Engine=InnoDB;

CREATE TABLE Extra_Bed (
    Rroomnum   int  NOT NULL,
    Rlocation  varchar(10)   NOT NULL,
    bedcost    DEC(4,2)  NOT NULL,
    PRIMARY KEY(Rroomnum, Rlocation),
    FOREIGN KEY(Rroomnum, Rlocation) REFERENCES Room(roomnum, location)
)Engine=InnoDB;

CREATE TABLE Select_Extra_Bed (
    SreservationID  int  NOT NULL,
    Sroomnum        int  NOT NULL,
    Slocation       varchar(10)   NOT NULL,
    PRIMARY KEY(SreservationID, Sroomnum, Slocation),
    FOREIGN KEY(Sroomnum, Slocation) REFERENCES Room(roomnum, location)
)Engine=InnoDB;

CREATE TABLE Reservation_Has_Room (
    HreservationID  int  NOT NULL,
    Hroomnum        int  NOT NULL,
    Hlocation       varchar(10)   NOT NULL,
    PRIMARY KEY(HreservationID, Hroomnum, Hlocation),
    FOREIGN KEY(HreservationID) REFERENCES Reservation(reservationID),
    FOREIGN KEY(Hroomnum, Hlocation) REFERENCES Room(roomnum, location)
)Engine=InnoDB;
