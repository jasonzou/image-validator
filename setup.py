from setuptools import setup
# setuptools used instead of distutils.core so that
# dependencies can be handled automatically

# Extract version number from resync/_version.py. Here we
# are very strict about the format of the version string
# as an extra sanity check. (Thanks for comments in
# http://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package )
import re
VERSIONFILE = "iiif_validator/_version.py"
verfilestr = open(VERSIONFILE, "rt").read()
match = re.search(r"^__version__ = '(\d\.\d.\d+(\.\d+)?)'", verfilestr,
                  re.MULTILINE)
if match:
    version = match.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE))

setup(
    name='iiif-validator',
    version=version,
    packages=['iiif_validator', 'iiif_validator.tests'],
    scripts=['iiif-validator.py', 'iiif-validate.py'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",  #is this true? know Linux & OS X ok
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment"
    ],
    author='IIIF Contributors',
    author_email='simeon.warner@cornell.edu',
    description='IIIF Image API Validator',
    long_description=open('README').read(),
    url='http://github.com/IIIF/image-api',
    install_requires=[
        "Pillow>=3.2.0,<4.0.0",  # Pillow 4.0.0 drops python 2.6 support
        "bottle>=0.12.1,<0.13",  # Bottle 0.13 drops python 2.6 support
        "python-magic>=0.4.12",
        "lxml>=3.7.0"
    ],
    test_suite="tests",
    tests_require=["mock"])
