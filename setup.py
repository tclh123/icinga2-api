from setuptools import setup, find_packages

version = '0.1.2'


requirements = [
    'setuptools',
    # -*- Extra requirements: -*-
    'requests',
]


setup(name='icinga2py',
      version=version,
      description="An icinga2 API client.",
      long_description=open("README.md").read(),
      long_description_content_type='text/markdown',
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      url='https://github.com/tclh123/icinga2-api',
      keywords=['Icinga2', 'API Client'],
      author='Harry Lee',
      author_email='tclh123@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['examples*', 'tests*']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requirements,
)  # NOQA
