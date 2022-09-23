 ### Hangman Codification ###
import random ## Random importation

class HangMan(object):
    
    # Hangman game
    hang = []
    hang.append(' +---+') # comand to draw hang
    hang.append(' |   |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('=======')
    
    man = {}
    man[0] = [' 0   |'] # Comand to draw a man
    man[1] = [' 0   |', ' |   |']
    man[2] = [' 0   |', '/|   |']
    man[3] = [' 0   |', '/|\\  |']
    man[4] = [' 0   |', '/|\\  |', '/    |']
    man[5] = [' 0   |', '/|\\  |', '/ \\  |']
    
    pics = []
    
    words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote
crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama
mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram
rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger
toad trout turkey turtle weasel whale wolf wombat ze bra slot'''.split()  # Random Words

    infStr='_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\''
  
    def __init__(self, *args, **kwargs): # Values to draw a man and hang
        i, j = 2, 0
        self.pics.append(self.hang[:])
        for ls in self.man.values():
            pic, j = self.hang[:], 0
            for m in ls:
                pic[i + j] = m
                j += 1
            self.pics.append(pic)

    def pickWord(self): # Pick characters words. Each is divided into characters
        return self.words[random.randint(0, len(self.words) - 1)]
    
    def printPic(self, idx, wordLen):
        for line in self.pics[idx]: # Values to print Hangman
            print(line)
            
    def askAndEvaluate(self, word, result, missed):
        guess = input()
        if guess == None or len(guess) != 1 or (guess in result) or (guess in missed):# Ask character's values to evaluate if this is correct
            return None, False
        i = 0
        right = guess in word
        for c in word:
            if c == guess:
                result[i] = c
            i += 1
        return guess, right

    def info(self, info): # Information what is the word
        ln=len(self.infStr)
        print(self.infStr[:-3])
        print(info)
        print(self.infStr[3:])
            
    def start(self): # Main work of program
        print('Welcome to Hangman !')
        word = list(self.pickWord())# Pick a word from list
        result = list('*' * len(word))# Transform a word into a character
        print('The word is: ', result)# The word is evaluated
        success, i, missed = False, 0, []# right or wrong chracter
        while i < len(self.pics)-1:
            print('Guess the word: ', end='')
            guess,right = self.askAndEvaluate(word, result, missed)
            if guess == None:
                print('You\'ve already entered this character.')# Repeated character.
                continue
            print(''.join(result))
            if result == word:
                self.info('Congratulations ! You\'ve just saved a life !')#You won the game
                success = True
                break
            if not right:
                missed.append(guess)
                i+=1
            self.printPic(i, len(word))
            print('Missed characters: ', missed)
        
        if not success:
            self.info('The word was \''+''.join(word)+'\' ! You\'ve just killed a man, yo !') #You lost a game

a = HangMan().start()
