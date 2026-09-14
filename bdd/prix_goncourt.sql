DROP DATABASE IF EXISTS `prix_goncourt`;
CREATE DATABASE IF NOT EXISTS `prix_goncourt` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `prix_goncourt`;
-- --------------------------------------------------------
-- Table `PERSON`
-- --------------------------------------------------------
CREATE TABLE PERSON(
   person_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   person_name VARCHAR(20) NOT NULL,
   person_lastname VARCHAR(20) NOT NULL,
   biography BLOB
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Table `JURY_MEMBER`
-- --------------------------------------------------------

CREATE TABLE JURY_MEMBER(
   person_id INT NOT NULL UNIQUE,
   chairman BOOLEAN,
   member_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   CONSTRAINT "fk_person_jury" FOREIGN KEY (person_id) REFERENCES PERSON(person_id)
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
