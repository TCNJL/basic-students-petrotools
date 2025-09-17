#En este módulo encontraras las reglas de mezclado
#Gases es una lista que contiene objetos tipo gas, con propiedades PresionCritica, TemperaturaCritica, FraccionMolar, componenentes
#Toma una lista de objetos y devuelve solo un objeto con propiedades PresionCritica, TemperaturaCritica
import math
def Kay(gases):
    #Para esta regla de mezclado usa Ppc, Tpc =Kay(gases)
    Tpc = sum(a * b for a, b in zip(gases.FraccionMolar, gases.TemperaturaCritica))
    Ppc = sum(a * b for a, b in zip(gases.FraccionMolar, gases.PresionCritica))
    return Ppc, Tpc

def Sutton(gases):
    #Reglas de mezclado de sutton
    suma_1 = sum(y * (Tci / Pci) for y, Tci, Pci in zip(gases.FraccionMolar, gases.TemperaturaCritica, gases.PresionCritica))
    suma_2 = sum(y * (Tci / Pci)**0.5 for y, Tci, Pci in zip(gases.FraccionMolar, gases.TemperaturaCritica, gases.PresionCritica))
    yc7=gases.FraccionMolar[-1]
    pc7=gases.PresionCritica[-1]
    tc7=gases.TemperaturaCritica[-1]
    J = (1/3) * suma_1 + (2/3) * suma_2**2
    K = sum(yi * (Tci / math.sqrt(pci)) for yi, Tci, pci in zip(gases.FraccionMolar, gases.TemperaturaCritica, gases.PresionCritica))
    Fj=(1/3)*yc7*tc7/pc7+(2/3)*(yc7*(tc7/pc7)**0.5)**2
    Ej=0.6081*Fj+1.1325*Fj**2-14.004*Fj*yc7+64.434*Fj*yc7**2
    Ek=tc7/(pc7**0.5)*(0.3129*yc7-4.8156*yc7**2+27.3751*yc7**3)
    Jp=J-Ej
    Kp=K-Ek
    Tpc=Kp**2/Jp
    Ppc=Tpc/Jp
    return Ppc, Tpc

