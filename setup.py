#!/usr/bin/env python
from setuptools import setup

name = 'credstash'
version = '1.16.0'

setup(
    name=name,
    version=version,
    description='A utility for managing secrets in the cloud using AWS KMS and DynamoDB',
    license='Apache2',
    url="https://github.com/fugue/credstash",
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
    ],
    scripts=['credstash.py'],
    py_modules=['credstash'],
    install_requires=[
        'cryptography>=2.1',
        'boto3>=1.1.1',
    ],
    extras_require={
        'YAML': ['PyYAML>=3.10']
    },
    entry_points={
        'console_scripts': [
            'credstash = credstash:main'
        ]
    },
    setup_requires=[
        'nose>=1.3.6',
    ],
)
