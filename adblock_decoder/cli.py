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

Provides the CLI entrypoints.

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


    Copyright 2017, 2018, 2019, 2020, 2021 Nissar Chababy

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

import argparse

from colorama import Fore, Style

from .core import AdBlock2Hosts, AdBlock2Plain


def adblock2plain() -> None:
    """
    Provides the CLI entrypoint of the adblock2plain tool.
    """

    parser = argparse.ArgumentParser(
        description="An AdBlock2plain (text) converter.",
        epilog=f"Crafted with {Fore.RED}{Style.BRIGHT}♥{Style.RESET_ALL} "
        f"by {Fore.YELLOW}{Style.BRIGHT}Nissar Chababy (Funilrys){Style.RESET_ALL}!",
        add_help=True,
    )

    parser.add_argument(
        "input_file",
        type=argparse.FileType("r", encoding="utf-8"),
        help="The input file to work with.",
    )

    parser.add_argument(
        "--aggressive",
        action="store_true",
        help="[USE AT YOUR OWN RISK AS IT IS EXPERIMENTAL] Activates the extraction "
        "of everything regardless of the interpretation of AdBlock/UBlock.",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=argparse.FileType("w", encoding="utf-8"),
        help="The file to write to.",
    )

    args = parser.parse_args()

    AdBlock2Plain(
        args.input_file, args.aggressive, output=args.output
    ).process_conversion()


def adblock2host() -> None:
    """
    Provides the CLI entrypoint of the adblock2hosts tool.
    """

    parser = argparse.ArgumentParser(
        description="An AdBlock2hosts converter.",
        epilog=f"Crafted with {Fore.RED}{Style.BRIGHT}♥{Style.RESET_ALL} "
        f"by {Fore.YELLOW}{Style.BRIGHT}Nissar Chababy (Funilrys){Style.RESET_ALL}!",
        add_help=True,
    )

    parser.add_argument(
        "input_file",
        type=argparse.FileType("r"),
        help="The input file to work with.",
    )

    parser.add_argument(
        "--aggressive",
        action="store_true",
        help="[USE AT YOUR OWN RISK AS IT IS EXPERIMENTAL] Activates the extraction "
        "of everything regardless of the interpretation of AdBlock/UBlock.",
    )

    parser.add_argument(
        "--ip",
        type=str,
        help="Sets the IP to use while generating the hosts file.",
        default="0.0.0.0",
    )

    parser.add_argument(
        "-o", "--output", type=argparse.FileType("w"), help="The file to write to."
    )

    args = parser.parse_args()

    AdBlock2Hosts(
        args.input_file, args.aggressive, output=args.output, ip=args.ip
    ).process_conversion()
