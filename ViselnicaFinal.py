# -*- coding: utf8 -*-
import random

#Функция приветсвия 
def wellcome():
	print('Добро пожаловать в игру Висельница. Для начала нажмите Enter.....')
	input()

#Функция инструкции
def instruction():
	print('Правила игры следующие:\n1) Система сгенерирует случайное слово\n2) Ваша задача ввести букву\n3) Елси буквы нет в слове, то начнется строится висельница. У вас 11 попыток на ошибку.')
	input()

#Генерация рисунка
def generation(list1, list2, list3, list4, list5, list6, list7, list8, list9, list10):
	print('\n')
	print(*list1)
	print(*list2)
	print(*list3)
	print(*list4)
	print(*list5)
	print(*list6)
	print(*list7)
	print(*list8)
	print(*list9)
	print(*list10)
	print('\n')


#Функция возврата писков при первой ошибке
def first_mistake(listtochange10):
    listtochange10[0] = '_'
    listtochange10[1] = '_'
    listtochange10[2] = '_'
    listtochange10[3] = '_'
    listtochange10[4] = '_'
    listtochange10[5] = '_'
    listtochange10[6] = '_'
    return listtochange10

#Функция возврата списков при второй ошибке
def second_mistake(listtochange1, listtochange2, listtochange3, listtochange4, listtochange5, 
    listtochange6, listtochange7, listtochange8, listtochange9, listtochange10):
    listtochange1[0] = '+'
    listtochange2[0] = '|'
    listtochange3[0] = '|'
    listtochange4[0] = '|'
    listtochange5[0] = '|'
    listtochange6[0] = '|'
    listtochange7[0] = '|'
    listtochange8[0] = '|'
    listtochange9[0] = '|'
    listtochange10[0] = '|'
    return listtochange1, listtochange2, listtochange3, listtochange4, 
    listtochange5, listtochange6, listtochange7, listtochange8, listtochange9, listtochange10

#Функция возврата списков при третей ошибке
def third_mistake(listtochange7, listtochange8, listtochange9, listtochange10):
    listtochange7[1] = '—'
    listtochange7[2] = '—'
    listtochange7[3] = '+'
    listtochange8[3] = '|'
    listtochange9[3] = '|'
    listtochange10[3] = '|'
    return listtochange7, listtochange8, listtochange9, listtochange10

#Функция возврата списков при четвертой ошибке
def fourth_mistake(listtochange1):
    listtochange1[1] = '—'
    listtochange1[2] = '—'  
    listtochange1[3] = '—'  
    listtochange1[4] = '—'  
    listtochange1[5] = '—'  
    listtochange1[6] = '—' 
    listtochange1[7] = '+' 
    return listtochange1

#Функция возврата списков при пятой ошибке
def fifth_mistake(listtochange2, listtochange3):
    listtochange2[7] = '|'
    listtochange3[7] = '|'
    return listtochange2, listtochange3

#Функция возврата списков при шестой ошибке
def sixsth_mistake(listtochange4):
    listtochange4[7] = 'O'
    return listtochange4

#Функция возврата списков при седьмой ошибке
def seventh_mistake(listtochange5, listtochange6, listtochange7):
    listtochange5[7] = '|'
    listtochange6[7] = '|'
    listtochange7[7] = '|'
    return listtochange5, listtochange6

#Функция возврата списков при восьмой ошибке
def eight_mistake(listtochange8, listtochange9):
    listtochange8[6] = '|'
    listtochange9[6] = '|'
    return listtochange8, listtochange9

#Функция возврата списков при девятой ошибке
def nine_mistake(listtochange8, listtochange9):
    listtochange8[8] = '|'
    listtochange9[8] = '|'
    return listtochange8, listtochange9

#Функция возврата списков при десятой ошибке
def ten_mistake(listtochange5):
    listtochange5[6] = '—'
    listtochange5[5] = '—'
    return listtochange5

#Функция возврата списков при одинадцатой ошибке
def eleven_mistake(listtochange5):
    listtochange5[8] = '—'
    listtochange5[9] = '—'
    return listtochange5

#Основная функция
def main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word):
	random_word_list = list(random_word)
	error = '\n                                                    Ошибка!\n'
	print('\n-----------------------------------------')
	print('Загаданное слово:\n')
	print(*guess_list)
	print('-----------------------------------------\n')
	print('\nПоле:\n')
	generation(list1, list2, list3, list4, list5, list6, list7, list8, list9, list10)
	print('\n-----------------------------------------')
	print('Использованные буквы:\n')
	print(used_bukv)
	print('-----------------------------------------\n')
	player_answer = input("Введите букву: ")
	player_answer.lower()
	if counter<=11:
		if len(player_answer) != 1:
			print(error)
			print('-----Введите одну букву!-----\n')
			main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word)
		elif not player_answer in rus_list:
			print(error)
			print('-----Введите русские буквы!-----\n')
			main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word)
		elif player_answer in used_bukv:
			print('\nБуква была использована!\n')
			main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word)
