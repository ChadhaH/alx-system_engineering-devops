# fix our stack so that we get to 0 fails

exec {'fix_nginx':
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  provider => shell,
  before   => Exec['restart'],
}

exec {'restarting':
  provider => shell,
  command  => 'sudo service nginx restart',
}
