def convert_temp(value):
    celsius = value - 273.15
    return round(celsius, 2)

def convert_speed(value):
    kmph = value * 3.6
    return round(kmph, 2)

# def convert_temp(value, target_unit):
#     unit = target_unit.upper()
#     if unit == 'C':
#         result = value - 273.15
#     elif unit == 'F':
#         result = value - 459.67
#     elif unit == 'K':
#         result = value
#     else:
#         return "Nieznana jednostka"
#     return round(result, 2)

