DROP DATABASE IF EXISTS `Swimming_Fantasy`;
CREATE DATABASE `Swimming_Fantasy`;
USE `Swimming_Fantasy`;

-- TABLE CREATION --

CREATE TABLE athletes (
	athlete_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    club VARCHAR(50)
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
	result_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	competition_id INT NOT NULL,
    athlete_id INT NOT NULL,
    style_id INT NOT NULL,
    final_time TIME(2),
    FOREIGN KEY (athlete_id) REFERENCES athletes(athlete_id),
    FOREIGN KEY (style_id) REFERENCES swimming_styles(style_id)
);


-- INSERTING VALUES ON TABLES --

INSERT INTO swimming_styles (meters, style)
VALUES
(50, 'Free'),
(100, 'Free'),
(200, 'Free'),
(400, 'Free'),
(800, 'Free'),
(1500, 'Free'),
(50, 'Back'),
(100, 'Back'),
(200, 'Back'),
(50, 'Breastroke'),
(100, 'Breastroke'),
(200, 'Breastroke'),
(50, 'Butterfly'),
(100, 'Butterfly'),
(200, 'Butterfly'),
(100, 'Medley'),
(200, 'Medley'),
(400, 'Medley');

INSERT INTO fantasy_users (first_name, last_name, email, age, gender, draft_salary)
VALUES
('Vasco', 'Santos', 'vasco@email.com', 25, 'Male', 1000),
('Pedro', 'Fróis', 'pedro@email.com', 28, 'Male', 1000);













