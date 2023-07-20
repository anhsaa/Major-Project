-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: futsaldb
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `venue`
--

DROP TABLE IF EXISTS `venue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venue` (
  `venue_id` int NOT NULL AUTO_INCREMENT,
  `owner_id` int DEFAULT NULL,
  `image` varchar(150) DEFAULT NULL,
  `venue_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `contact` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `rating` int DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `delete_flag` int DEFAULT NULL,
  PRIMARY KEY (`venue_id`),
  KEY `owner_id` (`owner_id`),
  CONSTRAINT `venue_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `owner` (`owner_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venue`
--

LOCK TABLES `venue` WRITE;
/*!40000 ALTER TABLE `venue` DISABLE KEYS */;
INSERT INTO `venue` VALUES (2,NULL,'https://lh3.googleusercontent.com/p/AF1QipNzJW4wMXgP2GDVhTx1e47J_TYRWN0S0HhceOPu=s680-w680-h510','kathmandu Fustal','ktm@gmail.com','tinkune','184116565',NULL,3,'jfnoifjfkfoijfnwef',NULL),(3,NULL,'https://lh5.googleusercontent.com/p/AF1QipO-RC_PeCAPvfh_tCxcFjFfQyljaopZpahVSASW=w68-h69-n-k-no','futsal','f@gmail.com','tinkune','5464212168',NULL,4,'ssfdsgdfhtfgjhg',NULL),(4,NULL,'https://lh3.googleusercontent.com/p/AF1QipNzJW4wMXgP2GDVhTx1e47J_TYRWN0S0HhceOPu=s680-w680-h510','bhaktapur futsal','bht@gmail.com','Bhaktapur','789654',NULL,4,'string',NULL),(5,1,'https://lh3.googleusercontent.com/p/AF1QipNzJW4wMXgP2GDVhTx1e47J_TYRWN0S0HhceOPu=s680-w680-h510','futsal ktm','f@fmail.com','tinkunne','7896541233',NULL,5,' dsnsd sjnd sjvbsd',NULL);
/*!40000 ALTER TABLE `venue` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-20 15:29:48
