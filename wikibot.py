import wikipedia
import click


@click.command()
#@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Wikipedia page to scrape',
              help='Webpage that we will scrape.')

def scrape(name="Microsoft", lenght=1):
    res = wikipedia.summary(name, sentences=lenght)
    click.echo(f" {res}!")
    
print (scrape())

if __name__ == '__main__':
    scrape()

#usr_inp = input ("Please enter a name that you would like a wikipedia entry about: ")



