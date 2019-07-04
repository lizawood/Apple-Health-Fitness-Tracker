from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='myFitness',
    version='0.2',
    packages=find_packages(exclude=['*test*']),
    license='MIT',
    description='This package provides some basic tools to analyze the health data in a csv file downloaded from Apple Health.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/lizawood/Apple-Health-Fitness-Tracker',
    author='Liza Wood',
    author_email='liza.4.bc@gmail.com'
)
