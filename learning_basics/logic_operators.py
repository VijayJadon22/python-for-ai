age=25
has_license=True
drunk=False

can_drive = age>=16 and has_license
print(can_drive)

can_drive = age>=16 or has_license #true

print(not True)
print(not False)

can_drive=age>=18 and has_license and not drunk


score=5
score+=2
print(score)