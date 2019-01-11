#Arrays and Strings

# Is Unique - Implement an algorithm to determine if a string has all unique characters

def isUnique(string):
    if len(string) == len(set(string)):
        return True
    else:
        return False


def check_unique(input):
  input_seen = []
  for i in input:
    if i in input_seen:
      return False
    input_seen.append(i)
  return True

print(isUnique('Supriya'))
print(isUnique('aaddffggh'))


print(check_unique('Supriya'))
print(check_unique('aaddffggh'))


#Check Permutation - Given two strings, write a method to decide if one is a permutation of the other

def isPermutation(input1,input2):
    input1 = input1.upper()
    input2 = input2.upper()
    if (len(input1)==len(input2)) and (sorted(input1)==sorted(input2)):
        return True
    else:
        return False

def isPerm(input1,input2):
    input1 = input1.upper()
    input2 = input2.upper()
    
    if (len(input1)!= len(input2)):
        return False

    d = dict()

    for i in input1:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1

    for i in input2:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    return all(value == 0 for value in d.values())
    

print(isPermutation('Supriya','Priyasu'))

print(isPerm('Supriya','Priyasu'))
    


