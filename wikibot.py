import wikipedia

usr_inp = input ("Please enter a name that you would like a wikipedia entry about: ")

def scrape(name=usr_inp, lenght=1):
    res = wikipedia.summary(name, sentences=lenght)
    return res
    
print (scrape())