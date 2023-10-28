# astra-document

Provides you with high level functions to interact with the Datastax Astra API's HTTP verbs

## Installation

Since PyPi has obbligaatory 2FA with TOTP, I chose to just share the package on github. Clone it in your project
and just import it has a package:

    from astra_document import astra

Then you need the necessary envoirnement variables, which are provided to you in the Astra GUI...

![Where to find env](https://bafkreih37heaxteuhi2psg5un3plr7sj6sxbj473qgliyrtrswp2zxkfee.ipfs.nftstorage.link/)

...and, if you prefer you can store them in an .env file and load them with init:

    astra.init()