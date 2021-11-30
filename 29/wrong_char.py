def get_index_different_char(chars):
    alphanumeric = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    mydict = {}
    alpha = 0
    nonalpha = 0
    alphapos = []
    nonalphapos = []
    for mynum, mychar in enumerate(chars):
        if len(str(mychar)):
            if str(mychar) in alphanumeric:
                alphapos.append(mynum)
                alpha += 1
            else:
                nonalphapos.append(mynum)
                nonalpha += 1

    if alpha < nonalpha:
        return alphapos[0]
    else:
        return nonalphapos[0]

