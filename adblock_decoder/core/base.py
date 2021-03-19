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

Porivdes the base of all cores.

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

from typing import Iterable, Optional

from PyFunceble.converter.adblock_input_line2subject import AdblockInputLine2Subject


class BaseCore:
    """
    Provides the base of all cores.

    :param aggressive:
        Activates or disable the decode in an aggressive matter. When active,
        the decoder will try to decode as much as possible without taking the
        basic of adblock filter list codex into consideration.
    """

    _aggressive: bool = False

    decoder: Optional[AdblockInputLine2Subject] = None

    def __init__(self, aggressive: Optional[bool] = None):
        if aggressive is not None:
            self.aggressive = aggressive

        self.decoder = AdblockInputLine2Subject()

    @property
    def aggressive(self) -> bool:
        """
        Provides the current state of the aggressive attribute.
        """

        return self.decoder.aggressive

    @aggressive.setter
    def aggressive(self, value: bool) -> None:
        """
        Overwrites the current state of the aggressive attribute.

        :param value:
            The value to set.
        """

        self.decoder.aggressive = value

    def set_aggressive(self, value: bool) -> "BaseCore":
        """
        Overwrites the current state of the aggressive attribute.

        :param value:
            The value to set.
        """

        self.aggressive = value

        return self

    def decode_line(self, line: str) -> Iterable[str]:
        """
        Decodes a single line.

        :param line:
            The line to decode.
        """

        return (
            x for x in self.decoder.set_data_to_convert(line.strip()).get_converted()
        )
