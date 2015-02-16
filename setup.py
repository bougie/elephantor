from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='elephant',
      version='0.1',
      description="Duplicity frontend",
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Archiving :: Backup',
      ],
      keyworkds='duplicity backup rsync ftp unison sftp',
      url='https://github.com/bougie/elephant',
      author='David Hymonnet',
      author_email='bougie@appartland.eu',
      license='BSD',
      scripts=['bin/elephant'],
      data_files=[('/etc/elephant/', ['config/config.sample.py'])],
      include_package_data=True,
      zip_safe=False)
