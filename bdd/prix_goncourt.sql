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
   chairman BOOLEAN NOT NULL,
   member_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   CONSTRAINT "fk_person_jury" FOREIGN KEY (person_id) REFERENCES PERSON(person_id)
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

   -- --------------------------------------------------------
-- Table `AUTHOR`
-- --------------------------------------------------------

CREATE TABLE AUTHOR(
   person_id INT NOT NULL UNIQUE,
   author_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   CONSTRAINT "fk_person_author" FOREIGN KEY (person_id) REFERENCES PERSON(person_id)
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

   -- --------------------------------------------------------
-- Table `CHARACTER`
-- --------------------------------------------------------

CREATE TABLE CHARACTER(
   person_id INT NOT NULL UNIQUE,
   character_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   CONSTRAINT "fk_person_character" FOREIGN KEY (person_id) REFERENCES PERSON(person_id)
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

   -- --------------------------------------------------------
-- Table `LITERARY_PRIZE`
-- --------------------------------------------------------
CREATE TABLE LITERARY_PRIZE(
   prize_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   prize_name VARCHAR(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


   -- --------------------------------------------------------
-- Table `SELECTION`
-- --------------------------------------------------------

CREATE TABLE SELECTION(
   prize_id INT NOT NULL,
   SELECTION_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   selection_number TINYINT NOT NULL,
   date_selection datetime NOT NULL,
   CONSTRAINT "fk_prize_selection" FOREIGN KEY (prize_id) REFERENCES LITERARY_PRIZE(prize_id)
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

      -- --------------------------------------------------------
-- Table `BOOK`
-- --------------------------------------------------------

CREATE TABLE BOOK(
   author_id INT NOT NULL,
   book_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   title VARCHAR(30) NOT NULL,
   editor VARCHAR(20) NOT NULL,
   summarize BLOB,
   release datetime NOT NULL,
   number_page INT NOT NULL,
   price DECIMAL(6,2),
   ISBN VARCHAR(20) NOT NULL UNIQUE,
   CONSTRAINT "fk_author_book" FOREIGN KEY (prize_id) REFERENCES LITERARY_PRIZE(prize_id)
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

   -- --------------------------------------------------------
-- Table `VOTE`
-- --------------------------------------------------------

CREATE TABLE VOTE(
   book_id INT,
   selection_id INT,
   number_vote TINYINT NOT NULL,
   CONSTRAINT "fk_selection_vote" FOREIGN KEY (selection_id) REFERENCES SELECTION(selection_id),
   CONSTRAINT "fk_book_vote" FOREIGN KEY (book_id) REFERENCES book(book_id)
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

      -- --------------------------------------------------------
-- Table `CREATING`
-- --------------------------------------------------------

CREATE TABLE CREATING(
   book_id INT NOT NULL,
   character_id INT NOT NULL,
   CONSTRAINT "fk_character_creating" FOREIGN KEY (character_id) REFERENCES CHARACTER(character_id),
   CONSTRAINT "fk_book_creating" FOREIGN KEY (book_id) REFERENCES book(book_id)
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
