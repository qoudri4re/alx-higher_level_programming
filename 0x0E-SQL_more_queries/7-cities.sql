-- creates the database hbtn_0d_usa and 
-- the table cities in the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
--switch database
USE htbn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
  id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  UNIQUE(id),
  FOREIGN KEY(states_id) REFERENCES states(id)
);  
