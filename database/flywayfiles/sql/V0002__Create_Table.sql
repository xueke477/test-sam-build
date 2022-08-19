USE `test_db`;

CREATE TABLE `test_table2` (
  `row_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `value` int,
  `insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`row_id`)
);
