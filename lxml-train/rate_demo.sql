/*
money_type : 金额类型 美元,欧元
cur_price : 当前价格
published_time : 发布时间
collection_time : 采集日期
*/

CREATE TABLE `rate_demo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `money_type` varchar(45) DEFAULT NULL,
  `cur_price` decimal(10,0) DEFAULT NULL,
  `published_time` varchar(50) DEFAULT NULL,
  `collection_time` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;