DROP TABLE IF EXISTS `TO_BE_MEMBER_OF`;
DROP TABLE IF EXISTS `CREATING`;
DROP TABLE IF EXISTS `EDITE`;
DROP TABLE IF EXISTS `EDITOR`;
DROP TABLE IF EXISTS `VOTE`;
DROP TABLE IF EXISTS `BOOK`;
DROP TABLE IF EXISTS `LITERARY_PRIZE`;
DROP TABLE IF EXISTS `CHARACTER_BOOK`;
DROP TABLE IF EXISTS `AUTHOR`;
DROP TABLE IF EXISTS `JURY_MEMBER`;
DROP TABLE IF EXISTS `SELECTION`;
DROP TABLE IF EXISTS `PERSON`;
-- --------------------------------------------------------
-- Table `PERSON`
-- --------------------------------------------------------
CREATE TABLE prix_goncourt.PERSON(
   person_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   person_name VARCHAR(20) NOT NULL,
   person_lastname VARCHAR(20) NOT NULL,
   biography BLOB
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------
-- Table `JURY_MEMBER`
-- --------------------------------------------------------

CREATE TABLE prix_goncourt.JURY_MEMBER(
   person_id INT NOT NULL,
   member_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   CONSTRAINT fk_person_jury FOREIGN KEY (person_id) REFERENCES PERSON(person_id) ON DELETE CASCADE
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

   -- --------------------------------------------------------
-- Table `AUTHOR`
-- --------------------------------------------------------

CREATE TABLE prix_goncourt.AUTHOR(
   person_id INT NOT NULL,
   author_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   CONSTRAINT fk_person_author FOREIGN KEY (person_id) REFERENCES PERSON(person_id) ON DELETE CASCADE
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

   -- --------------------------------------------------------
-- Table `CHARACTER`
-- --------------------------------------------------------

CREATE TABLE prix_goncourt.CHARACTER_BOOK(
   person_id INT NOT NULL,
   character_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   CONSTRAINT fk_person_character FOREIGN KEY (person_id) REFERENCES PERSON(person_id) ON DELETE CASCADE
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
   -- --------------------------------------------------------
-- Table `SELECTION`
-- --------------------------------------------------------

CREATE TABLE prix_goncourt.SELECTION(
   selection_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   selection_number TINYINT NOT NULL,
   date_selection date NOT NULL,
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


   -- --------------------------------------------------------
-- Table `LITERARY_PRIZE`
-- --------------------------------------------------------
CREATE TABLE prix_goncourt.LITERARY_PRIZE(
   prize_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   prize_name VARCHAR(50) NOT NULL,
   selection_id INT NOT NULL,
   CONSTRAINT fk_selection_prize FOREIGN KEY (selection_id) REFERENCES SELECTION(selection_id) ON DELETE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
      -- --------------------------------------------------------
-- Table `BOOK`
-- --------------------------------------------------------

-- j'ai volontairement pas mis de colonnes année car on a 2 solutions qui sont aussi efficace sans devoir en créé
-- si on a peu de donnée, juste  year(release_book) si c'est realease_book qu'on veut pour avoir l'année
-- ou sinon faire realease_book >= 'a-01-01' AND realease_date <= 'a-12-31' ou a est l'année et si
-- il y a beaucoup de données. dans des cas assez spécifiques, on peut toujours créé
-- une colonne virtuelle avec mariadb, ce genre de cas est pour des dizaines ou
-- des centaines de millions de lignes et encore, fautdrait demander avec des group by.

CREATE TABLE prix_goncourt.BOOK(
   author_id INT NOT NULL,
   book_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   title VARCHAR(200) NOT NULL,
   summarize BLOB,
   release_book date NOT NULL,
   number_page INT NOT NULL,
   price DECIMAL(6,2),
   ISBN VARCHAR(20) NOT NULL UNIQUE,
   CONSTRAINT fk_author_book FOREIGN KEY (author_id) REFERENCES AUTHOR(author_id) ON DELETE CASCADE
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

     -- --------------------------------------------------------
-- Table `EDITOR`
-- --------------------------------------------------------

CREATE TABLE prix_goncourt.EDITOR(
   editor VARCHAR(20) NOT NULL,
   editor_id INT NOT NULL PRIMARY KEY,
   PRIMARY KEY(editor, editor_id)
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

   -- --------------------------------------------------------
-- Table `EDITE`
-- --------------------------------------------------------

CREATE TABLE prix_goncourt.EDITE(
   book_id INT NOT NULL,
   editor_id INT NOT NULL
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

   -- --------------------------------------------------------
-- Table `VOTE`
-- --------------------------------------------------------

CREATE TABLE prix_goncourt.VOTE(
   book_id INT NOT NULL,
   selection_id INT NOT NULL,
   number_vote TINYINT NOT NULL,
   CONSTRAINT fk_selection_vote FOREIGN KEY (selection_id) REFERENCES SELECTION(selection_id) ON DELETE CASCADE,
   CONSTRAINT fk_book_vote FOREIGN KEY (book_id) REFERENCES book(book_id) ON DELETE CASCADE
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

      -- --------------------------------------------------------
-- Table `CREATING`
-- --------------------------------------------------------

CREATE TABLE prix_goncourt.CREATING(
   book_id INT NOT NULL,
   character_id INT NOT NULL,
   CONSTRAINT fk_character_creating FOREIGN KEY (character_id) REFERENCES CHARACTER_BOOK(character_id) ON DELETE CASCADE,
   CONSTRAINT fk_book_creating FOREIGN KEY (book_id) REFERENCES book(book_id) ON DELETE CASCADE
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



      -- --------------------------------------------------------
-- Table `TO_BE_MEMBER_OF`
-- --------------------------------------------------------

CREATE TABLE prix_goncourt.TO_BE_MEMBER_OF(
   member_id INT NOT NULL,
   chairman BOOLEAN NOT NULL,
   prize_id INT NOT NULL,
   CONSTRAINT fk_prize_to_be_member_of FOREIGN KEY (prize_id) REFERENCES LITERARY_PRIZE(prize_id) ON DELETE CASCADE,
   CONSTRAINT fk_member_to_be_member_of FOREIGN KEY (member_id) REFERENCES JURY_MEMBER(member_id) ON DELETE CASCADE
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
