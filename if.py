try:
    hrs = float(input('enter hours: '))
    rate = float(input('enter rate: '))
except:
    print('Error!, please enter digits')
    quit()

if hrs >= 40:
    h = hrs - 40
    print((h*1.5*rate) + (hrs*rate))
else:
    print(hrs*rate)
