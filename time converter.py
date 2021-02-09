#  V - conversion of time to seconds
 #Write an algorithm which receives the time of day in three different numbers, the hour,
# the minutes and the seconds and returns the number of seconds since midnight.
hour=int(input("type the hour "))
h=hour*3600
minutes=int(input("type the minutes "))
m=(minutes*60)
seconds=int(input("type the seconds "))
sec=h+m+seconds
print(sec)
