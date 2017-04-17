
'''
text1 = 'Science can change life of many people'
text2 = 'Science is a source of all pain'
text3 = 'Science has a mathematical basis'

targettext = 'I love Science'
'''
#aim is to match percentage of words in target text match with the text1,2 and 3.

def checker(text,targettext):
    print text
    print targettext
    text_count=len(text)
    target_count=len(targettext)
    print target_count
    match_count =0
    for target_word in targettext:
        if target_word in text:
            match_count=match_count+1

    print match_count
    percentage_plagiarised = (match_count/float(target_count))*100
    return percentage_plagiarised

def plagiarismchecker(text1,text2,text3,targettext):
    text1=text1.split(' ')
    text2=text2.split(' ')
    text3 = text3.split(' ')
    targettext=targettext.split(' ')
    percentage1 = checker(text1,targettext)
    percentage2 = checker(text2, targettext)
    percentage3 = checker(text3, targettext)

    print percentage1
    print percentage2
    print percentage3

    percentages={
        'percentage1':percentage1,
        'percentage2':percentage2,
        'percentage3':percentage3
    }

    return percentages
#plagiarismchecker(text1,text2,text3,targettext)


