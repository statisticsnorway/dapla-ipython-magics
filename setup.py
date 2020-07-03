import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


DEPENDENCIES = [
    'ipython>=4.0.2'
    'nose'
    'requests'
    'ipykernel>=4.2.2'
    'notebook>=4.2'
    'tornado>=4'
]

setup(
    name="ssb-ipython-magics",
    version="0.0.2",
    url="https://github.com/statisticsnorway/dapla-ipython-magics",
    license='MIT',

    author="Statistics Norway",
    author_email="bjorn.skaar@ssb.no",

    description="IPython magics for dapla.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",

    packages=find_packages(exclude=('tests', 'examples',)),

    install_requires=DEPENDENCIES,

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
