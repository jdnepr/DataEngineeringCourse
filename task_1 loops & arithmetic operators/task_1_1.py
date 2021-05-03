duration = input('Input your duration:')
duration = int(duration)

if (duration < 60):
    print (duration, 'sec')
elif (duration < 3600):
    minutes = duration // 60
    seconds = duration % 60
    print(minutes, 'min,', seconds, 's')
elif (duration < 24*3600):
    hours = duration // 3600
    print("duration / 3600", duration / 3600)
    minutes = (duration % 3600)
    print("minutes_", minutes)
    seconds = minutes % 60
    print(hours, 'hours,', minutes, 'min,', seconds, 's')
