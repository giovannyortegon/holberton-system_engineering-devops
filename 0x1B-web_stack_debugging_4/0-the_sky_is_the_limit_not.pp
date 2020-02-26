# Fix our stack
exec { 'Fix our stack':
  command  => 'sed -i \'s/15/2001/\' /etc/default/nginx && service nginx restart',
  provider => shell,
  }
