str1, str2, str3 = input(), input(), input()
condition1 = str1 == "рас" and str2 == "два" and str3 == "три"
condition2 = str1 == "1" and str2 == "2" and str3 == "3"
print("ГОРИ" if condition1 or condition2 else "НЕ ГОРИ")