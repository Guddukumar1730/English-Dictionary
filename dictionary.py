#colonel,draught,onomatopoeia
print("THE GUDDU DICTIONARY")
d1={'colonel':'a rank of officer in the army and in the US air force\n,above a lieutenant colonel and below a brigadier or '
              'brigadier general.\n example- Colonel Murphy was the evening\'s guest','draught':'current of air. example-the draught made robyn shiver',
                 'onomatopoeia':'the formation of a word from  a sound associated with what is named. '
                   'example- a relatively large number of bird names arise by onomatopoeia','python':'python is a \n '
                'computer programming language often used to build websites\n and software,automate tasks, and conduct data analysis.','shreyansh':'part of the best blessing'}

print("ENTER YOUR WORD")
d2=d1
d2=input()
print("the meaning of ", d2 , end=" is ")
print(d1.get(d2))