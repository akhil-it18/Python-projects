import random
words=['stuart broad','james anderson','zaheer khan','anil kumble','graeme smith','chris gayle','shawn pollock','jacques kallis','monty panesar','jonty rhodes','umesh yadav','michael clarke','daniel vettori','tom latham']
word=random.choice(words).split()
gword=' '.join(['_' for i in range(len(word[0]))])+"   "+' '.join(['_' for i in range(len(word[1]))])
word=' '.join(word)
print(gword)
guesses=5
aul=[]
while(guesses>0):
	uguess=input("What's your guess?")
	if(len(uguess)>1):
		print("Invalid guess")
		print(gword)
	
	elif uguess in word:
		lst=[j for j, ch in enumerate(word) if ch==uguess]
		for i in lst:
			gword=list(gword)
			gword[2*i]=uguess
			gword=''.join(gword)
		if '_' not in gword:
			print(gword)
			print("Congrats genius! You guessed the word")
			break
		print("Woah! Nice guess. Keep going")
		print(gword)
		print("Already used letter not in name: "+str(aul))
	
	elif uguess not in word:
		aul.append(uguess)
		guesses=guesses-1
		if(guesses==0):
			print("Sorry! You lost")
			print("The cricketer is "+word)
			break
		print("Wrong guess. You have %d chances left" %guesses)
		print(gword)
		print("Already used letter not in name: "+str(aul))
