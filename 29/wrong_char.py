def get_index_different_char(chars):
    alphanumeric = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    
    alphapos = []
    nonalphapos = []
    for mynum, mychar in enumerate(chars):
        if str(mychar) in alphanumeric:
            alphapos.append(mynum)
        else:
            nonalphapos.append(mynum)

    if len(alphapos) == 1:
        return alphapos[0]
    else:
        return nonalphapos[0]