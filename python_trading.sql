-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 20, 2021 at 02:22 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_trading`
--

-- --------------------------------------------------------

--
-- Table structure for table `analises`
--

CREATE TABLE `analises` (
  `id` int(11) NOT NULL,
  `time_id` int(11) NOT NULL,
  `cripto_id` int(11) NOT NULL,
  `indecator_id` int(11) NOT NULL,
  `price` varchar(191) NOT NULL,
  `tehran_time` varchar(191) NOT NULL,
  `utc_time` varchar(191) NOT NULL,
  `sql_time` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `criptoCurences`
--

CREATE TABLE `criptoCurences` (
  `id` int(11) NOT NULL,
  `cripto_name` varchar(191) NOT NULL,
  `cripto_short_name` varchar(191) NOT NULL,
  `cripto_trade_name` varchar(191) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `indicators`
--

CREATE TABLE `indicators` (
  `id` int(11) NOT NULL,
  `indecator_name` varchar(191) NOT NULL,
  `indecator_shortname` varchar(191) NOT NULL,
  `type` varchar(191) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `timeFrames`
--

CREATE TABLE `timeFrames` (
  `id` int(11) NOT NULL,
  `timeFrameSeconds` varchar(191) CHARACTER SET utf8 COLLATE utf8_persian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
