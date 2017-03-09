"""
a quick and simple script to display an inline image inside an iterm2 shell.
also works with tmux :)
"""

import os
import sys
import base64

def create_inline_image_cmd(input, height=5, is_file=True):
    # determine whether this runs out of tmux
    in_tmux = 'TMUX' in os.environ

    # load the file and encode it
    if is_file:
        with open(input) as fh:
            file_content = fh.read()
            b64img = base64.b64encode(file_content)
        file_name = input
    else:
        b64img = input
        file_name = 'buffer'
        
    if in_tmux:
        # this is the tmux escape seq
        cmd_str = "\033Ptmux;\033\033]"
    else:
        cmd_str = "\033]"

    # special iterm2 image inline escape syntax:
    # https://www.iterm2.com/documentation-images.html
    cmd_str += '1337;File=%s'%file_name # does not really matter I don't think
    cmd_str += ';height=%d'%height # how many lines?
    cmd_str += ';inline=1' # always set to true!
    cmd_str += ':'
    cmd_str += b64img # the main image meat as base64

    # and complete with the endmarker
    if in_tmux:
        cmd_str += '\a\033\\'
        # something still weird with the cursor, so add some newlines to not
        # overwrite the image.
        cmd_str += '\n'*(height-1)
    else:
        cmd_str += '\a'

    return cmd_str

if __name__=='__main__':
    # parse input
    if len(sys.argv) < 2:
        print 'usage: ./inline_img.py <img_file> [<height>]'
        sys.exit()

    file_name = sys.argv[1]
    if len(sys.argv) > 2:
        height = int(sys.argv[2])
    else:
        height = 5

    # for tmux, we need to append some special escapes, so this python program can
    # talk to iterm directly.
    in_tmux = 'TMUX' in os.environ
    if in_tmux:
        os.system('clear')

    cmd_str = create_inline_image_cmd(file_name, height=height)
    print cmd_str
