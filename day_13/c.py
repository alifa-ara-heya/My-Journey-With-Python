sh = input("Enter hours again please: ")
sr = input("Enter rate again please: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input.")
    quit()

print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:", xp)