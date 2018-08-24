import math

def freqToRGB(frequency):
    Wavelength = 299792458e9 / frequency
    Gamma = 0.8
    IntensityMax = 255

    if ((Wavelength >= 380) and (Wavelength<440)):
        Red = -(Wavelength - 440) / (440 - 380)
        Green = 0.0
        Blue = 1.0
    elif ((Wavelength >= 440) and (Wavelength<490)):
        Red = 0.0
        Green = (Wavelength - 440) / (490 - 440)
        Blue = 1.0
    elif ((Wavelength >= 490) and (Wavelength<510)):
        Red = 0.0
        Green = 1.0
        Blue = -(Wavelength - 510) / (510 - 490)
    elif ((Wavelength >= 510) and (Wavelength<580)):
        Red = (Wavelength - 510) / (580 - 510)
        Green = 1.0
        Blue = 0.0
    elif ((Wavelength >= 580) and (Wavelength<645)):
        Red = 1.0
        Green = -(Wavelength - 645) / (645 - 580)
        Blue = 0.0
    elif ((Wavelength >= 645) and (Wavelength<781)):
        Red = 1.0
        Green = 0.0
        Blue = 0.0
    else:
        Red = 0.0
        Green = 0.0
        Blue = 0.0

    if ((Wavelength >= 380) and (Wavelength<420)):
        factor = 0.3 + 0.7*(Wavelength - 380) / (420 - 380)
    elif((Wavelength >= 420) and (Wavelength<701)):
        factor = 1.0
    elif((Wavelength >= 701) and (Wavelength<781)):
        factor = 0.3 + 0.7*(780 - Wavelength) / (780 - 700)
    else:
        factor = 0.0

    if Red == 0.0:
        Red1 = 0
    else:
        Red1 = round(IntensityMax * math.pow(Red * factor, Gamma))

    if Green == 0.0:
        Green1 = 0
    else:
        Green1 = round(IntensityMax * math.pow(Green * factor, Gamma))

    if Blue == 0.0:
        Blue1 = 0
    else:
        Blue1 = round(IntensityMax * math.pow(Blue * factor, Gamma))

    return (Red1, Green1, Blue1)

print(freqToRGB(4.7e14))
