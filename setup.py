from setuptools import setup, find_packages

packages = find_packages()

setup(
    author="yutiansut && somewheve",
    name="quantdata",
    version=0.1,
    description="quant data support of full platform",
    packages=packages,
    install_requires=['pandas','tqsdk','ctpbee'],
)
