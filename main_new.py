import pandas as pd
import json 
import numpy as np 
import os
import string
import re


# добавляем к стандартным знакам пунктуации кавычки и многоточие
spec_chars = string.punctuation + '«»\t—…’'
bad_words = pd.read_csv('bad_words.csv', skipinitialspace=True, sep=',')
right_data = pd.DataFrame()


def cleaner(some_str: str):
    text = some_str.lower()
    # очищаем текст от знаков препинания
    text = "".join([ch for ch in text if ch not in spec_chars])
    # меняем переносы строк на пробелы
    text = re.sub('\n', ' ', text)
    # убираем из текста цифры
    text = "".join([ch for ch in text if ch not in string.digits])
    text = " ".join(text.split())
    # приведение слов к начальной форме 
    return text


def get_dialogues(data: json):
    dialogue = data['dialogue']
    all_messages = []  #все предложения, все сообщения
    for key in dialogue:
        if key['share_photo'] == True:  #иду пока не встречу фотку
            break 
        text = key['message']
        text = cleaner(text)  #очищу предложение от пунктуации и приведу к образцу 
        all_messages.append(text)
    all_messages = " ".join((all_messages))  #отсортирую предложения по длине и возьму первые пять
    return all_messages #верну список всех предложений


path = 'C:\\Visual Studio programs\\datas'
files = os.listdir(path)   
id_col, phrase_col, picture_col = [], [], []
for i in files:
    file = path + '\\' + i
    with open(file) as f:
        dial = json.load(f)
        for e in dial:
            phrases = get_dialogues(e)
            id_col.append(e['dialogue_id'])
            phrase_col.append(phrases)
            picture_col.append(e['photo_url'])


right_data['id'] = id_col
right_data['phrase'] = phrase_col
right_data['url_picture'] = picture_col
right_data.to_csv('rdata1.csv', index=False, sep=';')
