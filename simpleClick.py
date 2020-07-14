import click
import random

@click.group()
def main():
    pass

@main.command()
@click.argument('text')
def reverse(text):
    """Reverse a text"""
    click.echo(text[::-1])

@main.command()
@click.argument('text')
def leet(text):
    """Leet a text"""
    chars = {'a':'4','b':'13'}
    getchar = lambda c: chars[c] if c in chars else c
    click.echo(''.join(getchar(c) for c in text))

@main.command()
@click.argument('myword')
def shufflize(myword):
    """Shufflize a Text"""
    click.echo(''.join(random.sample(myword, len(myword))))

if __name__=='__main__':
    main()