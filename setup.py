from setuptools import setup

setup(name='MinimumBoundingBox',
      version='0.0.0',
      license='MIT',
      description='Finds the minimum bounding box from a point cloud.',
      author='William Rusnack',
      author_email='williamrusnack@gmail.com',
      url='https://github.com/BebeSparkelSparkel/MinimumBoundingBox',
      classifiers=['Development Status :: 2 - Pre-Alpha', 'Programming Language :: Python :: 3'],
      py_modules=['MinimumBoundingBox'],
      install_requires=['scipy==0.18.1', 'numpy==1.11.2'],
     )
