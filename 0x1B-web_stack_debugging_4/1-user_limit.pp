# script that removes limits placed on user holberton
file { '/etc/security/limits.conf':
  content => '',
}
