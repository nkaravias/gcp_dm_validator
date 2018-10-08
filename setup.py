import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="gcp_dm_validator",
    version="0.0.1",
    author="Nikolas Karavias",
    author_email="karavias.nikos@gmail.com",
    description=("Validate business rules for GCP Cloud YAML configuration"),
    license="MIT",
    keywords="python yaml validation googlecloud gcp",
    packages=['gcp-dm-validator tests'],
    long_description=read('README.md'),
    classifiers=[
        "DeploymentManager :: Utilities"
    ]
)
