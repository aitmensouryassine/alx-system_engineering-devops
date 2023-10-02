# task of creating a custom HTTP header response with Puppet

exec { 'update':
  command     => 'sudo apt-get -y update',
  provider => shell,
}

-> package { 'nginx':
  ensure   => present,
  provider => 'apt'
}

-> file_line { 'add custom HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $HOSTNAME;'
}

-> exec { 'restart':
  command => 'sudo service nginx restart',
  provider => shell,
}
