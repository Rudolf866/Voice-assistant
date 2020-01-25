import speech_recognition as sr
import os
import sys
import webbrowser

# Функция, позволяющая проговаривать слова
# Принимает параметр "Слова" и прогроваривает их
def talk(words):
	print(words,' ') # Дополнительно выводим на экран
	os.system(words) # Проговариваем слова

# Вызов функции и передача строки
# именно эта строка будет проговорена компьютером
talk("Привет, чем я могу помочь вам?")

""" 
	Функция command() служит для отслеживания микрофона.
	Вызывая функцию мы будет слушать что скажет пользователь,
	при этом для прослушивания будет использован микрофон.
	Получение данные будут сконвертированы в строку и далее
	будет происходить их проверка.
"""



import speech_recognition as sr
r = sr.Recognizer()

#with sr.Microphone(device_index=12) as source:
   #r.adjust_for_ambient_noise(source)
   #print("Скажи что- нибудь")
  # audio = r.listen(source)

#query = r.recognize_google(audio,language="ru-Ru").lower()
#print("Вы сказали:"+ query)
#import speech_recognition as sr
#for index, name in enumerate(sr.Microphone.list_microphone_names()):
    #print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


def command():
	# Создаем объект на основе библиотеки
	# speech_recognition и вызываем метод для определения данных
	r = sr.Recognizer()

	# Начинаем прослушивать микрофон и записываем данные в source
	with sr.Microphone() as source:        
		# Просто вывод, чтобы мы знали когда говорить        
		print("Говорите")
		# Устанавливаем паузу, чтобы прослушивание
		# началось лишь по прошествию 1 секунды
		r.pause_threshold = 1
		# используем adjust_for_ambient_noise для удаления
		# посторонних шумов из аудио дорожки
		r.adjust_for_ambient_noise(source, duration=1)
		# Полученные данные записываем в переменную audio
		# пока мы получили лишь mp3 звук
		audio = r.listen(source)

	try: # Обрабатываем все при помощи исключений
		""" 
		Распознаем данные из mp3 дорожки.
		Указываем что отслеживаемый язык русский.
		Благодаря lower() приводим все в нижний регистр.
		Теперь мы получили данные в формате строки,
		которые спокойно можем проверить в условиях
		"""
		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		# Просто отображаем текст что сказал пользователь
		print("Вы сказали: " + zadanie)
	# Если не смогли распознать текст, то будет вызвана эта ошибка
	except sr.UnknownValueError:
		# Здесь просто проговариваем слова "Я вас не поняла"
		# и вызываем снова функцию command() для
		# получения текста от пользователя
		talk("Я вас не поняла")
		zadanie = command()

	# В конце функции возвращаем текст задания
	# или же повторный вызов функции
	return zadanie

# Данная функция служит для проверки текста,
# что сказал пользователь (zadanie - текст от пользователя)
def makeSomething(zadanie):
	# Попросту проверяем текст на соответствие
	# Если в тексте что сказал пользователь есть слова
	# "открыть сайт", то выполняем команду
  
	if 'открыть контакт' in zadanie:
		# Проговариваем текст
		talk("Уже открываю")
		# Указываем сайт для открытия
		url = 'https://vk.com/id93036714'
		# Открываем сайт
		webbrowser.open(url)
	# если было сказано "стоп", то останавливаем прогу
	elif 'стоп' in zadanie:
		# Проговариваем текст
		talk("Да, конечно, без проблем")
		# Выходим из программы   
		sys.exit(0)
	# Аналогично
	elif 'имя' in zadanie:
		talk("Меня зовут Сири")
# Вызов функции для проверки текста будет
# осуществляться постоянно, поэтому здесь
# прописан бесконечный цикл while
while True:
	makeSomething(command())
