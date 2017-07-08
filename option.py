#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click


@click.command()
@click.option('-n', '--name', default='World', help='Greeting partner')
def cmd(name):
    """
    Show greeting message.
    :type name: str
    """
    msg = 'Hello, {name}!'.format(name=name)
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
