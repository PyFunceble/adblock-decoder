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

Provides the adblock2hosts decoder/converter.

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

from io import TextIOWrapper
from typing import Optional

from adblock_decoder.core.io_base import IOBase


class AdBlock2Hosts(IOBase):
    """
    Provides the core of the adblock2hosts decoder.

    :param input_file:
        The input file to traverse.
    :param aggressive:
        The decoding mode.
    :param output:
        The output file to write.
    :param hosts_ip:
        The IP to preffix each lines with.
    """

    hosts_ip: str = None

    def __init__(
        self,
        input_file: TextIOWrapper,
        aggressive: bool = False,
        output: Optional[TextIOWrapper] = None,
        hosts_ip: str = "0.0.0.0",
    ):
        super().__init__(input_file, aggressive=aggressive, output=output)

        self.hosts_ip = hosts_ip

    def process_conversion(self) -> None:
        """
        Process the actual conversion.
        """

        for line in self.input:
            for converted in self.decode_line(line):
                if self.output:
                    self.output.write(f"{self.hosts_ip} {converted}\n")
                else:
                    print(f"{self.hosts_ip} {converted}")
