/*
 Navicat Premium Data Transfer

 Source Server         : 10.10.10.125
 Source Server Type    : MySQL
 Source Server Version : 50620
 Source Host           : 10.10.10.125
 Source Database       : cdb_test

 Target Server Type    : MySQL
 Target Server Version : 50620
 File Encoding         : utf-8

 Date: 05/18/2017 17:25:44 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `cus$shop`
-- ----------------------------
DROP TABLE IF EXISTS `cus$shop`;
CREATE TABLE `cus$shop` (
  `shop_id` varchar(10) NOT NULL,
  `shop_name` varchar(30) DEFAULT NULL,
  `shop_addr` varchar(100) DEFAULT NULL,
  `shop_type` varchar(5) DEFAULT NULL COMMENT '店门类型',
  `shop_level` varchar(10) DEFAULT NULL COMMENT '门店等级',
  `shop_area` varchar(20) DEFAULT NULL,
  `busidisc_type_name` varchar(16) DEFAULT NULL COMMENT '门店所属商圈',
  `salesman_name` varchar(20) DEFAULT NULL COMMENT '跟进业务人员',
  `boss_name` varchar(20) DEFAULT NULL,
  `boss_tel_no` varchar(30) DEFAULT NULL,
  `sign_mode` varchar(16) DEFAULT NULL,
  `sign_status` varchar(8) DEFAULT NULL,
  `status` char(1) DEFAULT NULL,
  `createon` datetime DEFAULT NULL,
  `createby` varchar(5) DEFAULT NULL,
  `modifyon` datetime DEFAULT NULL,
  `modifyby` varchar(5) DEFAULT NULL,
  `link_to_shop_id` varchar(30) DEFAULT NULL COMMENT '推荐人ID',
  `password` varchar(255) DEFAULT NULL COMMENT '密码',
  `province` varchar(10) DEFAULT NULL COMMENT '省份',
  `city` varchar(40) DEFAULT NULL COMMENT '市',
  `register_status` int(11) DEFAULT '2' COMMENT '注册状态 0禁用 1新用户未审核 2审核通过 3审核通过并返利过 4审核通过并7天返利过',
  `distr_site` bigint(255) DEFAULT NULL COMMENT '外配站点ID',
  `subarea_id` varchar(16) DEFAULT NULL,
  `shop_streetId` int(11) DEFAULT NULL,
  `shop_streetName` varchar(48) DEFAULT NULL,
  PRIMARY KEY (`shop_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
