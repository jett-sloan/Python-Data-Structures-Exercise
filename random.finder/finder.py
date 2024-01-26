import random
class WordFinder:
    def __init__(self,path):
        self.path = path
        self.word_list = self.get_words_from_file()
        
    def get_words_from_file(self):
        word_file = open(self.path, 'r')
        word_string = word_file.read()
        return word_string.split('\n')
    
    def get_random_word(self):
        return random.choice(self.word_list)
    


new_var = WordFinder('/home/jettsloan/word.txt')
random_word = new_var.get_random_word()


