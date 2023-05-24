def uppercase(string):
    return string.upper()


def lowercase(string):
    return string.lower()

def reverse(string):
    return string[::-1]

def changeletters(string):
    if 'a'  in string:
      return(string.replace('a', 'A'))
    else:
        return "Não existe essa letra na palavra fornecida"

def starts_with(string, prefix):
    return string.startswith(prefix)


