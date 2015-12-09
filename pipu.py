import pip
from subprocess import call

import colorama
colorama.init()

for dist in pip.get_installed_distributions():
    print(colorama.Fore.RED + 'Upgrading {0}'.format(dist.project_name) + colorama.Fore.BLACK)
    call('pip install --upgrade {0} --user'.format(dist.project_name), shell=True)
