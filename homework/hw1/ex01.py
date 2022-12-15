# Íàïèøèòå ïğîãğàììó, êîòîğàÿ ïğèíèìàåò íà âõîä öèôğó, îáîçíà÷àşùóş äåíü íåäåëè, 
# è ïğîâåğÿåò, ÿâëÿåòñÿ ëè ıòîò äåíü âûõîäíûì
# Ïğèìåğ:
# - 6 -> äà
# - 7 -> äà
# - 1 -> íåò

day_number = int(input('Write day number: '))

if day_number > 0 and day_number < 8:
    if day_number == 6 or day_number == 7:
        print('Weekend!!! :)')
    else:
        print('Work!')
else:
    print('Wrong number!')
