DROP DATABASE IF EXISTS askdb;
CREATE DATABASE askdb
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;
USE mysql;
CREATE USER 'askdb_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON askdb.* TO 'askdb_user'@'localhost'
WITH GRANT OPTION;
FLUSH PRIVILEGES;
