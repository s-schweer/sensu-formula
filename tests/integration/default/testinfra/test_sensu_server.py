def test_config_directory_exists(host):
    conf_d = host.file('/etc/sensu/conf.d')
    assert conf_d.exists
    assert conf_d.is_directory

def test_sensu_is_installed(host):
    sensu = host.package('sensu')
    assert sensu.is_installed


def test_user_and_group_exist(host):
    user = host.user('sensu')
    assert user.group == 'sensu'
    assert user.home == '/opt/sensu'

def test_service_is_running_and_enabled(host):
    sensu_server = host.service('sensu-server')
    assert sensu_server.is_enabled
    assert sensu_server.is_running
