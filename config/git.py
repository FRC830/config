#!/usr/bin/env python

import subprocess

def conf(name):
    try:
        return subprocess.check_output('git config --global'.split() + [name])\
               .replace('\n', '').replace('\r', '')
    except subprocess.CalledProcessError:
        return ''

def set_conf(name, value):
    subprocess.call('git config --global'.split() + [name, value])

def run():
    if not conf('user.name'):
        username = util.input('Computer name (e.g. R2, B3): ')
        set_conf('user.name', '830-%s' % username)
        set_conf('user.email', '%s@830.local' % username)
    set_conf('alias.stat', 'status')
    set_conf('alias.st', 'status -s')
    set_conf('alias.co', 'checkout')
    set_conf('push.default', 'simple')
    set_conf('credential.helper', 'wincred')
    
