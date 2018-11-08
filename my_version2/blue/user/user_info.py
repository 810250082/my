from . import user
from my_version2.version import version


@user.route('/info')
@version
def info(*args, **kwargs):
    a = 1
    return 'ok la'
