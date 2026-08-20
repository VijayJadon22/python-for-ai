age=25
has_license=False

can_drive = age>=16 and has_license
print(can_drive)

can_drive = age>=16 or has_license #true