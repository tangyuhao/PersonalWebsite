# this is my default username and password
INSERT INTO User VALUES('yuhaotang','Yuhao','Tang','sha512$061faf7306ab4f5a8d7c011016ba9c1e$e58242f8651b9169794dca810c34ac1d45abb5fd13580a014df20a1faa9af907f4c3aff2cd8f3a401d7362e0e04aa63f638c67bfcfd5266672e0842c009b8bb6','blogyhtang1993@gmail.com');


INSERT INTO BlogGroup(title) VALUES ('Tech'); # id: 1
INSERT INTO Blog(title,groupid) VALUES ('Test',1);
INSERT INTO Blog(title,groupid) VALUES ('Deep Learning',1);
INSERT INTO Blog(title,groupid) VALUES ('Computer Vision',1);
INSERT INTO Blog(title,groupid) VALUES ('Web Development',1);
INSERT INTO Blog(title,groupid) VALUES ('Leetcode',1);

INSERT INTO BlogGroup(title) VALUES ('Travel'); # id: 2 
INSERT INTO Blog(title,groupid) VALUES ('Travel',2);

INSERT INTO BlogGroup(title) VALUES ('Others'); # id: 3 
INSERT INTO Blog(title,groupid) VALUES ('Others',3);

# These are just for testing blogs!
INSERT INTO Article(articleid, blogid, title, abstract, cover_img) VALUES ('sample_article_1', 1, 'this is a test article', 'this is a test for abstract', 'default-1.jpg');
INSERT INTO Article(articleid, blogid, title, abstract, cover_img) VALUES ('sample_article_2', 1, 'this is a test article', 'this is a test for abstract', 'default-1.jpg');
INSERT INTO Article(articleid, blogid, title, abstract, cover_img) VALUES ('sample_article_3', 1, 'this is a test article', 'this is a test for abstract', 'default-1.jpg');
INSERT INTO Article(articleid, blogid, title, abstract, cover_img) VALUES ('sample_article_4', 3, 'this is a test article', 'this is a test for abstract', 'default-1.jpg');
INSERT INTO Article(articleid, blogid, title, abstract) VALUES ('sample_article_5', 4, 'this is a test article', 'this is a test for abstract');
INSERT INTO Article(articleid, blogid, title, abstract) VALUES ('sample_article_6', 2, 'this is a test article', 'this is a test for abstract');
INSERT INTO Article(articleid, blogid, title, abstract) VALUES ('sample_article_7', 2, 'this is a test article', 'this is a test for abstract');
INSERT INTO Article(articleid, blogid, title, abstract) VALUES ('sample_article_8', 2, 'this is a test article', 'this is a test for abstract');

# These are just for testing albums!
INSERT INTO Album(title) VALUES('I love sports');
INSERT INTO Album(title) VALUES('I love football');
INSERT INTO Album(title) VALUES('Around The World');
INSERT INTO Album(title) VALUES('Cool Space Shots');

INSERT INTO Photo(albumid,picid,format) VALUES(2,'001025dd643b0eb0661e359de86e3ea9','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(2,'9a0a7d25af4f7a73f67dde74e8e54cff','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(2,'c8e60100f13ffe374d59e39dc4b6a318','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(2,'5e8b6207f007338243d3e29d6b82acab','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(4,'4ddba6e2f905e9778c6b6a48b6fc8e03','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(4,'09d8a979fa638125b02ae1578eb943fa','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(4,'143ba34cb5c7e8f12420be1b576bda1a','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(4,'e615a10fc4222ede59ca3316c3fb751c','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(4,'65fb1e2aa4977d9414d1b3a7e4a3badd','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(1,'b94f256c23dec8a2c0da546849058d9e','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(1,'01e37cbdd55913df563f527860b364e8','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(1,'8d554cd1d8bb7b49ca798381d1fc171b','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(1,'2e9e69e19342b98141789925e5f87f60','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(1,'298e8943ef1942159ef88be21c4619c9','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(1,'cefe45eaeaeb599256dda325c2e972da','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(1,'bf755d13bb78e1deb59ef66b6d5c6a70','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(1,'5f8d7957874f1303d8300e50f17e46d6','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(3,'bac4fca50bed35b9a5646f632bf4c2e8','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(3,'f5b57bd7a2c962c54d55b5ddece37158','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(3,'b7d833dd3aae203ca618759fc6f4fc01','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(3,'faa20c04097d40cb10793a19246f2754','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(3,'aaaadd578c78d21defaa73e7d1f08235','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(3,'adb5c3af19664129141268feda90a275','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(3,'abf97ffd1f964f42790fb358e5258e8d','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(3,'ea2db8b970671856e43dd011d7df5fad','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(3,'76d79b81b9073a2323f0790965b00a68','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(3,'6510a4add59ef655ae3f0b6cdb24e140','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(3,'28d38afca913a728b2a6bcf01aa011cd','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(3,'5fb04eb11cbf99429a05c12ce2f50615','jpg');
INSERT INTO Photo(albumid,picid,format) VALUES(3,'39ee267d13ccd32b50c1de7c2ece54d6','jpg');

