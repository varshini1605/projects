import csv
import random

def get_random_Quote(file='list.csv'):
    try:#Load quotes from csv file
        with open(file) as csvfile:
            Quotes=[{'author': line[1],'quotes': line[0]} for line in csv.reader(csvfile, delimiter='|')]

    except Exception as e:#default get_random_Quote
        Quotes=[{"author":"abc", "quote":'anything'}]
    return random.choice(Quotes)

if __name__=='__main__':
    Quotes=get_random_Quote()
    print(f'quote is "{Quotes["quotes"]}" - {Quotes["author"]}')

