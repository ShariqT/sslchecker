from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name='sslcheck',
  version='0.1.1',
  packages=['sslcheck'],
  author = "Shariq Torres",
  description = "Check the status of any SSL Certificate in a Request-like API",
  author_email="shariq.torres@gmail.com",
  test_require=['pytest'],
  setup_requires=['pytest-runner'],
  license='GPL-2.0',
  long_description=long_description,
  long_description_content_type='text/markdown'
)