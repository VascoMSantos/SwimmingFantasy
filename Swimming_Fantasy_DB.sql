DROP DATABASE IF EXISTS `Swimming_Fantasy`;
CREATE DATABASE `Swimming_Fantasy`;
USE `Swimming_Fantasy`;

CREATE TABLE athletes (
	athlete_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    club VARCHAR(50),
    competition_id INT NOT NULL DEFAULT 0,
    competition_points INT
);

CREATE TABLE fantasy_users (
	user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    team JSON,
    draft_salary INT,
    fantasy_points INT
);

CREATE TABLE swimming_styles (
	style_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    meters INT,
    style VARCHAR(10)
);

CREATE TABLE competition_results (
	competition_id INT NOT NULL,
    athlete_id INT NOT NULL,
    style_id INT NOT NULL,
    final_time TIME(2)
);



















