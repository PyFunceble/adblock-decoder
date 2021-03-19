AdBlock Filter List Decoder
===========================

A set of tools for the decoding and conversion of AdBlock and filter lists.
The decoder itself is part of the PyFunceble project.

Installation
------------

::

    $ pip install --user adblock-decoder

Update
------

::

    $ pip install --user --upgrade adblock-decoder

Python API
----------

If you want to use the decoder in your own Python modules or infrastructure,
you may use the PyFunceble project to access the decoder.


::

    from PyFunceble.converter.adblock_input_line2subject import AdblockInputLine2Subject

    to_decode = ["||example.com^", "||example.net^"]

    decoder = AdblockInputLine2Subject()
    decoder.aggressive = False

    decoded = set()

    for line in to_decode:
        # One shot method.
        decoded.update(decoder.set_data_to_convert(line).get_converted())

        # Step by step method
        decoder.set_data_to_convert(line)
        decoded.update(decoder.get_converted())

    print("Decoded:", decoded)

Tools
-----

:code:`adblock2hosts`
^^^^^^^^^^^^^^^^^^^^^

A tool to convert adblock or filter lists to hosts format.

Usage
"""""

::

    usage: adblock2hosts [-h] [--aggressive] [--ip IP] [-o OUTPUT] input_file

    An AdBlock2hosts converter.

    positional arguments:
        input_file            The input file to work with.

    optional arguments:
        -h, --help            show this help message and exit
        --aggressive          [USE AT YOUR OWN RISK AS IT IS EXPERIMENTAL] Activates the extraction of everything regardless of the interpretation of AdBlock/UBlock.
        --ip IP               Sets the IP to use while generating the hosts file.
        -o OUTPUT, --output OUTPUT
                                The file to write to.

    Crafted with ♥ by Nissar Chababy (Funilrys)!

:code:`adblock2plain`
^^^^^^^^^^^^^^^^^^^^^

A tool to convert adblock or filter lists to plain text format.


Usage
"""""

::

    usage: adblock2plain [-h] [--aggressive] [-o OUTPUT] input_file

    An AdBlock2plain (text) converter.

    positional arguments:
        input_file            The input file to work with.

    optional arguments:
        -h, --help            show this help message and exit
        --aggressive          [USE AT YOUR OWN RISK AS IT IS EXPERIMENTAL] Activates the extraction of everything regardless of the interpretation of AdBlock/UBlock.
        -o OUTPUT, --output OUTPUT
                                The file to write to.

    Crafted with ♥ by Nissar Chababy (Funilrys)!


License
-------

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
