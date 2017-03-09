#!/usr/bin/env python
import os

VERSION = '1.0'

def run_setup():
    DISTNAME = "iterm2_display"
    DESCRIPTION = "inline in iterm2"

    from setuptools import setup

    setup(
        name = DISTNAME,
        description = DESCRIPTION,
        version = VERSION,
        author_email='tobibaum@gmail.com',
        packages = ["iterm2_display"],
        include_package_data=True,
        zip_safe=False,
    )

if __name__=='__main__':
    run_setup()
