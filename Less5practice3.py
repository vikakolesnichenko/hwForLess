#Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк.
# Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!
f = open('Pr5.txt', 'r')
fo = f.readlines()
l = []
for i in fo:
    l.append(i.split())
def kill_list(input_list):
    output_list = []
    for element in input_list:
        if type(element) == list:
            output_list.extend(kill_list(element))
        else: output_list.append(element)
    return output_list
k = (kill_list(l))

def count_in_text(list_word):
    M = {}
    for i in list_word:
        M[i] = M.setdefault(i, 0) +1 #не знаю как тут применить map :(
    return M
f.close()
print(count_in_text(k))