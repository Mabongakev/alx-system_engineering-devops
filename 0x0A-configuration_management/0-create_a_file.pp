# create a file
file { '/tmp/school':
    mode => '0744',
    mode => 'www-data'
    group => 'www-data'
    contains => 'I love Puppet'
}
