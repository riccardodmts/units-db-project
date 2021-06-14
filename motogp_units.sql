-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: motogp_units
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accordo`
--

DROP TABLE IF EXISTS `accordo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accordo` (
  `anno` year NOT NULL,
  `durata` int DEFAULT NULL,
  `categoria` varchar(45) DEFAULT NULL,
  `team` varchar(60) NOT NULL,
  `moto` varchar(45) NOT NULL,
  PRIMARY KEY (`anno`,`team`,`moto`),
  KEY `team_fk` (`team`),
  KEY `moto_fk` (`moto`),
  CONSTRAINT `moto_fk` FOREIGN KEY (`moto`) REFERENCES `casacostruttrice` (`nome`),
  CONSTRAINT `team_fk` FOREIGN KEY (`team`) REFERENCES `team` (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accordo`
--

LOCK TABLES `accordo` WRITE;
/*!40000 ALTER TABLE `accordo` DISABLE KEYS */;
INSERT INTO `accordo` VALUES (2020,2,'motogp','Petronas SRT','Yamaha'),(2020,1,'motogp','Pramac Racing','Ducati');
/*!40000 ALTER TABLE `accordo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campionato`
--

DROP TABLE IF EXISTS `campionato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campionato` (
  `anno` year NOT NULL,
  `categoria` varchar(45) NOT NULL,
  PRIMARY KEY (`anno`,`categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campionato`
--

LOCK TABLES `campionato` WRITE;
/*!40000 ALTER TABLE `campionato` DISABLE KEYS */;
INSERT INTO `campionato` VALUES (2018,'moto2'),(2020,'motogp');
/*!40000 ALTER TABLE `campionato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `casacostruttrice`
--

DROP TABLE IF EXISTS `casacostruttrice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `casacostruttrice` (
  `nome` varchar(30) NOT NULL,
  `nazione` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `casacostruttrice`
--

LOCK TABLES `casacostruttrice` WRITE;
/*!40000 ALTER TABLE `casacostruttrice` DISABLE KEYS */;
INSERT INTO `casacostruttrice` VALUES ('Aprilia','Italia'),('Ducati','Italia'),('Honda','Giappone'),('KTM','Austria'),('Suzuki','Giappone'),('Yamaha','Giappone');
/*!40000 ALTER TABLE `casacostruttrice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `circuito`
--

DROP TABLE IF EXISTS `circuito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `circuito` (
  `nome` varchar(70) NOT NULL,
  `nazione` varchar(45) DEFAULT NULL,
  `località` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `circuito`
--

LOCK TABLES `circuito` WRITE;
/*!40000 ALTER TABLE `circuito` DISABLE KEYS */;
INSERT INTO `circuito` VALUES ('Circuito di Brno','Repubblica Ceca','Brno'),('Circuito di Jerez de la Frontera','Spagna','Jerez de la Frontera'),('Misano World Circuit Marco Simoncelli','Italia','Misano Adriatico'),('Red Bull Ring','Austria','Spielberg bei Knittelfeld');
/*!40000 ALTER TABLE `circuito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contratto`
--

DROP TABLE IF EXISTS `contratto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contratto` (
  `anno` year NOT NULL,
  `durata` int DEFAULT NULL,
  `categoria` varchar(45) DEFAULT NULL,
  `team` varchar(60) NOT NULL,
  `pilota` int NOT NULL,
  PRIMARY KEY (`anno`,`team`,`pilota`),
  KEY `team_c_fk` (`team`),
  KEY `pilota_fk` (`pilota`),
  CONSTRAINT `pilota_fk` FOREIGN KEY (`pilota`) REFERENCES `pilota` (`codice`),
  CONSTRAINT `team_c_fk` FOREIGN KEY (`team`) REFERENCES `team` (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contratto`
--

LOCK TABLES `contratto` WRITE;
/*!40000 ALTER TABLE `contratto` DISABLE KEYS */;
INSERT INTO `contratto` VALUES (2020,1,'motogp','Ducati Team',5),(2020,1,'motogp','Monster Energy Yamaha MotoGP',2),(2020,1,'motogp','Petronas SRT',1),(2020,1,'motogp','Pramac Racing',4),(2020,1,'motogp','Team SUZUKI ECSTAR',6),(2021,1,'motogp','Petronas SRT',2),(2021,1,'motogp','Pramac Racing',1);
/*!40000 ALTER TABLE `contratto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `granpremio`
--

DROP TABLE IF EXISTS `granpremio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `granpremio` (
  `codice` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) DEFAULT NULL,
  `data` date DEFAULT NULL,
  `circuito` varchar(70) DEFAULT NULL,
  `anno` year DEFAULT NULL,
  `categoria` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`codice`),
  KEY `circuito_fk` (`circuito`),
  KEY `campionato_fk` (`anno`,`categoria`),
  CONSTRAINT `campionato_fk` FOREIGN KEY (`anno`, `categoria`) REFERENCES `campionato` (`anno`, `categoria`),
  CONSTRAINT `circuito_fk` FOREIGN KEY (`circuito`) REFERENCES `circuito` (`nome`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `granpremio`
--

LOCK TABLES `granpremio` WRITE;
/*!40000 ALTER TABLE `granpremio` DISABLE KEYS */;
INSERT INTO `granpremio` VALUES (1,'Gran Premio Red Bull de Espana','2020-07-19','Circuito di Jerez de la Frontera',2020,'motogp'),(4,'Gran Premio Red Bull de Andalucia','2020-07-26','Circuito di Jerez de la Frontera',2020,'motogp'),(5,'Monster Energy Grand Prix České republiky','2020-08-08','Circuito di Brno',2020,'motogp'),(7,'myWorld Motorrad Grand Prix Von Österreich','2020-08-16','Red Bull Ring',2020,'motogp'),(8,'BMW M Gran Priz of Styria','2020-08-23','Red Bull Ring',2020,'motogp'),(9,'Gran Premio Lenovo di San Marino','2020-09-13','Misano World Circuit Marco Simoncelli',2020,'motogp');
/*!40000 ALTER TABLE `granpremio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `iscrizione`
--

DROP TABLE IF EXISTS `iscrizione`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `iscrizione` (
  `numero` int DEFAULT NULL,
  `pilota` int NOT NULL,
  `categoria` varchar(45) NOT NULL,
  `anno` year NOT NULL,
  PRIMARY KEY (`anno`,`categoria`,`pilota`),
  KEY `pilota_iscrizione_fk` (`pilota`),
  CONSTRAINT `campionato_iscrizione_fk` FOREIGN KEY (`anno`, `categoria`) REFERENCES `campionato` (`anno`, `categoria`),
  CONSTRAINT `pilota_iscrizione_fk` FOREIGN KEY (`pilota`) REFERENCES `pilota` (`codice`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iscrizione`
--

LOCK TABLES `iscrizione` WRITE;
/*!40000 ALTER TABLE `iscrizione` DISABLE KEYS */;
INSERT INTO `iscrizione` VALUES (63,4,'moto2',2018),(20,1,'motogp',2020),(46,2,'motogp',2020),(63,4,'motogp',2020),(4,5,'motogp',2020),(36,6,'motogp',2020);
/*!40000 ALTER TABLE `iscrizione` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partecipazione`
--

DROP TABLE IF EXISTS `partecipazione`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partecipazione` (
  `posizioneGriglia` int DEFAULT NULL,
  `posizione` int DEFAULT NULL,
  `punti` int DEFAULT NULL,
  `tempo` time(3) DEFAULT NULL,
  `pilota` int NOT NULL,
  `granPremio` int NOT NULL,
  PRIMARY KEY (`pilota`,`granPremio`),
  KEY `gp_iscrizione_fk` (`granPremio`),
  CONSTRAINT `gp_iscrizione_fk` FOREIGN KEY (`granPremio`) REFERENCES `granpremio` (`codice`),
  CONSTRAINT `pilota_par_fk` FOREIGN KEY (`pilota`) REFERENCES `pilota` (`codice`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partecipazione`
--

LOCK TABLES `partecipazione` WRITE;
/*!40000 ALTER TABLE `partecipazione` DISABLE KEYS */;
INSERT INTO `partecipazione` VALUES (1,1,25,'00:41:23.796',1,1),(1,1,25,'00:41:22.666',1,4),(2,7,9,'00:41:50.573',1,5),(3,8,8,'00:28:33.387',1,7),(10,13,3,'00:17:03.431',1,8),(3,NULL,0,NULL,1,9),(11,NULL,0,NULL,2,1),(4,3,16,'00:41:28.212',2,4),(10,5,11,'00:41:46.276',2,5),(12,5,11,'00:28:26.690',2,7),(17,9,7,'00:17:00.542',2,8),(4,4,13,'00:42:04.915',2,9),(4,7,9,'00:41:36.823',4,1),(3,NULL,0,NULL,4,4),(6,2,20,'00:42:02.489',4,9),(8,3,16,'00:41:29.742',5,1),(16,6,10,'00:41:35.220',5,4),(20,11,5,'00:41:55.219',5,5),(4,1,25,'00:28:20.853',5,7),(9,5,11,'00:16:57.439',5,8),(9,7,9,'00:42:12.630',5,9),(12,NULL,0,NULL,6,1),(10,5,11,'00:41:30.359',6,4),(9,NULL,0,NULL,6,5),(6,2,20,'00:28:22.230',6,7),(4,4,13,'00:16:56.666',6,8),(8,3,16,'00:42:02.562',6,9);
/*!40000 ALTER TABLE `partecipazione` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pilota`
--

DROP TABLE IF EXISTS `pilota`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pilota` (
  `codice` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) DEFAULT NULL,
  `cognome` varchar(45) DEFAULT NULL,
  `dataNascita` date DEFAULT NULL,
  `nazione` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`codice`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pilota`
--

LOCK TABLES `pilota` WRITE;
/*!40000 ALTER TABLE `pilota` DISABLE KEYS */;
INSERT INTO `pilota` VALUES (1,'Fabio','Quartararo','1999-04-20','Francia'),(2,'Valentino','Rossi','1979-02-16','Italia'),(4,'Francesco','Bagnaia','1997-01-14','Italia'),(5,'Andrea','Dovizioso','1986-03-23','Italia'),(6,'Joan','Mir','1997-09-01','Spagna');
/*!40000 ALTER TABLE `pilota` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team`
--

DROP TABLE IF EXISTS `team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team` (
  `nome` varchar(60) NOT NULL,
  `nazione` varchar(45) DEFAULT NULL,
  `costruttore` varchar(45) DEFAULT NULL,
  `tipo` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team`
--

LOCK TABLES `team` WRITE;
/*!40000 ALTER TABLE `team` DISABLE KEYS */;
INSERT INTO `team` VALUES ('Ducati Team','Italia','Ducati','ufficiale'),('Monster Energy Yamaha MotoGP','Giappone','Yamaha','ufficiale'),('Petronas SRT','Malaysia',NULL,'satellite'),('Pramac Racing','Italia',NULL,'satellite'),('Team SUZUKI ECSTAR','Giappone','Suzuki','ufficiale');
/*!40000 ALTER TABLE `team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'motogp_units'
--
/*!50003 DROP PROCEDURE IF EXISTS `sp_get_championship_manufacturer_ranking` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_get_championship_manufacturer_ranking`(IN anno_ch VARCHAR(10), IN cat_ch VARCHAR(10))
BEGIN
SELECT (@row_num := @row_num + 1) AS Pos, t2.*
FROM (SELECT t.Moto AS 'Casa costruttrice', SUM(t.Punti) AS Punti
FROM( SELECT numero AS Num , CONCAT(pilota.nome, ' ', pilota.cognome) AS Pilota, sum(punti) AS Punti, team.nome as Team, moto AS Moto 
FROM partecipazione

INNER JOIN pilota 
ON pilota.codice = partecipazione.pilota

INNER JOIN contratto
ON pilota.codice = contratto.pilota

INNER JOIN team
ON team.nome = contratto.team

INNER JOIN accordo
ON team.nome = accordo.team

INNER JOIN iscrizione
ON pilota.codice = iscrizione.pilota

WHERE contratto.anno = '2020' AND iscrizione.anno = '2020' AND iscrizione.categoria = 'motogp'
GROUP BY pilota.codice

UNION

SELECT numero AS Num,CONCAT(pilota.nome, ' ', pilota.cognome) AS Pilota, sum(punti) AS Punti, team.nome AS Team, costruttore AS Moto
FROM partecipazione

INNER JOIN pilota 
ON pilota.codice = partecipazione.pilota

INNER JOIN contratto
ON pilota.codice = contratto.pilota

INNER JOIN team
ON team.nome = contratto.team

INNER JOIN iscrizione
ON pilota.codice = iscrizione.pilota

WHERE contratto.anno = '2020' AND team.tipo = 'ufficiale' AND iscrizione.anno = '2020' AND iscrizione.categoria = 'motogp'

GROUP BY pilota.codice

ORDER BY Punti DESC) t

GROUP BY t.Moto

ORDER BY Punti DESC) t2 JOIN (SELECT @row_num := 0) r;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_get_championship_ranking` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_get_championship_ranking`(IN anno_ch VARCHAR(10), IN cat_ch VARCHAR(10))
BEGIN

SELECT (@row_num := @row_num + 1) AS Posizione, t.* 
FROM (SELECT numero AS Num , CONCAT(pilota.nome, ' ', pilota.cognome) AS Pilota, sum(punti) AS Punti, team.nome as Team, moto AS Moto 
FROM partecipazione

INNER JOIN pilota 
ON pilota.codice = partecipazione.pilota

INNER JOIN contratto
ON pilota.codice = contratto.pilota

INNER JOIN team
ON team.nome = contratto.team

INNER JOIN accordo
ON team.nome = accordo.team

INNER JOIN iscrizione
ON pilota.codice = iscrizione.pilota

WHERE contratto.anno = anno_ch AND iscrizione.anno = anno_ch AND iscrizione.categoria = cat_ch
GROUP BY pilota.codice

UNION

SELECT numero AS Num,CONCAT(pilota.nome, ' ', pilota.cognome) AS Pilota, sum(punti) AS Punti, team.nome AS Team, costruttore AS Moto
FROM partecipazione

INNER JOIN pilota 
ON pilota.codice = partecipazione.pilota

INNER JOIN contratto
ON pilota.codice = contratto.pilota

INNER JOIN team
ON team.nome = contratto.team

INNER JOIN iscrizione
ON pilota.codice = iscrizione.pilota

WHERE contratto.anno = anno_ch AND team.tipo = 'ufficiale' AND iscrizione.anno = anno_ch AND iscrizione.categoria = cat_ch

GROUP BY pilota.codice

ORDER BY Punti DESC) t  JOIN (SELECT @row_num := 0) r;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_get_drivers_list_from_championship` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_get_drivers_list_from_championship`(IN anno_ch VARCHAR(10), IN cat_ch VARCHAR(10))
BEGIN
	SELECT CONCAT(iscrizione.numero, ' ', pilota.nome, ' ', pilota.cognome) AS Pilota
	FROM iscrizione
	INNER JOIN pilota
	ON pilota.codice = iscrizione.pilota
	WHERE iscrizione.anno = anno_ch AND iscrizione.categoria = cat_ch;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_get_driver_results` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_get_driver_results`(IN anno_ch VARCHAR(10), IN cat_ch VARCHAR(10), IN nome_pilota VARCHAR(45), IN cognome_pilota VARCHAR(45))
BEGIN
SELECT  granPremio.data AS 'Data', granPremio.nome AS GranPremio, partecipazione.posizione AS Posizione, partecipazione.punti AS Punti
FROM partecipazione
INNER JOIN granPremio
ON partecipazione.granPremio = granPremio.codice
INNER JOIN pilota
ON partecipazione.pilota = pilota.codice
WHERE pilota.nome = nome_pilota AND pilota.cognome = cognome_pilota AND granPremio.anno = anno_ch AND granPremio.categoria = cat_ch
ORDER BY 'Data';
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_get_gran_prix_ranking` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_get_gran_prix_ranking`(IN anno_gp VARCHAR(10), IN cat_gp VARCHAR(50), IN nome_gp VARCHAR (80))
BEGIN
	DECLARE codice_gp INT(11);
    
    SELECT codice INTO  codice_gp FROM granPremio WHERE categoria = cat_gp AND granPremio.anno = anno_gp AND nome = nome_gp; 
    
    SELECT posizione AS Posizione,numero AS Num , CONCAT(pilota.nome, ' ', pilota.cognome) AS Pilota, punti AS Punti,tempo AS Tempo, team.nome as Team, moto AS Moto 
	FROM partecipazione

	INNER JOIN pilota 
	ON pilota.codice = partecipazione.pilota

	INNER JOIN contratto
	ON pilota.codice = contratto.pilota

	INNER JOIN team
	ON team.nome = contratto.team

	INNER JOIN accordo
	ON team.nome = accordo.team

	INNER JOIN iscrizione
	ON pilota.codice = iscrizione.pilota

	WHERE contratto.anno =  anno_gp AND granPremio =  codice_gp AND iscrizione.anno = anno_gp AND iscrizione.categoria = cat_gp

	UNION

	SELECT posizione AS Posizione,numero AS Num,CONCAT(pilota.nome, ' ', pilota.cognome) AS Pilota, punti AS Punti,tempo AS Tempo, team.nome AS Team, costruttore AS Moto
	FROM partecipazione

	INNER JOIN pilota 
	ON pilota.codice = partecipazione.pilota

	INNER JOIN contratto
	ON pilota.codice = contratto.pilota

	INNER JOIN team
	ON team.nome = contratto.team

	INNER JOIN iscrizione
	ON pilota.codice = iscrizione.pilota

	WHERE contratto.anno = anno_gp AND granPremio = codice_gp AND team.tipo = 'ufficiale' AND iscrizione.anno = anno_gp AND iscrizione.categoria = cat_gp

	ORDER BY -posizione DESC;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_get_leader` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_get_leader`(IN anno_ch VARCHAR(10), IN cat_ch VARCHAR(10))
BEGIN
SELECT t.nome, t.cognome FROM (
SELECT sum(punti) AS Punti, pilota.codice, pilota.nome as nome, pilota.cognome as cognome
FROM partecipazione

INNER JOIN pilota 
ON pilota.codice = partecipazione.pilota

INNER JOIN iscrizione
ON pilota.codice = iscrizione.pilota

WHERE iscrizione.anno = anno_ch AND iscrizione.categoria = cat_ch
GROUP BY pilota.codice
ORDER BY Punti DESC) t LIMIT 1;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_get_number_na` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_get_number_na`(IN anno_ch VARCHAR(10), IN cat_ch VARCHAR(10), IN nome_pilota VARCHAR(45), IN cognome_pilota VARCHAR(45))
BEGIN
SELECT COUNT(*) AS NA
FROM partecipazione
INNER JOIN granPremio
ON partecipazione.granPremio = granPremio.codice
INNER JOIN pilota
ON partecipazione.pilota = pilota.codice
WHERE pilota.nome = nome_pilota AND pilota.cognome = cognome_pilota AND granPremio.anno = anno_ch AND granPremio.categoria = cat_ch AND partecipazione.posizione IS NULL;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_get_number_podiums` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_get_number_podiums`(IN anno_ch VARCHAR(10), IN cat_ch VARCHAR(10), IN nome_pilota VARCHAR(45), IN cognome_pilota VARCHAR(45))
BEGIN
SELECT COUNT(partecipazione.posizione) AS Podi
FROM partecipazione
INNER JOIN granPremio
ON partecipazione.granPremio = granPremio.codice
INNER JOIN pilota
ON partecipazione.pilota = pilota.codice
WHERE pilota.nome = nome_pilota AND pilota.cognome = cognome_pilota AND granPremio.anno = anno_ch AND granPremio.categoria = cat_ch AND partecipazione.posizione <= 3;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_get_number_victories` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_get_number_victories`(IN anno_ch VARCHAR(10), IN cat_ch VARCHAR(10), IN nome_pilota VARCHAR(45), IN cognome_pilota VARCHAR(45))
BEGIN
SELECT COUNT(partecipazione.posizione) AS Vittorie
FROM partecipazione
INNER JOIN granPremio
ON partecipazione.granPremio = granPremio.codice
INNER JOIN pilota
ON partecipazione.pilota = pilota.codice
WHERE pilota.nome = nome_pilota AND pilota.cognome = cognome_pilota AND granPremio.anno = anno_ch AND granPremio.categoria = cat_ch AND partecipazione.posizione = 1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-13 12:40:30
