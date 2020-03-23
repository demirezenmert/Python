

def counterFrequency (text,subText) :
    counter = 0 
    len_sub = len(subText)

    for i in range(len(text)):
        if text[i: i+len_sub] == subText : counter += 1

    return counter




text = "ABCCDCDBCBABC"
sub_text = "CD"
print(counterFrequency(text,sub_text))


