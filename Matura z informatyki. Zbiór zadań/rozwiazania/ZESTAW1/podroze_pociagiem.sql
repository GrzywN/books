-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 14 Maj 2023, 17:49
-- Wersja serwera: 10.4.27-MariaDB
-- Wersja PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `podroze_pociagiem`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `bilety`
--

CREATE TABLE `bilety` (
  `nr_biletu` int(4) DEFAULT NULL,
  `nr_przejazdu` int(3) DEFAULT NULL,
  `cena` int(3) DEFAULT NULL,
  `ilosc` int(2) DEFAULT NULL,
  `ulga` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Zrzut danych tabeli `bilety`
--

INSERT INTO `bilety` (`nr_biletu`, `nr_przejazdu`, `cena`, `ilosc`, `ulga`) VALUES
(2001, 501, 180, 1, 0),
(2002, 501, 180, 2, 0),
(2003, 502, 69, 1, 0),
(2004, 502, 69, 2, 0),
(2005, 503, 180, 2, 0),
(2006, 504, 32, 10, 0),
(2007, 506, 120, 1, 0),
(2008, 504, 32, 1, 0),
(2009, 509, 180, 1, 0),
(2010, 503, 180, 1, 0),
(2011, 504, 32, 2, 0),
(2012, 509, 180, 1, 0),
(2013, 504, 32, 2, 0),
(2014, 505, 32, 1, 0),
(2015, 506, 120, 1, 0);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `przejazdy`
--

CREATE TABLE `przejazdy` (
  `nr_przejazdu` int(3) DEFAULT NULL,
  `nr_skladu` int(3) DEFAULT NULL,
  `data` date DEFAULT NULL,
  `stacja_pocz` varchar(18) DEFAULT NULL,
  `czas_wyj` time DEFAULT NULL,
  `stacja_kon` varchar(19) DEFAULT NULL,
  `czas_przyj` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Zrzut danych tabeli `przejazdy`
--

INSERT INTO `przejazdy` (`nr_przejazdu`, `nr_skladu`, `data`, `stacja_pocz`, `czas_wyj`, `stacja_kon`, `czas_przyj`) VALUES
(501, 104, '2022-07-15', 'Warszawa Wschodnia', '08:12:00', 'Berlin Hauptbahnhof', '14:55:00'),
(502, 106, '2022-07-15', 'Warszawa Wschodnia', '16:10:00', 'Berlin Hauptbahnhof', '20:55:00'),
(503, 109, '2022-07-15', 'Gdynia', '03:12:00', 'Jelenia Gora', '13:12:00'),
(504, 108, '2022-07-16', 'Konin', '05:12:00', 'Poznan', '07:12:00'),
(505, 108, '2022-07-16', 'Poznan', '12:12:00', 'Konin', '16:44:00'),
(506, 105, '2022-07-17', 'Katowice', '06:12:00', 'Gdynia', '14:55:00'),
(507, 103, '2022-07-17', 'Poznan', '08:10:00', 'Katowice', '12:40:00'),
(508, 101, '2022-07-18', 'Poznan', '05:12:00', 'Zielona Gora', '08:12:00'),
(509, 102, '2022-07-18', 'Katowice', '07:12:00', 'Gdynia', '14:12:00'),
(510, 108, '2022-07-18', 'Poznan', '12:12:00', 'Konin', '16:44:00');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `sklady`
--

CREATE TABLE `sklady` (
  `nr_skladu` int(3) DEFAULT NULL,
  `nazwa` varchar(23) DEFAULT NULL,
  `lokomotywa` varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Zrzut danych tabeli `sklady`
--

INSERT INTO `sklady` (`nr_skladu`, `nazwa`, `lokomotywa`) VALUES
(101, 'Bachus', 'EP-07'),
(102, 'Zefir', 'EP-09'),
(103, 'Cegielski', 'EP-09'),
(104, 'Malczewski', 'EP-09'),
(105, 'Barbakan', 'EP-07'),
(106, 'Berolina', 'Husarz'),
(107, 'Berolina', 'Husarz'),
(108, 'Powstaniec Wielkopolski', 'EP-09'),
(109, 'Szklarka', 'EP-09'),
(110, 'Hetman', 'Pendolino');

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `zadanie5_1`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `zadanie5_1` (
`nr_skladu` int(3)
,`nazwa` varchar(23)
,`lokomotywa` varchar(9)
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `zadanie5_2`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `zadanie5_2` (
`nr_biletu` int(4)
,`ilosc` int(2)
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `zadanie5_3`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `zadanie5_3` (
`Ile różnych modeli lokomotyw` bigint(21)
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `zadanie5_4`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `zadanie5_4` (
`nr_przejazdu` int(3)
,`Łączna kwota zakupionych biletów w zł` varbinary(26)
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `zadanie5_5`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `zadanie5_5` (
`Stacja początkowa` varchar(18)
,`Ile osób wyjechało` decimal(32,0)
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `zadanie5_6a`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `zadanie5_6a` (
`nr_przejazdu` int(3)
,`Najkrótszy czas drogi` time
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `zadanie5_6b`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `zadanie5_6b` (
`nr_przejazdu` int(3)
,`Najdłuższy czas drogi` time
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `zadanie5_7`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `zadanie5_7` (
`nr_przejazdu` int(3)
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `zadanie5_8`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `zadanie5_8` (
`lokomotywa` varchar(9)
,`Liczba przejazdów` bigint(21)
,`DATA` date
);

-- --------------------------------------------------------

--
-- Struktura widoku `zadanie5_1`
--
DROP TABLE IF EXISTS `zadanie5_1`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `zadanie5_1`  AS SELECT `sklady`.`nr_skladu` AS `nr_skladu`, `sklady`.`nazwa` AS `nazwa`, `sklady`.`lokomotywa` AS `lokomotywa` FROM `sklady` WHERE !(`sklady`.`nr_skladu` in (select `przejazdy`.`nr_skladu` from `przejazdy`))  ;

-- --------------------------------------------------------

--
-- Struktura widoku `zadanie5_2`
--
DROP TABLE IF EXISTS `zadanie5_2`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `zadanie5_2`  AS SELECT `bilety`.`nr_biletu` AS `nr_biletu`, `bilety`.`ilosc` AS `ilosc` FROM `bilety` WHERE `bilety`.`nr_przejazdu` = 504 ORDER BY `bilety`.`ilosc` AS `DESCdesc` ASC  ;

-- --------------------------------------------------------

--
-- Struktura widoku `zadanie5_3`
--
DROP TABLE IF EXISTS `zadanie5_3`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `zadanie5_3`  AS SELECT count(distinct `sklady`.`lokomotywa`) AS `Ile różnych modeli lokomotyw` FROM `sklady``sklady`  ;

-- --------------------------------------------------------

--
-- Struktura widoku `zadanie5_4`
--
DROP TABLE IF EXISTS `zadanie5_4`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `zadanie5_4`  AS SELECT `bilety`.`nr_przejazdu` AS `nr_przejazdu`, concat(sum(`bilety`.`ilosc` * `bilety`.`cena` * (1 - `bilety`.`ulga`)),' zł') AS `Łączna kwota zakupionych biletów w zł` FROM (`bilety` join `przejazdy` on(`bilety`.`nr_przejazdu` = `przejazdy`.`nr_przejazdu`)) GROUP BY `bilety`.`nr_przejazdu` ORDER BY sum(`bilety`.`ilosc` * `bilety`.`cena` * (1 - `bilety`.`ulga`)) DESC LIMIT 0, 11  ;

-- --------------------------------------------------------

--
-- Struktura widoku `zadanie5_5`
--
DROP TABLE IF EXISTS `zadanie5_5`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `zadanie5_5`  AS SELECT `przejazdy`.`stacja_pocz` AS `Stacja początkowa`, sum(`bilety`.`ilosc`) AS `Ile osób wyjechało` FROM (`bilety` join `przejazdy` on(`bilety`.`nr_przejazdu` = `przejazdy`.`nr_przejazdu`)) GROUP BY `przejazdy`.`stacja_pocz` ORDER BY sum(`bilety`.`ilosc`) DESC LIMIT 0, 11  ;

-- --------------------------------------------------------

--
-- Struktura widoku `zadanie5_6a`
--
DROP TABLE IF EXISTS `zadanie5_6a`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `zadanie5_6a`  AS SELECT `przejazdy`.`nr_przejazdu` AS `nr_przejazdu`, timediff(`przejazdy`.`czas_przyj`,`przejazdy`.`czas_wyj`) AS `Najkrótszy czas drogi` FROM `przejazdy` ORDER BY timediff(`przejazdy`.`czas_przyj`,`przejazdy`.`czas_wyj`) ASC LIMIT 0, 11  ;

-- --------------------------------------------------------

--
-- Struktura widoku `zadanie5_6b`
--
DROP TABLE IF EXISTS `zadanie5_6b`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `zadanie5_6b`  AS SELECT `przejazdy`.`nr_przejazdu` AS `nr_przejazdu`, timediff(`przejazdy`.`czas_przyj`,`przejazdy`.`czas_wyj`) AS `Najdłuższy czas drogi` FROM `przejazdy` ORDER BY timediff(`przejazdy`.`czas_przyj`,`przejazdy`.`czas_wyj`) DESC LIMIT 0, 11  ;

-- --------------------------------------------------------

--
-- Struktura widoku `zadanie5_7`
--
DROP TABLE IF EXISTS `zadanie5_7`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `zadanie5_7`  AS SELECT `przejazdy`.`nr_przejazdu` AS `nr_przejazdu` FROM `przejazdy` WHERE !(`przejazdy`.`nr_przejazdu` in (select `bilety`.`nr_przejazdu` from `bilety`))  ;

-- --------------------------------------------------------

--
-- Struktura widoku `zadanie5_8`
--
DROP TABLE IF EXISTS `zadanie5_8`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `zadanie5_8`  AS SELECT `sklady`.`lokomotywa` AS `lokomotywa`, count(0) AS `Liczba przejazdów`, `przejazdy`.`data` AS `DATA` FROM (`przejazdy` join `sklady` on(`przejazdy`.`nr_skladu` = `sklady`.`nr_skladu`)) GROUP BY `sklady`.`lokomotywa`, `przejazdy`.`data` ORDER BY count(0) AS `DESCdesc` ASC  ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
