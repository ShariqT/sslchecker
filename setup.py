from setuptools import setup

setup(
  name='sslcheck',
  version='0.1.0',
  packages=['sslcheck'],
  author = "Shariq Torres",
  description = "Check the status of any SSL Certificate in a Request-like API",
  author_email="shariq.torres@gmail.com",
  test_require=['pytest'],
  setup_requires=['pytest-runner'],
  license='GPL-2.0'
)