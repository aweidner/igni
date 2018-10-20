from distutils.core import setup

setup(
  name='igni',
  packages=['igni'],
  version='0.2.0',
  license='MIT',
  description='Client for gitignore.io with shell completions',
  entry_points={
    'console_scripts': ['igni=igni.__main__:main']
  },
  author='Adam Weidner',
  author_email='aweidner6993@gmail.com',
  url='https://github.com/aweidner/igni',
  download_url='https://github.com/aweidner/igni/archive/0.2.0.tar.gz',
  keywords=['gitignore', 'gitignore.io'],
  install_requires=[
    'requests'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ]
)
