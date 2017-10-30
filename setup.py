#!/usr/bin/env python
from setuptools.command.test import test as TestCommand
import sys
from setuptools import setup

__version__ = "0.0.1"


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    tox_args = None
    test_args = None
    test_suite = None

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


setup(
    name='drf-swagger-yaml',
    version=__version__,
    packages=['drf_swagger_yaml'],
    include_package_data=True,
    url='https://github.com/TriplePoint-Software/drf-swagger-yaml',
    license='Apache License, Version 2.0',
    author='Konstantin Liuterovich',
    author_email='konstantinliuterovich@gmail.com',
    description='Django\'s Drf swagger yaml',
    install_requires=["django>=1.8,<1.11", 'djangorestframework', 'pyyaml'],
    tests_require=["tox", "pyyaml"],
    cmdclass={'test': Tox},
)
