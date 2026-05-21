#calcular condicional de pagamento de salário 
hrs = input("Enter hours:  ")
rt = input("Enter rate:  ")
xh = float(hrs)
xr = float(rt)
if xh < 40 :
    xp = xh * xr
else : 
    xp = 40 * xr +((xh - 40) * xr * 1.5)
print("Pay: ", xp)
