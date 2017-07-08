#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click


@click.command()
@click.option('--language', type=click.Choice(['Japanese', 'English']))
def cmd(language):
    msg = 'Chose: {name}'.format(name=language)
    click.echo(msg)


def main():
    cmd()


if __name__ == '__main__':
    main()
