Baikal_volume = 23620
Days_year = 365
L_KM3 = 0.00000000001
KM3_M3 = 1000000000
RUB_BLN = 1000000000

# 1. На сколько лет хватит запасов воды Байкала для личного потребления?

# Среднее потребление воды в мире для личного использования - 40 л/день на человека
# Среднее потребление воды в России для личного пользования - 129 л/день на человека
water_consumption_l = float(input())

# Население земли - 7700000000 человек
# Население России - 146780720 человек
population = float(input())

water_cons_km3_day = water_consumption_l * L_KM3
cons_total = water_cons_km3_day * population
cons_years = Baikal_volume / cons_total / Days_year

print('Воды Байкала хватит на', format(cons_years // 1, '.0f'), 'лет.')


# 2. Выручка Правительства России при продаже запасов воды Байкала населению России для личного пользования.

# Тарифы Москвы: 38,7 за питьевую воду и 27,47 за водоотведение
tarif = input()
tarif1 = tarif.split(' ')
sum_tarif = float(tarif1[0]) + float(tarif1[1])

Baikal_volume_m3 = Baikal_volume * KM3_M3

revenue = Baikal_volume_m3 * sum_tarif

print('Выручка Правильства России', format(revenue / RUB_BLN, '.0f'), 'млрд руб')

if population == 146780720:
    print('Выручка правительства России за год', format(revenue / cons_years / RUB_BLN, '.0f'), 'млрд руб.')
else:
    print()

