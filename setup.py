from setuptools import setup, find_packages

packages = find_packages()

setup(
    author="yutiansut && somewheve",
    name="quantdata",
    description="data support of full quant platform",
    packages=packages,
    install_requires=['pandas', 'tqsdk'],
)
