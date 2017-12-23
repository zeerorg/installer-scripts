from setuptools import setup, find_packages

setup(
    name="Intasker",
    version='0.0.1',
    description="A command line tool to install software",
    author="Rishabh Gupta(zeerorg)",
    packages=find_packages(),
    install_requires=[
        'Click'
    ],
    entry_points="""
        [console_scripts]
        intasker=main:cli
    """
)
