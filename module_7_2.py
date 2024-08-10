def custom_write(f_name,strings):
    file=open(f_name,'w',encoding='utf-8',)
    ret_dict=dict()
    num=1
    for x in strings:
        ret_dict[(num,file.tell())]=x
        num+=1
        file.write(x+'\n')
    return ret_dict

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
