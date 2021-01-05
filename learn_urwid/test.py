import click


@click.command()
def hello():
    click.echo("hello World!")

# hello()


# nesting
"""
@click.group()
def cli():
    pass

@click.command()
def stuff():
    click.echo("hi")

@click.command()
def other_stuff():
    click.echo("bye")

cli.add_command(stuff)
cli.add_command(other_stuff)
"""

# add parameters


@click.command()
@click.option("--count", default=1, help="number of greetings")
@click.argument('name')
def hallihallo(count, name):
    try:
        for x in range(count):
            click.echo(f"hi, how's it going {name}")
    except:
        click.echo("forgot a name")


hallihallo()

cli.add_command(hallihallo)

cli()
