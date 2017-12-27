from setuptools import setup, find_packages

setup(
    name='nono-line',
    version='0.0.2',
    packages=find_packages(exclude=['test']),
    url='https://github.com/withsmilo/nonoLINE',
    license='MIT',
    author='Sungjun, Kim',
    author_email='smilolistener@gmail.com',
    description='A simple notification helper to send messages to LINE Notify',
    keywords=['LINE', 'LINE Notify', 'notification', 'nonoLINE', 'nono-line'],
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License'],
    install_requires=['requests', 'requests-futures']
)

