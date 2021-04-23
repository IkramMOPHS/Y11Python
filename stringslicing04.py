#Ikram Munye 
#stringslicing04

rhyme = str(input("Enter the first line of a nursery rhyme: "))

print("This has," ,len(rhyme), "letters in it")

startnum = int(input("Enter a starting number: "))
endnum = int(input("Enter a ending number: "))

print(rhyme[startnum:endnum])
