# create a file in /tmp using puppet

file { '/tmp/school':
  content => 'I love Puppet',
  owner   => 'www-dat',
  group   => 'www-data',
  mode    => '0744',
}
