#!python3
# -*- coding: utf-8 -*- 
#canpIt.py - find out the cantonese pronouciation of marked words in text, and overwite the original text.

f1 = str(input('which text would you like to canIt?\n'))
ln = 0
sub = ' '
text_complished = ' '

with open(f1, mode='r+', encoding='utf-8') as raw_f:
    text = raw_f.read()
    textlist = text.split('*')
    
    for i in textlist:       
        m_char = i[-1]
        
        with open('ypdict.txt', encoding='utf-8') as ypdict:
            for l in ypdict:
                ln +=1
                if l.find(m_char) != -1:
                    sub = str('(') + l[4:].rstrip() + str(')')  
                else:
                    continue 
        n_i = i.replace(i, i + sub)
        raw_f.write('#')
        raw_f.write( n_i)

    raw_f.seek(0)
    n_text = raw_f.read()
    n_textlist = n_text.split('#')
    n_textlist.remove(n_textlist[0])
    text_complished = ''.join(n_textlist)

with open(f1, mode='w+', encoding='utf-8') as f2:
    f2.write(text_complished)
    print('Alright, there you go: '+ '\n')
    print(''.join(n_textlist))

       
    
