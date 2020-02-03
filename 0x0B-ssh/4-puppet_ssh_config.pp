# Set up your client SSH configuration
exec {'/etc/ssh/ssh_config':
    command   => '/bin/echo -e "IdentityFile ~/.ssh/holberton\n
		 PasswordAuthentication no" >> /etc/ssh/ssh_config',
    path      => '/etc/ssh/ssh_config',
}
