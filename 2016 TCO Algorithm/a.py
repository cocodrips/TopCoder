def getTime(time):
    hh, mm = map(int, time.split(':'))

    h = 0
    # if mm != 0:
    h = mm / 5

    m = hh * 5
    # if m == 60:
    #     m = 0

    return "{0}:{1}".format(str(h).zfill(2), str(m).zfill(2))

# print getTime("12:00")

HH = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
MM = ["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]
for H in HH:
    for M in MM:
        print "{0}:{1} -> {2}".format(H, M, getTime("{0}:{1}".format(H, M)))