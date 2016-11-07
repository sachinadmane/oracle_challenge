-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Nov 07, 2016 at 03:52 PM
-- Server version: 5.5.36
-- PHP Version: 5.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `oracle_2`
--

-- --------------------------------------------------------

--
-- Table structure for table `oracle_recipedetails`
--

CREATE TABLE IF NOT EXISTS `oracle_recipedetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `owner` varchar(250) NOT NULL,
  `recipe_id` int(11),
  `recipedescription` longtext,
  PRIMARY KEY (`id`),
  KEY `oracle_recipedetails_da50e9c3` (`recipe_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `oracle_recipedetails`
--
ALTER TABLE `oracle_recipedetails`
  ADD CONSTRAINT `oracle_recipedetails_recipe_id_08738fbe_fk_oracle_recipe_id` FOREIGN KEY (`recipe_id`) REFERENCES `oracle_recipe` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
