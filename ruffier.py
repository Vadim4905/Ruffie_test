def ruffier_index(P1, P2, P3):
    return (4 * (P1 + P2 + P3) - 200) / 10

def neud_level(age):
    norm_age = (min(age, 15) - 7) // 2  # кожні 2 роки різниці від 7 років перетворюються на одиницю - аж до 15 років
    result = 21 - norm_age * 1.5 # множимо кожні 2 роки різниці на 1.5, так розподілені рівні у таблиці
    return result 

def ruffier_result(r_index, level):
    if r_index >= level:
        return 0
    level = level - 4 
    if r_index >= level:
        return 1
    level = level - 5     
    if r_index >= level:
        return 2
    level = level - 5.5 
    if r_index >= level:
        return 3
    return 4 

def main(P1, P2, P3, age):
    txt_res = []
    txt_res.append('''Низька. Терміново зверніться до лікаря!''')
    txt_res.append('''Задовільна. Зверніться до лікаря!''')
    txt_res.append('''Середня. Можливо, варто додатково обстежитись у лікаря.''')
    txt_res.append('''Вище середнього ''')
    txt_res.append('''Висока ''')

    r_index = ruffier_index(P1,P2,P3)
    level = neud_level(age)
    conclusion = txt_res[ruffier_result(r_index,level)]
    return r_index,conclusion