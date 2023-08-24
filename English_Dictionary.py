import json
from difflib import get_close_matches

class English_Dict:
    def __init__(self) -> None:
        self.word = ""
        with open("C:/Users/USER/Downloads/dictionary.json") as file:
            self.data = json.load(file)
        self.get_meaning()
    def unknown_word(self):
        print("Invalid word")
        
    def get_meaning(self):
        try:
            self.word = input("Input the word: ")
            self.word = self.word.lower()
            if  not self.word.isalpha():
               self.unknown_word()
      
            elif self.word in self.data:
                meaning = self.data[self.word]
                print(meaning)
            else:
                self.get_match(self.word)
        except:
                print("Invalid input")
                
        
    def get_match(self, word):
        if len(get_close_matches(self.word, self.data.keys())) > 0:
            closest = get_close_matches(self.word, self.data)[0]
            
            try:
                choice = input("Did you mean {} instead? Y or N: ".format(closest))
                choice = choice.lower()
                if choice == "yes" or choice == "y" or choice == "ye":
                    meaning = self.data[closest]
                    print(meaning)
                else:
                    print("sorry {} not found.".format(self.word))
            except:
                print("Check your input again")
            
    
        
Dictionary = English_Dict()
Dictionary

    
