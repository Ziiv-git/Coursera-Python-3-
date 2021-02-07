def compute_pay(hrs,rate):
    if hrs >= 40:
        h = hrs - 40
        result = ((h*1.5*rate) + (40*rate))
    else:
        result = (hrs*rate)

    return result

try:
    hrs = float(input('enter hours: '))
    rate = float(input('enter rate: '))
except:
    print('Error!, please enter digits')
    quit()

cp = compute_pay(hrs,rate)
print('Pay:', cp)
