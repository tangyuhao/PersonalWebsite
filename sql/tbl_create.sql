DROP TABLE IF EXISTS User, Album, Photo, BlogGroup, BlogContain, Blog, Article;
CREATE TABLE User(
	username VARCHAR(20),
	firstname VARCHAR(20),
	lastname VARCHAR(20),
	password VARCHAR(256),
	email VARCHAR(40),
	PRIMARY KEY(username)
	);
CREATE TABLE BlogGroup(
	groupid INT AUTO_INCREMENT,
	title VARCHAR(50),
	PRIMARY KEY(groupid)
	);
CREATE TABLE Blog(
	blogid INT AUTO_INCREMENT,
	groupid INT,
	title VARCHAR(50),
	article_num INT DEFAULT 0,
	PRIMARY KEY(blogid)
	);
CREATE TABLE Article(
	articleid VARCHAR(64),
	blogid INT,
	title VARCHAR(256),
	abstract VARCHAR(4096) NOT NULL DEFAULT '',
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	lastupdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	author VARCHAR(20) DEFAULT 'Mr.Tang',
	cover_img VARCHAR(64) DEFAULT 'default-3.jpg',
	reading_num INT DEFAULT 0,
	PRIMARY KEY(articleid)
	);



CREATE TABLE Album(
	albumid INT AUTO_INCREMENT,
	title VARCHAR(50),
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	lastupdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY(albumid)
	);
CREATE TABLE Photo(
	picid VARCHAR(40),
	albumid INT,
	format CHAR(3),
	caption VARCHAR(255) NOT NULL DEFAULT '',
	date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(picid)
	);

CREATE TRIGGER photo_add_update AFTER INSERT ON Photo
FOR EACH ROW
	UPDATE Album 
	SET lastupdated = CURRENT_TIMESTAMP
	WHERE albumid = NEW.albumid;

CREATE TRIGGER photo_cap_update AFTER UPDATE ON Photo
FOR EACH ROW
	UPDATE Album 
	SET lastupdated = CURRENT_TIMESTAMP 
	WHERE albumid = NEW.albumid;

CREATE TRIGGER photo_delete_update AFTER DELETE ON Photo
FOR EACH ROW
	UPDATE Album 
	SET lastupdated = CURRENT_TIMESTAMP
	WHERE albumid = OLD.albumid;

CREATE TRIGGER article_add_update AFTER INSERT ON Article
FOR EACH ROW
	UPDATE Blog
	SET article_num = article_num + 1
	WHERE blogid = NEW.blogid;

CREATE TRIGGER article_delete_update AFTER DELETE ON Article
FOR EACH ROW
	UPDATE Blog
	SET article_num = article_num - 1
	WHERE blogid = OLD.blogid;


-- CREATE TRIGGER album_delete_update AFTER DELETE ON Album
-- FOR EACH ROW
-- 	DELETE FROM Photo
-- 	WHERE albumid = OLD.albumid;

