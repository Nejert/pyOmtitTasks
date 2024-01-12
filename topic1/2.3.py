iterator = iter([input() for _ in range(4)])
print(f"""Индивидуальный гороскоп для пользователя {next(iterator)} {next(iterator)}
Кем вы были в прошлой жизни: {next(iterator)}
Ваш знак зодиака - {next(iterator)} , поэтому вы - тонко чувствующая натура.""")