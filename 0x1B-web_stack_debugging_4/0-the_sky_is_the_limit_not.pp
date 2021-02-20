# script that removes the hard limit of 15 max open files
file { '/etc/default/nginx':
  content => '',
} ->
exec { 'restart':
    command  => 'sudo service nginx restart',
    provider => 'shell',
}
