#text = input('Введите текст на одной строке\n')
#if 'хорош' in text and 'плох' not in text:
#    print('Текст имеет положительную эмоциональную окраску.')
#elif 'плох' in text and 'хорош' not in text:
#    print('Текст имеет отрицательную эмоциональную окраску.')
#else:
#    print('Текст имеет нейтральную или смешанную эмоциональную окраску.')

str1, str2, str3 = input(), input(), input()
condition1 = (str1 == "рас" or str1 == "один") and str2 == "два" and str3 == "три"
condition2 = str1 == "1" and str2 == "2" and str3 == "3"
print("ГОРИ" if condition1 or condition2 else "НЕ ГОРИ")

#print(input())
