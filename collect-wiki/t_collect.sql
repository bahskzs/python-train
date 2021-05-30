CREATE TABLE `t_collect` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Date` varchar(45) DEFAULT NULL,
  `Website Title` varchar(1000) DEFAULT NULL,
  `URL` varchar(1000) DEFAULT NULL,
  `Highlight Color Code` varchar(1000) DEFAULT NULL,
  `Highlight Color` varchar(1000) DEFAULT NULL,
  `Color Category` varchar(1000) DEFAULT NULL,
  `Highlighted Text` varchar(1000) DEFAULT NULL,
  `Note` varchar(1000) DEFAULT NULL,
  `collect_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
SELECT * FROM o2o.t_collect;