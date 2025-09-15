CREATE USER 'flaskusr'@'localhost' IDENTIFIED BY '<mot de passe de flaskusr>';
GRANT ALL PRIVILEGES ON `flaskSql`.* TO `flaskusr`@`localhost`;