SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

-- --------------------------------------------------------
-- Table structure for table `Users`
-- ---------------------------------------------------------

DROP TABLE IF EXISTS Users;

CREATE TABLE Users (
  user_id int NOT NULL AUTO_INCREMENT,
  email varchar(255) NOT NULL,
  username varchar(255) NOT NULL,
  last_login_date DATE DEFAULT NULL,
  UNIQUE (user_id, email, username),
  PRIMARY KEY(user_id)
);

INSERT INTO Users (email, username, last_login_date)
VALUES('jes@mail.com', 'jessey', '20050216'),('Hey@mail.com', 'hermines','20060405'),('imagine@mail.com', 'Boa', '20020312');

-- ---------------------------------------------------------
-- Table structure for table `Passwords`
-- ---------------------------------------------------------

DROP TABLE IF EXISTS Passwords;

CREATE TABLE Passwords (
  password_id int NOT NULL AUTO_INCREMENT,
  password_value varchar(255),
  created_at DATE NOT NULL,
  strength int(1) NOT NULL,
  FK_user_id int NOT NULL,
  PRIMARY KEY(password_id),
  FOREIGN KEY (FK_user_id) REFERENCES Users(user_id)
  ON DELETE CASCADE
);

INSERT INTO Passwords (password_value, created_at, FK_user_id)
VALUES ('helli', '20010715', 1), ('hehe', '19990615', 2), ('outside', '20020606', 3),('Corgi!23', '20230713', 1), ('DiscreteM@th589', '20221201', 1), ('Fuj!MCosmic32', '20230127', 3),
('Oreg3gonSt@te', '20220101', 2), ('Rhythym&Blues1996', '20230717', 2), ('M@cBo0k11', '20230717', 3);

-- ---------------------------------------------------------
-- Table structure for table `Password_Generator_Rules`
-- ---------------------------------------------------------

DROP TABLE IF EXISTS Password_Generator_Rules;

CREATE TABLE Password_Generator_Rules (
  FK_user_id int NOT NULL,
  password_length int(3) NOT NULL DEFAULT 8,
  allowed_characters boolean DEFAULT 0 NOT NULL,
  require_uppercase boolean DEFAULT 0 NOT NULL,
  require_lowercase boolean DEFAULT 0 NOT NULL,
  require_digits boolean DEFAULT 0 NOT NULL,
  require_special_characters boolean DEFAULT 0 NOT NULL,
  FOREIGN KEY (FK_user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

INSERT INTO Password_Generator_Rules (FK_user_id, password_length, allowed_characters, require_uppercase, require_lowercase, require_digits, require_special_characters)
VALUES (1, 10,1,1,1,1,1), (1,15,1,1,1,1,1), (3,8,1,1,1,1,1);

-- ---------------------------------------------------------
-- Table structure for table `Password_Histories`
-- ---------------------------------------------------------

DROP TABLE IF EXISTS Password_Histories;

CREATE TABLE Password_Histories (
  history_id int AUTO_INCREMENT,
  FK_user_id int NOT NULL,
  FK_password_id int NOT NULL,
  old_password_value varchar(255) NOT NULL DEFAULT '',
  change_date DATE NOT NULL,
  PRIMARY KEY (history_id),
  FOREIGN KEY (FK_password_id) REFERENCES Passwords(password_id) ON DELETE CASCADE,
  FOREIGN KEY (FK_user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

INSERT INTO Password_Histories (FK_user_id, FK_password_id, old_password_value, change_date)
VALUES (1, 4, 'helli', '20230713'), (2,5,'hehe','20230127'), (3,6,'outside', '20220101');

-- ---------------------------------------------------------
-- Table structure for table `Password_Categories`
-- ---------------------------------------------------------

DROP TABLE IF EXISTS Password_Categories;

CREATE TABLE Password_Categories (
  category_id int NOT NULL AUTO_INCREMENT,
  category_name varchar(255) NOT NULL,
  FK_password_id int NOT NULL,
  PRIMARY KEY(category_id),
  FOREIGN KEY (FK_password_id) REFERENCES Passwords(password_id)
  ON DELETE CASCADE
);

INSERT INTO Password_Categories (category_name, FK_password_id)
VALUES ('math',5),('apple',6),('school', 7);

-- ---------------------------------------------------------
-- Table structure for table `Password_Categories_Junction`
-- ---------------------------------------------------------

DROP TABLE IF EXISTS Password_Categories_Junction;

CREATE TABLE Password_Categories_Junction (
  FK_password_id int NOT NULL,
  FK_category_id int NOT NULL,
  FOREIGN KEY (FK_password_id) REFERENCES Passwords(password_id),
  FOREIGN KEY (FK_category_id) REFERENCES Password_Categories(category_id)
);
