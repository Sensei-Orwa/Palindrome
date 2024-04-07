#palindrome checker

def is_palindrome(text):
  length = len(text)

  for i in range(0, length // 2):
    if (text[i] != text[length -i -1]):
      return False

  return True

string1 = "mum"
string2 ="qwerty"

print(is_palindrome(string1))
print(is_palindrome(string2))