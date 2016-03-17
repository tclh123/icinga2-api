from setuptools import setup, find_packages

version = '0.1.0'


requirements = [
    'setuptools',
    # -*- Extra requirements: -*-
    'requests',
]


setup(name='icinga2-api',
      version=version,
      description="An icinga2 API client.",
      long_description=open("README.md").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords='',
      author='Harry Lee',
      author_email='tclh123@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['examples*', 'tests*']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requirements,
)
