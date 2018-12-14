from setuptools import setup

setup(name='iot-valley-counter-api',
      version='1.0',
      description='API for iot-valley counter website',
      url='http://github.com/workooz/iot-valley-counter-api',
      author='Cedric Badmington',
      author_email='cedric.badmington@gmail.com',
      license='MIT',
      packages=['iot-valley-counter-api'],
      install_requires=[
          'flask', 'flask-restplus', 'flask-sqlalchemy'
      ],
      zip_safe=False)
