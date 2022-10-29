# print('kabisa yilni topadigan dastur')

# a = int(input('istalgan yilni kiriting>>>'))
# if (a % 4 == 0 != a % 100 != 0) or a % 400 == 0:
#     print('kabisa yil')
# else:
#     print('kabisa yil emas')    


# kun = input('bugun qanaqa kun>>>')
# harorat = float(input('issiq necci gradus?'))
# if kun.lower() == 'yakshanba' and harorat>=35:
#     print('basenga go')
# elif kun.lower() == 'yakshanba' and harorat<35:
#     print('eeee nma qilasan borib soviqti qara')    


coy = input('''Siz coy olgan bulsangiz '1' deb yozing >>> ''')
price = 15000
non = input('''Siz non olmagan bulsangiz '0' deb yozing >>> ''')
if coy and non:
    price = price + 10000
elif coy or non:
    price = price + 5000    
print(f"sizning jami summangiz, {price}")



























