INDENTS = 4


def print_hanging_indents(poem):
    poemlist = poem.split('\n')
    cleanedpoem = [line.strip() for line in poemlist]
    indent = True
    for line in cleanedpoem:
        if line == '':
            indent = False
        elif indent:
            print ('    ' + line)
        else:
            indent = True
            print(line)
