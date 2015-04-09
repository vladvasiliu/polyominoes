import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
VERSION = open(os.path.join(os.path.dirname(__file__), 'VERSION')).read().splitlines()[0]

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
        name='polyominoes',
        version=VERSION,
        packages=['polyominoes'],
        include_package_data=True,
        license='GPLv2',
        description='Polyominoes puzzle.',
        long_description=README,
        author='Vlad VASILIU',
        author_email='vladvasiliun@yahoo.fr',
        install_requires=[],
        tests_require=[
                'nose',
            ],
        classifiers=[
                'Operating System :: OS Independent',
                'Programming Language :: Python',
            ],
        test_suite='polyominoes'
    )

