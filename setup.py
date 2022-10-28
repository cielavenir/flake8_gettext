from setuptools import setup
versionContext = {}
with open('flake8_gettext/version.py') as f:
    exec(f.read(), versionContext)

import sys

setup(
    name='flake8_gettext',
    description='flake8_gettext',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    version=versionContext['__version__'],
    url='https://github.com/cielavenir/flake8_gettext',
    license='0BSD',
    author='cielavenir',
    author_email='cielartisan@gmail.com',
    packages=['flake8_gettext'],
    keywords='flake8',
    entry_points={'flake8.extension': ['GT01 = flake8_gettext.checker:GettextChecker']},
    zip_safe=False,
    # include_package_data=True,
    platforms='any',
    install_requires=['flake8>=3.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
