#!/usr/bin/python3
def multiple_returns(sentence):
    s_tuple = ()
    if len(sentence) < 0:
        s_tuple = (len(sentence), None)
        return (s_tuple)

    s_tuple = (len(sentence), sentence[0])
    return (s_tuple)


'''
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
'''
