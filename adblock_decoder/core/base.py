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
