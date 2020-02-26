# Modify holberton Hard and Soft
exec { 'Hard and Soft':
  command  => 'sed -i \'s/nofile 5/nofile 3000/; s/nofile 4/nofile 2000/\' /etc/security/limits.conf',
  provider => shell,
  }
