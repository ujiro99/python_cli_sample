#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click


@click.command()
@click.option('-n', '--name', prompt=True, help='Greeting partner')
def cmd(name):
    """
    Show greeting message.
    :type name: str
    """
    click.echo('Hello, %s!' % name)


def main():
    cmd()


if __name__ == '__main__':
    main()
