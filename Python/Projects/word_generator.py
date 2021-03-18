import random
import requests

def word_generator():
    link_input = str(input('Enter the text file URL: '))
    content = requests.get(link_input).text
    splitted_file = content.split('\n')
    amount_of_words = int(input('Enter how many words you want to diplay: '))
    random_words = random.sample(splitted_file, (amount_of_words))
    print(random_words)
    
word_generator()