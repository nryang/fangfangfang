# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

from setuptools import setup, find_packages

NAME = 'fangfangfang'
VERSION = '1.0.0'

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements


def load_requirements(fname):
    reqs = parse_requirements(fname, session='test')
    return [str(ir.req) for ir in reqs]


setup(
    name=NAME,
    version=VERSION,
    description='A web application that allows you to defang and refang URLs in text.',
    author_email='nryang@users.noreply.github.com',
    url='https://github.com/nryang/fangfangfang',
    keywords=['defang', 'refang'],
    python_requires='>3.6',
    install_requires=load_requirements('requirements.txt'),
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': ['fangfangfang=fangfangfang.__main__:main']},
    long_description="""\
    A web application that allows you to defang and refang URLs in text.
    """
)
