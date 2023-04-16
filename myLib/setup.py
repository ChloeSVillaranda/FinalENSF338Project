from setuptools import setup, find_packages

setup( 
    name='myLib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List the dependencies required by your package here
        # For example, if your package requires NumPy and Pandas, you can list them like this:
        'queue'
    ],
    author='Maham Jamal and Chloe Villaranda',
    author_email='maham.jamal@ucalgary.ca',
    description='library of datastructures including linear datastructures and trees',
    url='https://github.com/yourusername/myLib',
    )

