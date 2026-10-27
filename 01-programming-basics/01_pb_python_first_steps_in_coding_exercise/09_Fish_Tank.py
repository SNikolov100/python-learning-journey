length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input()) / 100

volume_dm2 = (length_cm * width_cm * height_cm) / 1000
volume_dm2 -= volume_dm2 * percent

print(volume_dm2)