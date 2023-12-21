print("I can calculate your salary tax in Kazakhstan!")

salary = int(input("your salary number: "))

opv = (salary * 10) / 100
vosms = (salary * 2) / 100

mrp14 = 14 * 3450

ipn = ((salary - opv - mrp14 - vosms) * 10) / 100

so = ((salary - opv) * 3.5) / 100
sn = ((salary - opv - vosms) * 9.5) / 100
osms = (salary * 3) / 100

on_hands = salary - opv - vosms - ipn
print(f"{on_hands=}")

def info_calc():
    print("-----Идет вычисление...")
    print(f"ОПВ: {salary=} * 10% = {opv}")
    print(f"ВОСМС: {salary=} * 2% = {vosms}")
    print(f"ИПН: ({salary=} - ОПВ={opv} - 14МРП(14 * 3450)={mrp14} - ВОСМС={vosms}) * 10% = {ipn}")
    print("-----")
    print(f"CO (соц. очисление): ({salary=} - ОПВ={opv}) * 3.5% = {so}")  
    print(f"СН (соц. налог): ({salary=} - ОПВ={opv} - ВОСМС={vosms}) * 3.5% - СО={so} = {sn}")
    print(f"ОСМС: {salary=} * 3% = {osms}")
    print("-----")
    print(f"На руки: {salary=} - ОПВ={opv} - ВОСМС{vosms} - ИПН{ipn} = {on_hands}")
    print(f"На руки: {on_hands} тенге")

info_calc();
