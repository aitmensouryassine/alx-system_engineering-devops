# Fix typo: change extention from .phpp to .php
# file: /var/www/html/wp-settings.php

exec { 'fix_ext_typo':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin']
}