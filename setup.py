from setuptools import setup, find_packages

setup(
    name='montecarlo',
    version='1.0.0',
    url='https://github.com/aowen18/amo9f_ds5100_montecarlo',
    author='Alexa Owen',
    author_email='amo9f@virginia.edu',
    description='Package allows the user to create and roll "die" with different weights, '
                'allows the user to roll multiple similar die, and then analyze the results of the die rolls.',
    packages=find_packages(),
    install_requires=['pandas >= 2.0.3', 'numpy >= 1.22.4']
)