-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: Oct 05, 2024 at 03:49 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project_news`
--

-- --------------------------------------------------------

--
-- Table structure for table `decisionofnews`
--

CREATE TABLE `decisionofnews` (
  `Article` int(10) NOT NULL,
  `Feedback` varchar(1000) NOT NULL,
  `NewsDecision` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `decisionofnews`
--

INSERT INTO `decisionofnews` (`Article`, `Feedback`, `NewsDecision`) VALUES
(101, 'Its real', 'Real'),
(102, 'Its Fake', 'Fake'),
(103, 'It real', 'Real'),
(104, 'Its Fake', 'Fake'),
(105, 'Its real', 'Real'),
(106, 'Its Real', 'Real'),
(107, 'Its real', 'Real'),
(108, 'Its real', 'Real'),
(109, 'Its real', 'Real'),
(110, 'Its real', 'Real'),
(111, 'Its real', 'Real'),
(112, 'Its real', 'Real');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `Name` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Feedback` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`Name`, `Email`, `Feedback`) VALUES
('Jeyathish', 'jeyathish0987@gmail.com', 'Very Good'),
('Jeyathish', 'ads@gmail.com', 'jhsdvfghdarfawhfbdsgjcsj'),
('Jeyathish', 'sdfsdf@gmail.com', 'This is good website..'),
('Dark', 'sdfsdf@gmail.com', 'This is so good.....'),
('White', 'Jeua@gmail.com', 'This a good website.....'),
('Home', 'home@gmail.com', 'This is good....'),
('White', 'Jeua@gmail.com', 'reewrwrwe'),
('Mari', 'mari@gmail.com', 'Good Website...');

-- --------------------------------------------------------

--
-- Table structure for table `forgetpass`
--

CREATE TABLE `forgetpass` (
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `Username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `confirmpassword` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`Username`, `email`, `password`, `confirmpassword`) VALUES
('Jeyathish', 'jeyathish@gmail.com', '12345', '12345'),
('Pradeesh', 'pradeesh@gmail.com', '12345', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `login1`
--

CREATE TABLE `login1` (
  `Username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `confirmpassword` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login1`
--

INSERT INTO `login1` (`Username`, `email`, `password`, `confirmpassword`) VALUES
('Jeyathish', 'jeyathish0987@gmail.com', '12345', '12345'),
('darkened_soul_24', 'sdfsdf@gmail.com', '12345', '12345'),
('darkened', 'darkened@gmail.com', '12345', '12345'),
('Siva', 'siva@gmail.com', '12345', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `newsdataentry`
--

CREATE TABLE `newsdataentry` (
  `Article` int(10) NOT NULL,
  `Newsheading` varchar(100) NOT NULL,
  `Newssummary` varchar(500) NOT NULL,
  `Location` varchar(100) NOT NULL,
  `Image` varchar(255) NOT NULL,
  `NewsDecision` varchar(20) NOT NULL,
  `Feedback` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `newsdataentry`
--

INSERT INTO `newsdataentry` (`Article`, `Newsheading`, `Newssummary`, `Location`, `Image`, `NewsDecision`, `Feedback`) VALUES
(101, 'Suicide case', 'Suicide in Varkala..', 'Varkala', 'img4.jpg', 'Real', 'Its real'),
(102, 'Murder in a house', 'Fight between husband and wife. And the husband was murdered by his wife..', 'Vallioor', 'img5.jpg', 'Fake', 'Its Fake'),
(103, 'Chain Snatching', 'Two Theifs are snatcing a chain from a old lady in Madurai', 'Madurai', 'img2.jpg', 'Real', 'It real'),
(104, 'Car Accident', 'Car Accident in Munnar. Car Driver was dead..', 'Munnar', 'img3.jpg', 'Fake', 'Its Fake'),
(105, 'ICC T20 World Cup 2024', 'ICC T20 World cup 2024 was started in India', 'India', 'img8.jpg', 'Real', 'Its Real'),
(106, 'Terrorist Attack', 'Terrorist Attack in Kashmir..', 'Jammu and Kashmir', 'img1.jpg', 'Real', 'Its Real'),
(107, 'CM meets PM', 'Our Tamil Nadu Cheif Minister was met our Honourable Prime Minister in Delhi..', 'Delhi', 'img7.jpg', 'Real', 'Its real'),
(108, 'Kutti Puli Movie Release', 'The movie named \"Kutti Puli\" was released on May 30th this year.. ', 'Tamil Nadu', 'img9.jpg', 'Real', 'Its real'),
(109, 'Flood', 'Flood in Kanya Kumari...', 'Kanya Kumari', 'img6.jpg', 'Real', 'Its real'),
(110, 'Heavy Rainfall', 'Schools and Colleges are leave due to Heavy Rainfall in Tirunelveli..', 'Tirunelveli', 'img10.jpg', 'Real', 'Its real'),
(111, 'Crashing', 'crashing', 'Munnar', 'img3.jpg', 'Real', 'Its real'),
(112, 'Terrorist Attack', 'Terrorist Attack in India and Pakistan border..', 'Pakistan border', 'img1.jpg', 'Real', 'Its real');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `decisionofnews`
--
ALTER TABLE `decisionofnews`
  ADD UNIQUE KEY `Article` (`Article`);

--
-- Indexes for table `newsdataentry`
--
ALTER TABLE `newsdataentry`
  ADD UNIQUE KEY `Article` (`Article`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
