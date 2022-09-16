-- Create the schemas
CREATE DATABASE IF NOT EXISTS `test_db`;
CREATE DATABASE IF NOT EXISTS `audit_db`;

--  Create the users
DROP USER IF EXISTS 'dev_user'@'%';
CREATE USER `dev_user` IDENTIFIED BY 'devpassword' PASSWORD EXPIRE INTERVAL 45 DAY;

FLUSH PRIVILEGES;

-- Build the objects
USE `test_db`;

CREATE TABLE `test_table` (
  `row_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`row_id`)
);
