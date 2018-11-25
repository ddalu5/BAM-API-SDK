from setuptools import setup, find_packages


setup(name='BAM-API-SDK',
      version='0.1',
      description='Small SDK for the new BANk Al-Maghrib API.',
      url='https://github.com/ddalu5/BAM-API-SDK',
      author='Salah OSFOR',
      author_email='osfor.salah@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['tests']),
      test_suite='nose.collector',
      tests_require=['nose'],
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Programming Language :: Python :: 3.4',
      ],
      zip_safe=False)
