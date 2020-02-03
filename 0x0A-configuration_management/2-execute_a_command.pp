# Create a manifest that kills a process named killmenow.

exec { 'killmenow':
    command => 'pkill --signal SIGTERM killmenow',
    path    => '/usr/bin',
}
