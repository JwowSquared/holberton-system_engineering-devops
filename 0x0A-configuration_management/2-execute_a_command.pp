# using puppet exec, execute pkill on killmenow

exec { 'pkill killmenow':
  command => '/usr/bin/pkill -f /killmenow'
}
