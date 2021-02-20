# script that removes the hard limit of 15 max open files
exec { 'fix':
    command  => 'sed  "$d" /etc/default/nginx; sudo service nginx restart',
    provider => 'shell',
}
