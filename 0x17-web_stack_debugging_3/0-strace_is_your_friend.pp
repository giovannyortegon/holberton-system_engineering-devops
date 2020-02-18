# Find out why Apache is returning a 500 error. 
exec { 'Fix code apache2 and restart':
  command  => 'sudo sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php && sudo service apache2 restart',
  provider => shell,
}