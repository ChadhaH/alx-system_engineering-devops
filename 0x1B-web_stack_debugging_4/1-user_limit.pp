# Change the OS configuration so that it is possible to login
# with the holberton user and open a file without any error message

exec {'soft_limit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['replace-2'],
}

exec {'hard_limit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
