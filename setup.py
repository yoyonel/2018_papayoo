# -*- encoding: utf-8 -*-
from setuptools import setup

# https://docs.python.org/3/distutils/setupscript.html
setup(
    name='papayoo',
    version='0.1.0',
    license='None',
    description='',
    author='Lionel ATTY',
    author_email='lionel.atty@gmail.com',
    url='',
    package_dir={'': 'src'},
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    install_requires=[
        "attrs",
    ],
    entry_points={
        'console_scripts': [
            'papayoo = main:main',
        ]
    },
    cmdclass={},
    python_requires='>=3.6'
)
