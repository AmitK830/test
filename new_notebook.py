print("This is the new text notebook for Github")


def subzero(x):
    if x < -10:
        print("Freezing Point")
    elif x >= -10:
        print("No idea")
    elif x > 0:
        print("Need to check th data")
    else:
        print("New to do lots of experiment")


def pressure(x):
    if x > 1000:
        print("Atmospheric pressure")

    elif x < 0:
        print("Vacuum Pressure")
        print("New Pressure detected")
    else:
        print("Use Barometer or other device to measure")


<<<<<<< HEAD
def volume(x):
    try:
        if x > 1000:
            print("More than 1 liter")
        else:
            print("Need some device to measure")
    except ValueError:
        print("Invalid value of the volume")
=======

def temperature(x):
    if x > 4000:
        print("Temp of Sun")

    elif 4000 >= x > 2000:
        print("Temp of Hydrogen Bomb")
    elif x < 0:
        print("Temp of South & North poles")
    else:
        print("Measurable Temp")

temperature(10000)
>>>>>>> new_dev
