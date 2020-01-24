CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica_user';
GRANT REPLICATION SLAVE ON *.*
TO 'replica_user'@'%'
IDENTIFIED BY 'replica_user';
UPDATE mysql.user SET Repl_slave_priv='N' WHERE user='holberton_user';
FLUSH PRIVILEGES;
