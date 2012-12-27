## Installation

Celerity is meant to be a small, self-contained script.  You can download/clone the repo if you want, but all you need is a copy of the 'main.py' file.  An easy solution to this is:

   alias celerity='python <(curl -s https://raw.github.com/dukerson/celerity/master/main.py)'
   
(Please note that if you do this,  you're downloading an (admittedly small) file from GitHub, so you're putting a small strain on them *and* things are gonna take a few seconds longer.

## Usage

To post a file:

    celerity post [<filename>]
    > Uploaded to http://hastebin.com/<id>
    
You can post multiple files simultaneously by simply listing them, such as:

    celerity post fileone.py filetwo.py
    
And to retrieve a hastebin:

    celerity get <id> [<target>]