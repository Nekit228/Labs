#from words import words
words={'word': 'мир',\
    'earth':'земля',\
    'you': 'ты',\
    'I':'я',\
    'We':'мы',\
    'probably':'вероятно',\
    'piece':'кусок',\
    'tired':'усталый',\
    'should':'должен',\
    'be able':'быть в состоянии',\
    'not enough':'не хватает',\
    'enough':'достаточно',\
    'should':'должен',\
    'represent':'представлять',\
    'sequence':'последовательность'}

def rus_to_eng():
    eng_words=dict([[v, k] for k,v in words.items()])
    find_word=input('Введите слово ')
    print(eng_words.get(find_word) or 'Искомое слово не найдено')

def eng_to_rus():
    key = input('Enter word ')
    print (words.get(key) or 'No such key')

if __name__ == '__main__':
    while True:
        print('\nВыберите перевод:\n'
              '1 : рус - англ\n' '2 : eng - rus\n'
              'new - новое слово\n' 'stop - завершить')
        start = input()
        
        if start == '2':
            eng_to_rus()
        elif start == '1':
            rus_to_eng()
        elif start == 'stop':
            print('Увидимся позже')
            break
        else:
            print('Повторите ввод!')
