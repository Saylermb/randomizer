try:
    from setuptools import setup
except ImportError:
    raise ImportError(
        "setuptools module required, please go to https://pypi.python.org/pypi/setuptools and follow the instructions for installing setuptools")

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='randomizer',
    version='0.10',
    packages=['randomizer'],
    url='',
    license='',
    author='Saylermb',
    author_email='Saylermb@gmail.com',
    description='',
    install_requires=['numpy',],
    long_description=long_description,
    python_requires='>3.6.2'
)
