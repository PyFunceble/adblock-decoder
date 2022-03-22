"""
The tool to check the availability or syntax of domains, IPv4, IPv6 or URL.

::


    ██████╗ ██╗   ██╗███████╗██╗   ██╗███╗   ██╗ ██████╗███████╗██████╗ ██╗     ███████╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║████╗  ██║██╔════╝██╔════╝██╔══██╗██║     ██╔════╝
    ██████╔╝ ╚████╔╝ █████╗  ██║   ██║██╔██╗ ██║██║     █████╗  ██████╔╝██║     █████╗
    ██╔═══╝   ╚██╔╝  ██╔══╝  ██║   ██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗██║     ██╔══╝
    ██║        ██║   ██║     ╚██████╔╝██║ ╚████║╚██████╗███████╗██████╔╝███████╗███████╗
    ╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ ╚══════╝╚══════╝

This project is part of the PyFunceble project and infrastructure.

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Special thanks:
    https://pyfunceble.github.io/special-thanks.html

Contributors:
    https://pyfunceble.github.io/contributors.html

Project link:
    https://github.com/funilrys/PyFunceble

Project documentation:
    https://pyfunceble.readthedocs.io/en/dev/

Project homepage:
    https://pyfunceble.github.io/

License:
::


    Copyright 2017, 2018, 2019, 2020, 2021, 2022 Nissar Chababy

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from re import compile as comp

from setuptools import find_packages, setup


def get_requirements():
    """
    Extracts all requirements from requirements.txt.
    """

    with open("requirements.txt") as file:
        requirements = file.read().splitlines()

    return requirements


def get_version():
    """
    Extracts the version from adblock_decoder/__init__.py
    """

    to_match = comp(r'__version__\s=\s"(.*)"')

    return to_match.findall(
        open("adblock_decoder/__init__.py", encoding="utf-8").read()
    )[0]


def get_long_description():
    """
    Provides the long description.
    """

    return open("README.rst", encoding="utf-8").read()


if __name__ == "__main__":
    setup(
        name="adblock-decoder",
        version=get_version(),
        python_requires=">=3.6, <4",
        install_requires=get_requirements(),
        description="A set of tool for the decoding and conversion of AdBlock and Filter Lists.",
        author="funilrys",
        author_email="contact@funilrys.com",
        license="Apache 2.0",
        url="https://github.com/PyFunceble/adblock-decoder",
        platforms=["any"],
        packages=find_packages(),
        long_description=get_long_description(),
        project_urls={
            "Funding": "https://github.com/sponsors/funilrys",
            "Source": "https://github.com/PyFunceble/adblock-decoder",
            "Tracker": "https://github.com/funilrys/PyFunceble/issues",
        },
        keywords=["PyFunceble", "AdBlock", "Filter", "list", "decoder"],
        classifiers=[
            "Environment :: Console",
            "Topic :: Internet",
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Intended Audience :: Information Technology",
            "Intended Audience :: System Administrators",
            "Intended Audience :: Other Audience",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved",
        ],
        entry_points={
            "console_scripts": [
                "adblock2hosts=adblock_decoder.cli:adblock2host",
                "adblock2plain=adblock_decoder.cli:adblock2plain",
            ]
        },
    )
