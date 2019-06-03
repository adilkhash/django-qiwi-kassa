from setuptools import setup

install_requires = [
    'django>=2.0',
    'qiwi-payments==0.1',
]

setup(
    name='django-qiwi-kassa',
    version='0.2',
    packages=['qiwi_kassa'],
    url='https://github.com/adilkhash/django-qiwi-kassa',
    license='MIT',
    author='Adylzhan Khashtamov',
    author_email='adil.khashtamov@gmail.com',
    description='Django App for Qiwi Kassa',
    install_requires=install_requires,
)
