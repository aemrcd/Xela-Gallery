

CREATE Database IF NOT EXISTS xxelaDB;

USE xxelaDB;


CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);


-- This is for admin who controls the database
GRANT ALL PRIVILEGES ON xxelaDB. * TO 'admin_user'@'%';  

-- this is for readonly-user who can only read data and cannot apply changes to the database
GRANT SELECT, SHOW VIEW ON xxelaDB. * TO 'readonly_user'@'localhost';


Flush PRIVILEGES;

-- Show all the user in mariadb
SELECT User, Host FROM mysql.user;

-- DELETE A SINGLE ROW FROM THE TABLE
DELETE FROM users WHERE id = 1;