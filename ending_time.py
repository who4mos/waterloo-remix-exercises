starting_time = input()
D = int(input())

h, m = int(starting_time[:2]), int(starting_time[3:])

if m + D < 60:
    print(f"{h:02}:{m+D:02}")
else:
    print(f"{(h+(m+D)//60)%24:02}:{(m+D)%60:02}")
