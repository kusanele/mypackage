from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('READme.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<kusanele>/<mypackage>',
    author='<marble kusanele Mpofu>',
    author_email='<mpofukusanele@gmail.com>'
)