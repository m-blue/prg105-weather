temp = {'Jan': 45, 'Fed': 45, 'Mar': 48, 'Apr': 52, 'May': 57, 'Jun': 61, 'Jul': 66, 'Aug': 66, 'Sep': 63, 'Oct': 55, 'Nov': 50, 'Dec': 45 }

# global variables
average_temperature = 54
high_temp = dict()


def ave_temp(weat):
    count = 0
    for t in weat:
        count += weat[t]
    ave = count / len(weat)
    print("The average temperature in London, Britain is: " + str(ave) + " Fahrenheit")


def over_ave(weat):
    for t in weat:
        if weat[t] > average_temperature:
            high_temp[t] = weat[t]
    print high_temp


ave_temp(temp)
over_ave(temp)
