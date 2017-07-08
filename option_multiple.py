#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click


@click.command()
@click.option('-n', '--name', default='World', help='Greeting partner', multiple=True)
def cmd(name):
    """
    Show greeting message.
    :type name: list
    """
    names = ' '.join(name)
    msg = 'Hello, {names}!'.format(names=names)
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
