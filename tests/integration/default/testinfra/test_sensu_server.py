# def test_file_exists(host):
#     foo = host.file('/foo.yml')
#     assert foo.exists
#     assert foo.contains('your')

def test_sensu_is_installed(host):
    sensu = host.package('sensu')
    assert sensu.is_installed


# def test_user_and_group_exist(host):
#     user = host.user('foo')
#     assert user.group == 'foo'
#     assert user.home == '/var/lib/foo'
#
#
# def test_service_is_running_and_enabled(host):
#     foo = host.service('foo')
#     assert foo.is_enabled
#     assert foo.is_running
