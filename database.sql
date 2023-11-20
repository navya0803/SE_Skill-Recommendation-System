/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.1.13-MariaDB : Database - resume
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`resume` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `resume`;

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `Slno` int(200) NOT NULL AUTO_INCREMENT,
  `Username` varchar(200) DEFAULT NULL,
  `Useremail` varchar(200) DEFAULT NULL,
  `Userpassword` varchar(200) DEFAULT NULL,
  `Age` int(200) DEFAULT NULL,
  `Address` varchar(200) DEFAULT NULL,
  `Contact` int(200) DEFAULT NULL,
  PRIMARY KEY (`Slno`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`Slno`,`Username`,`Useremail`,`Userpassword`,`Age`,`Address`,`Contact`) values (1,'Balaram','admin@admin.com','1234',25,'tirupati',2147483647),(2,'Balaram','balaram@gmail.com','1234',25,'tirupati',2147483647);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
