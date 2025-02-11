from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name='ssldatechecker',
  version='0.1.3',
  packages=['ssldatechecker'],
  author = "Shariq Torres",
  url='https://github.com/ShariqT/sslchecker',
  description = "Check the status of SSL certificates, mainly the exipiration date",
  author_email="shariq.torres@gmail.com",
  test_require=['pytest'],
  setup_requires=['pytest-runner'],
  license='GPL-2.0',
  long_description=long_description,
  long_description_content_type='text/markdown',
  keywords='SSL OpenSSL x509 certificates',
  classifiers = [
    'Intended Audience :: Information Technology',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3.11',
    'Natural Language :: English',
  ],
  python_requires='>=3.9'

)