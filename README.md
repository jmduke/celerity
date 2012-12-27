I use a PC laptop, Mac laptop, and a Linux box.  Sending files between all three of them are a pain, and there are a lot of use-cases where Dropbox or something similar isn't particularly feasible either.

As per the Unix philosophy:

> Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.

Celerity leverages the amazing [Hastebin](http://www.hastebin.com) to quickly upload and download code.  I created it in a desire to optimize my experience, and I felt it worthwhile enough to clean and display to others, in hopes that it makes your workflow a little bit cleaner!

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
    
## Dependencies

Python 2.x/3 (I haven't tested it on 3, but none of the libraries I use are deprecated) and a working internet connection!

