#!/usr/bin/env python
"""print `.env` as json"""
# -*- coding: utf-8 -*-
import json
import sys
import click
import env2json

MODULE_NAME = "env2json"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s path' % MODULE_NAME


@click.command()
@click.argument('path', required=True)
def _cli(path):
    data = {}
    lines = open(path).read().splitlines()
    for line_no,line in enumerate(lines,0):
        try:
            data.update(env2json.parse(line))
        except ValueError:
            raise ValueError(".env:%s\n%s" % (line_no,line))
    print(json.dumps(data, indent=2, sort_keys=True))

if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
