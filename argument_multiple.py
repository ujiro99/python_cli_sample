#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click


@click.command()
@click.argument('src', nargs=-1)
@click.argument('dst', nargs=1)
def cmd(src, dst):
    """
    :type src: list
    :type dst: str
    """
    for i in src:
        msg = 'move from {src} to {dst}'.format(src=i, dst=dst)
        click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
