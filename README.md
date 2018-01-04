# shell-gtranslate
A simple tool to translate any text from command line, by using the library [googletrans](https://github.com/ssut/py-googletrans)

## Installation
The tool requires only python3 and can be installed with pip

`$ pip install shell-gtranslate`

## Use
The tool works with command `tl`, all you need to do is type in your terminal `tl 'your text'` and voila!

## Available commands
`$ tl 'your text'` - use the translater language recognition for the origin language and translate to english

`$ tl 'your text' -s 'origin-language'` - translate to english

`$ tl 'your text' -d 'destiny-language'`- use the translater language recognition for the origin language and translate to the language that you choose

`$ tl 'your text' -s 'origin-language' -d 'destiny-language'` - translate to the language that you choose (more accuracy)

Also the flag `-v` activate the verbose mode then more information about the text is showed

## Upcoming commands
`$ tl --config -s 'default-origin-language'`

`$ tl --config -d default-desireble-language`
