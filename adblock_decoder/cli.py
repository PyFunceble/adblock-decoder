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


    MIT License

    Copyright (c) 2019, 2020 PyFunceble
    Copyright (c) 2017, 2018, 2019, 2020 Nissar Chababy

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

import argparse

from colorama import Fore, Style

from .core import AdBlock2Hosts, AdBlock2Plain


def adblock2plain():
    """
    Provides the CLI entrypoint of the adblock2plain tool.
    """

    if __name__ == "adblock_decoder.cli":
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


def adblock2host():
    """
    Provides the CLI entrypoint of the adblock2hosts tool.
    """

    if __name__ == "adblock_decoder.cli":
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
