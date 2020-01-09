import random
import urllib.request

word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
wordList = long_txt.splitlines()

def DrawHangman(i):
    if(i==1):
        return("        O        ")
    if(i==2):
        return("        O\n\t|        ")
    if(i==3):
        return("      \ O \n\t|          ")
    if(i==4):
        return("      \ O /\n\t|          ")
    if(i==5):
        return("      \ O /\n\t|\n       /     ")
    if(i==6):
        return("      \ O /\n\t|\n       / \   ")
    if(i==7):
        return("      \ O |/\n\t|\n       / \   ")
    if(i==8):
        return("      \ O_|/\n\t|\n       / \   " +"\n"+ "Last breaths counting, Take care!")
    if(i==9):
        return("        O_|\n       /|\ \n       / \   "+ "\n"+ "you killed the poor man :(" )
        
        
    

print("Enter your name:" )
name= input()
print(f"welcome {name}")
print("  --------------  ")
print("try to guess the word in less than 10 attemps")

word = random.choice(wordList)
guessword = ''
j=1
turn=10
while(turn>=1):
    MainWord = ''
    missed = 0
    for letter in word:
       if letter in guessword:
         MainWord = MainWord + letter
       else:
         MainWord = MainWord + "_" + " "
    if MainWord == word:
            print(MainWord)
            print("You win!")
            break
    
    print("guess a letter from the word:", MainWord)
    char = input()
    if(char in word and char not in MainWord):
       guessword = guessword + char
    else:
       turn-=1
       print(f"you have {turn} turns left")
       print("    ------    ")
       print(DrawHangman(j))
       j+=1
     
    