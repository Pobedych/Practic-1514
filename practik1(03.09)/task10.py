dictionary = {'apple': 'яблоко', 'book': 'книга', 'cat': 'кошка', 'school': 'школа'}

translate = lambda w: dictionary.get(w) or {v:k for k,v in dictionary.items()}.get(w) or "Не найдено"

print(translate('apple'))  
print(translate('книга'))  