#! /usr/bin/env python
import sys, os, argparse, importlib

class Util:
    def input(self, prompt=''):
        try:
            return raw_input(prompt)
        except NameError:
            return input(prompt)

parser = argparse.ArgumentParser();
parser.add_argument('scripts', nargs='*')
parser.add_argument('-a', '--all', action='store_true')
args = parser.parse_args()

files = args.scripts
valid = map(lambda x: x.replace('.py', ''),
        filter(lambda f: f.endswith('.py') and not f.startswith('__'),
        os.listdir('config')))

run = []
if args.all:
    run = valid
else:
    for f in files:
        if not f in valid:
            raise ValueError(f + ': not found')
        run.append(f)

cwd = os.getcwd()
for f in run:
    os.chdir(cwd)
    print('* Running script %s' % f)
    module = importlib.import_module('config.%s' % f)
    if not hasattr(module, 'run'):
        print('Missing run()')
        continue
    module.util = Util()
    module.run()

    
