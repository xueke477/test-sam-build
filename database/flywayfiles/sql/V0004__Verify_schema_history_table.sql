USE `test_db`;

CREATE TABLE `verify_table` (
  `row_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `info` VARCHAR(100) DEFAULT NULL,
  PRIMARY KEY (`row_id`)
);

INSERT INTO `verify_table` (`info`)
SELECT `version` FROM `flyway_schema_history`
ORDER BY `version` DESC LIMIT 1;
