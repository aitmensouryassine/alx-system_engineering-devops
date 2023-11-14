# Change the limit of open files by nginx

exec { 'change_ulimit':
  command => sed -i "s/ULIMIT.*/ULIMIT='-n 2000'/g" /etc/default/nginx,
  path    => ['/bin', '/usr/bin']
}