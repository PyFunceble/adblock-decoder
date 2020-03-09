adblock-decoder
===============

A set of tools for the decoding and conversion of AdBlock and filter lists.
The decoder itself is part of the PyFunceble project.

Installation
------------

::

    $ pip install --user adblock-decoder

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

    MIT License

    Copyright (c) 2020 PyFunceble
    Copyright (c) 2020 Nissar Chababy

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
