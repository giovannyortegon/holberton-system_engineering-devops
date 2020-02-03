GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'replica_user';
FLUSH PRIVILEGES;
UPDATE mysql.user SET Repl_slave_priv='N' WHERE user='holberton_user';
