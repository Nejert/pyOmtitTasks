str1, str2 = input().lower(), input().lower()
lst = ["да", "нет"]
print("ВЕРНО" if str1 in lst and str2 in lst else "НЕВЕРНО")
