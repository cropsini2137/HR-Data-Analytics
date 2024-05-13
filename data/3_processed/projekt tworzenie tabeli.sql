-- Generated by Oracle SQL Developer Data Modeler 21.2.0.183.1957
--   at:        2022-11-28 18:04:43 CET
--   site:      SQL Server 2000
--   type:      SQL Server 2000



CREATE TABLE IdPracownik 
    (
     IdPracownik INTEGER NOT NULL , 
     Imie VARCHAR (30) , 
     Nazwisko VARCHAR (30) , 
     Stanowisko VARCHAR (30) , 
     Warsztat_IdWarsztat INTEGER NOT NULL 
    )
GO

ALTER TABLE IdPracownik ADD CONSTRAINT IdPracownik_PK PRIMARY KEY CLUSTERED (IdPracownik)
    GO

CREATE TABLE Klient 
    (
     IdKlient INTEGER NOT NULL , 
     Login VARCHAR (50) , 
     Imie VARCHAR (28) , 
     Nazwisko VARCHAR (30) , 
     numerTelefonu INTEGER , 
     czyKontoZweryfikowane BIT 
    )
GO

ALTER TABLE Klient ADD CONSTRAINT Klient_PK PRIMARY KEY CLUSTERED (IdKlient)
    GO

CREATE TABLE OpinieUzytkownikow 
    (
     IdOpinii INTEGER , 
     Ocena INTEGER , 
     TrescOpinii VARCHAR (500) , 
     Zamowienie_IdZamowienia INTEGER NOT NULL 
    )
GO

CREATE TABLE Pojazd 
    (
     IdPojazdu INTEGER NOT NULL , 
     kosztZaKilometr FLOAT , 
     lokalizacja VARCHAR (50) , 
     CzyHulajnoga BIT , 
     CzyRower BIT , 
     dopuszczalnaLiczbaPasazerow INTEGER , 
     maksymalnyUdzwig INTEGER , 
     stanBaterii INTEGER , 
     maksymalnaPredkosc INTEGER , 
     IdWarsztat INTEGER NOT NULL 
    )
GO

ALTER TABLE Pojazd ADD CONSTRAINT Pojazd_PK PRIMARY KEY CLUSTERED (IdPojazdu)
    GO

CREATE TABLE UsterkaPojazdu 
    (
     idUsterki INTEGER NOT NULL , 
     OpisUsterki VARCHAR (500) , 
     PriorytetUsterki INTEGER , 
     KosztUsterki FLOAT , 
     Zamowienie_IdZamowienia INTEGER NOT NULL 
    )
GO

ALTER TABLE UsterkaPojazdu ADD CONSTRAINT UsterkaPojazdu_PK PRIMARY KEY CLUSTERED (idUsterki)
    GO

CREATE TABLE Warsztat 
    (
     IdWarsztat INTEGER NOT NULL , 
     Miasto VARCHAR (50) , 
     KodPocztowy VARCHAR (7) , 
     PojemnoscPojazdu INTEGER 
    )
GO

ALTER TABLE Warsztat ADD CONSTRAINT Warsztat_PK PRIMARY KEY CLUSTERED (IdWarsztat)
    GO

CREATE TABLE Zamowienie 
    (
     IdZamowienia INTEGER NOT NULL , 
     PrzejechaneKilometry FLOAT , 
     Cena FLOAT , 
     Klient_IdKlient INTEGER NOT NULL , 
     Pojazd_IdPojazdu INTEGER NOT NULL 
    )
GO

ALTER TABLE Zamowienie ADD CONSTRAINT Zamowienie_PK PRIMARY KEY CLUSTERED (IdZamowienia)
    GO

ALTER TABLE IdPracownik 
    ADD CONSTRAINT IdPracownik_Warsztat_FK FOREIGN KEY 
    ( 
     Warsztat_IdWarsztat
    ) 
    REFERENCES Warsztat 
    ( 
     IdWarsztat 
    ) 
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION 
GO

ALTER TABLE OpinieUzytkownikow 
    ADD CONSTRAINT OpinieUzytkownikow_Zamowienie_FK FOREIGN KEY 
    ( 
     Zamowienie_IdZamowienia
    ) 
    REFERENCES Zamowienie 
    ( 
     IdZamowienia 
    ) 
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION 
GO

ALTER TABLE Pojazd 
    ADD CONSTRAINT Pojazd_Warsztat_FK FOREIGN KEY 
    ( 
     IdWarsztat
    ) 
    REFERENCES Warsztat 
    ( 
     IdWarsztat 
    ) 
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION 
GO

ALTER TABLE UsterkaPojazdu 
    ADD CONSTRAINT UsterkaPojazdu_Zamowienie_FK FOREIGN KEY 
    ( 
     Zamowienie_IdZamowienia
    ) 
    REFERENCES Zamowienie 
    ( 
     IdZamowienia 
    ) 
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION 
GO

ALTER TABLE Zamowienie 
    ADD CONSTRAINT Zamowienie_Klient_FK FOREIGN KEY 
    ( 
     Klient_IdKlient
    ) 
    REFERENCES Klient 
    ( 
     IdKlient 
    ) 
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION 
GO

ALTER TABLE Zamowienie 
    ADD CONSTRAINT Zamowienie_Pojazd_FK FOREIGN KEY 
    ( 
     Pojazd_IdPojazdu
    ) 
    REFERENCES Pojazd 
    ( 
     IdPojazdu 
    ) 
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION 
GO



-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                             7
-- CREATE INDEX                             0
-- ALTER TABLE                             12
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE DATABASE                          0
-- CREATE DEFAULT                           0
-- CREATE INDEX ON VIEW                     0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE ROLE                              0
-- CREATE RULE                              0
-- 
-- DROP DATABASE                            0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
