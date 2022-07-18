anekos
================

.. image:: https://img.shields.io/pypi/v/anekos
   :target: https://pypi.python.org/pypi/anekos
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/anekos
   :target: https://pypi.python.org/pypi/anekos
   :alt: PyPI supported Python versions
.. image:: https://img.shields.io/pypi/dd/anekos
   :target: https://pypi.python.org/pypi/anekos
   :alt: PyPI Downloads
.. image:: https://img.shields.io/pypi/l/anekos
   :target: https://pypi.python.org/pypi/anekos
   :alt: PyPI License

   An unofficial asynchronous wrapper for nekos.life API

Features
========

-  You can download the images! (using
   `aiofile <https://pypi.org/project/aiofile>`__)
-  Easy to use with an object-oriented design.
- Regularly updated with new API updates. (as of 11/06/2022)

Install
=======

.. code:: sh

   # Linux/macOS
   python3 -m pip install -U anekos

   # Windows
   py -3 -m pip install -U anekos

To install the development version, do the following:

.. code:: sh

    $ git clone https://github.com/Nekos-life/Async-nekos.life-wrapper.git
    $ cd Async-nekos.life-wrapper
    $ python3 -m pip install -U . 

Optional Packages
-----------------

-  `aiodns <https://pypi.org/project/aiodns>`__,
   `brotlipy <https://pypi.org/project/brotlipy>`__,
   `cchardet <https://pypi.org/project/cchardet>`__ (for aiohttp
   speedup)
-  `orjson <https://pypi.org/project/orjson>`__ (for json speedup)

Quick Example
=============

.. code:: py

   from nekos import NekosLifeClient, SFWImageTags
   from asyncio import get_event_loop

   client = NekosLifeClient()


   async def main():
       result = await client.image(SFWImageTags.WALLPAPER)
       print(result.url)


   loop = get_event_loop()
   loop.run_until_complete(main())

Links
=====
-  `Issues <https://github.com/Async-nekos.life-wrapper/issues>`__