#-------если неверная буква-----------------
		elif len(player_answer) == 1 and player_answer in rus_list and not player_answer in random_word_list:
			if counter == 1:
				used_bukv.append(player_answer)
				print(error)
				first_mistake(list10)
				counter+=1
				main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word)
			elif counter == 2:
				used_bukv.append(player_answer)
				print(error)
				second_mistake(list1, list2, list3, list4, list5, list6, list7, list8, list9, list10)
				counter+=1
				main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word)
			elif counter == 3:
				used_bukv.append(player_answer)
				print(error)
				third_mistake(list7, list8, list9, list10)
				counter+=1
				main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word)
			elif counter == 4:
				used_bukv.append(player_answer)
				print(error)
				fourth_mistake(list1)
				counter+=1
				main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word)
			elif counter == 5:
				used_bukv.append(player_answer)
				print(error)
				fifth_mistake(list2, list3)
				counter+=1
				main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word)
			elif counter == 6:
				used_bukv.append(player_answer)
				print(error)
				sixsth_mistake(list4)
				counter+=1
				main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word)
			elif counter == 7:
				used_bukv.append(player_answer)
				print(error)
				seventh_mistake(list5, list6, list7)
				counter+=1
				main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word)
			elif counter == 8:
				used_bukv.append(player_answer)
				print(error)
				eight_mistake(list8, list9)
				counter+=1
				main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word)
			elif counter == 9:
				used_bukv.append(player_answer)
				print(error)
				nine_mistake(list8, list9)
				counter+=1
				main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word)
			elif counter == 10:
				used_bukv.append(player_answer)
				print(error)
				ten_mistake(list5)
				counter+=1
				main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word)
			elif counter == 11:
				used_bukv.append(player_answer)
				print(error)
				eleven_mistake(list5)
				print('Неотгаданное слово:\n')
				print(random_word)
				print('\nПоле:\n')
				generation(list1, list2, list3, list4, list5, list6, list7, list8, list9, list10)
				print ('\n'+'#'*20+'Конец игры!'+'#'*20+'\n')
				input("\nНажмите Enter для новой игры.......\n\n\n")
				start()
#-------если верная буква-------------------------------
		elif len(player_answer) == 1 and player_answer in rus_list and player_answer in random_word_list:
			print("\n                                                    Верно!\n")
			used_bukv.append(player_answer)
			while player_answer in random_word_list:
				x=random_word_list.index(str(player_answer))
				guess_list[x] = player_answer
				random_word_list[x] = "``"
			if not '_' in guess_list:
				print('\n'+'#'*20+'Победа'+'#'*20+'\n')
				print(*guess_list)
				print('\nПоле:\n')
				generation(list1, list2, list3, list4, list5, list6, list7, list8, list9, list10)
				input("\nНажмите Enter для новой игры.......\n\n\n")
				start()
			main(counter, guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,random_word)

#Функция запуска
def start():
	#Начало кода
	used_bukv = []
	#список слов
	Words = "округ господин зло лодка магазин ряд частность этаж редакция совет механизм обеспечение милиция план птица соответствие размер запах безопасность расстояние дверь оборона игра лидер ресторан место расход деревня течение шум стакан крыло рыба водка враг мешок следователь фигура трава ремонт размер запись опасность картина половина оборона рассмотрение предприятие толпа владелец журнал частность концепция звук указание сторона обращение церковь остров отец порядок плата уровень процент последствие раз категория работа стиль ученый основное небо ручка колено страна техника молодежь ночь шум враг значение руководство металл судьба учреждение редакция удивление лагерь повышение ухо судья неделя влияние частность бок основное сезон спор сущность"
	Words_list = Words.split()
	#Функция генерации случайного слова
	random_word = Words_list[random.randint(0,len(Words_list))]
	random_word_list = list(random_word)
	#создание пустого поля
	guess_list = ["_"]*len(random_word)
	#Строка с русскими буквами
	rus_list ='абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
	#пустые списки
	list1 = [' ']*10
	list2 = [' ']*10
	list3 = [' ']*10
	list4 = [' ']*10
	list5 = [' ']*10
	list6 = [' ']*10
	list7 = [' ']*10
	list8 = [' ']*10
	list9 = [' ']*10
	list10 = [' ']*10
	wellcome()
	instruction()
	main(1,guess_list, used_bukv, rus_list, list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, random_word)

#Запуск программы
start()