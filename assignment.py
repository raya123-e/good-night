year=2002
if (year%4==0 and year%100!=0) or(year %400==0):
    print( year," is a leap year")

else :print(" is not a leap year")

#A python prompt that checks whether a letter is a vowel or a consonant
vowel="aeiouAEIOU"
letter='l'
if letter in vowel:
    print("vowel")
else:
    print("consonant")