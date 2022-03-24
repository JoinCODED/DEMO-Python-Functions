def brush_teeth():
    print("- Pickup the toothbrush")
    print("- Open the toothpaste")
    print("- Put some toothpaste on the toothbrush")
    print("- Brush your teeth by rubbing the toothbrush on your teeth")


def make_bed_prayer():
    print("بسمك اللهم أموت وأحيا")


def go_to_bed():
    brush_teeth()
    make_bed_prayer()


go_to_bed()


# bmi = (weight / height) ^ 2
# bmi status( < 19 thin, 19 < bmi < 25 Good, >= 25 you're overweight)

def get_bmi(weight, height):
    return weight / (height * height)


def get_bmi_status(bmi):
    if (bmi < 20):
        return "Underweighted"
    elif (bmi < 25):
        return "normal"
    else:
        return "overweight"


aBmi = get_bmi(80, 1.8)
bBmi = get_bmi(40, 1.8)
cBmi = get_bmi(120, 1.8)

aStatus = get_bmi_status(aBmi)
bStatus = get_bmi_status(bBmi)
cStatus = get_bmi_status(cBmi)

print("a", aBmi, aStatus)
print("b", bBmi, bStatus)
print("c", cBmi, cStatus)
