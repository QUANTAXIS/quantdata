from setuptools import setup, find_packages

packages = find_packages()

setup(
    author="yutiansut && somewheve",
    name="quantdata",
    description="quant data support of full platform",
    packages=packages,
    install_requires=['pandas'],
)
