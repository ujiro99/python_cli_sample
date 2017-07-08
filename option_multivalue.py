#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click


@click.command()
@click.option('-n', '--names', nargs=2)
def cmd(names):
    """
    Show greeting message.
    :type names: str
    """
    click.echo('Hello, %s and %s!' % names)


def main():
    cmd()


if __name__ == '__main__':
    main()
