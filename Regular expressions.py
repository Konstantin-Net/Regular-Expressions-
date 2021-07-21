from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)


def names_separation():  # Функция разделяет полное имя на шаблон Ф + И + О
    for i in contacts_list:
        p = f"{i[0]} {i[1]} {i[2]}".split(" ")
        n = 0
        for k in i[0: 3]:
            i.remove(k)
            i.insert(n, p[n])
            n += 1


def repeats_combining():  # Функция комбинирует одинаковые имена с данными в единую запись
    n = 0
    while n <= len(contacts_list) - 1:
        p = contacts_list[n]
        for i in contacts_list[n + 1:]:
            if p[0] == i[0] and p[1] == i[1]:
                x = 0
                while x <= 6:
                    if len(p[x]) < len(i[x]):
                        p[x] = i[x]
                    x += 1
                contacts_list.remove(i)
        n += 1


def editing_phones():  # Функция приводит телефонне номера к единому шаблону
    phone_pattern = re.compile(
        r"(\+7|8)[\s\(]*(\d+)[\)\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})([\s\(]*(доб\.)\s(\d+)\)*)*")
    for i in contacts_list[1:]:
        result = phone_pattern.sub(r"+7(\2)\3-\4-\5 \7\8", i[5])
        i[5] = result


if __name__ == '__main__':
    names_separation()
    repeats_combining()
    editing_phones()


with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
