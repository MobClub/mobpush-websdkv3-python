from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="mobPushSdkV3",
    version="2.0.0",
    author="yylu",
    author_email="yylu@yoozoo.com",
    description="Python Framework.",
    license="MIT",
    url="https://github.com/MobClub/mobpush-websdkv3-python",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'requests>=2.24.0',  # 所需要包的版本号
    ],
    zip_safe=True,
)
