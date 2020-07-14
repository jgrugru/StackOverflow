import click

@click.command()
@click.option('--name','-n')
def main(name):
    # click.echo(click.style((f"My name is {name}"), fg='blue', bg='white',bold=True))
    click.secho(f"My name is {name}", fg='white', bg='black',bold=False)
if __name__=='__main__':
    main()