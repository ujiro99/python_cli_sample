#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click


@click.command()
@click.option('--age', type=click.IntRange(0, 100))
def cmd(age):
    msg = 'Your age: {age}'.format(age=age)
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
