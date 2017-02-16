DROP TABLE IF EXISTS User, Album, Contain, Photo, AlbumAccess;
SET @sequencenum = 0;
CREATE TABLE User(
	username VARCHAR(20),
	firstname VARCHAR(20),
	lastname VARCHAR(20),
	password VARCHAR(256),
	email VARCHAR(40),
	PRIMARY KEY(username)
	);
CREATE TABLE Album(
	albumid INT AUTO_INCREMENT,
	title VARCHAR(50),
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	lastupdated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	username VARCHAR(20),
	access ENUM('public','private'),
	PRIMARY KEY(albumid)
	);
CREATE TABLE Contain(
	sequencenum INT,
	albumid INT,
	picid VARCHAR(40),
	caption VARCHAR(255) NOT NULL DEFAULT ' ',
	PRIMARY KEY(sequencenum)
	);
CREATE TABLE Photo(
	picid VARCHAR(40),
	format CHAR(3),
	date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(picid)
	);

CREATE TABLE AlbumAccess(
	albumid INT,
	username VARCHAR(20),
	CONSTRAINT Unique_id_user PRIMARY KEY (albumid,username)
	);


CREATE TRIGGER add_update AFTER INSERT ON Contain
FOR EACH ROW
	UPDATE Album 
	SET lastupdated = DEFAULT 
	WHERE albumid = NEW.albumid;

CREATE TRIGGER cap_update AFTER UPDATE ON Contain
FOR EACH ROW
	UPDATE Album 
	SET lastupdated = CURRENT_TIMESTAMP 
	WHERE albumid = NEW.albumid;

CREATE TRIGGER auto_seq AFTER INSERT ON Photo
FOR EACH ROW
	SET @sequencenum = @sequencenum + 1;

delimiter //
CREATE TRIGGER delete_delete AFTER DELETE ON Contain
FOR EACH ROW
BEGIN 
	UPDATE Album 
	SET lastupdated = DEFAULT 
	WHERE albumid = OLD.albumid;
	DELETE FROM Photo  
	WHERE picid = OLD.picid;
END
//
delimiter ;
