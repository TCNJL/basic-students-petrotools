#En este módulo encontrarás correlaciones para el cálculo del factor z y la compresibilidad de un gas
from math import exp
from scipy.optimize import newton

def Papay(presion_critica,temperatura_critica, presion, temperatura):
#Correlación de Papay, calcula el factor Z y la compresibilidad del gas
#llama a la correlación mediante z,cg=Papay(presion_critica,temperatura_critica, presion, temperatura)
    tr=temperatura/temperatura_critica
    pr=presion/presion_critica
    #Límites de la correlación
    if 1.2<=tr<=3 or 0.1<=pr<=15:
        z=1-3.52*pr/(10**(0.9813*tr))+0.274*pr**2/(10**(0.8157*tr))
        dz=-3.52/(10**(0.9813*tr))+0.544*pr/(10**(0.8157*tr))
        cg=(1/pr-1/z*dz)/presion_critica
        return z,cg
    else:
        print("La correlacion está fuera de rango")
        return None

def Hall_Yarborough(presion_critica,temperatura_critica, presion, temperatura):
#Correlación de Hall_Yarborough, calcula el factor Z y la compresibilidad del gas
#llama a la correlación mediante z,cg=Hall_Yarborough(presion_critica,temperatura_critica, presion, temperatura)
    pr=presion/presion_critica
    tr=temperatura/temperatura_critica
    t=1/tr
    #Límites de la coprrelación
    if 1<=tr<=3 or 0.1<=pr<=24:
        k=0.06125*t*exp(-1.2*(1-t)**2)
        x1=-k*pr
        x2=14.76*t - 9.76*t**2 + 4.58*t**3
        x3=90.7*t - 242.2*t**2 + 42.4*t**3
        x4=2.18 + 2.82*t
        densidad_reducida = lambda y: x1+(y+y**2+y**3-y**4)/(1-y)**3-x2*y**2+x3*y**x4
        derivada_densidad= lambda y: (y**4-4*y**3+4*y**2+4*y+1)/(1-y)**4-2*x2*y+x3*x4*y**(x4-1)
        y_sol = newton(func=densidad_reducida,fprime=derivada_densidad, x0=0.1, tol=1e-12)
        z = 0.06125*pr*t*exp(-1.2*(1-t)**2)/y_sol
        dFdy=derivada_densidad(y_sol)
        dydp=(k/y_sol)/(dFdy+pr*k/y_sol**2)
        dzdp=k*(y_sol-pr*dydp)/y_sol**2
        cg=(1/pr-1/z*dzdp)/presion_critica
        return z,cg
    else:
        print("los valores estan fuera de rango para la correlacion")
        return None
    
def Dranchuk_Abu_Kassem(presion_critica,temperatura_critica, presion, temperatura):
#Correlación de Dranchuk_Abu_Kassem, calcula el factor Z y la compresibilidad del gas
#llama a la correlación mediante z,cg=Dranchuk_Abu_Kassem(presion_critica,temperatura_critica, presion, temperatura)
    a = [0.3265, -1.0700, -0.5339, 0.01569, -0.05165, 0.5475, -0.7361, 0.1844, 0.1056, 0.6134, 0.7210]
    pr=presion/presion_critica
    tr=temperatura/temperatura_critica
    #Límites de la correlación
    if 1<=tr<=3 or 0.2<=pr<=30:
        r1=a[0]+ a[1]/tr + a[2]/tr**3+ a[3]/tr**4 + a[4]/tr**5
        r2=0.27*pr/tr
        r3=a[5] + a[6]/tr + a[7]/tr**2
        r4=a[8]*(a[6]/tr+a[7]/tr**2)
        r5=a[9]/tr**3
        f=lambda x: r1*x-r2/x+r3*x**2-r4*x**5+r5*(1+a[10]*x**2)*x**2*exp(-a[10]*x**2)+1
        df=lambda x: r1+r2/x**2+2*r3*x-5*r4*x**4+2*r5*x*exp(-a[10]*x**2)*((1+2*a[10]*x**3)-a[10]*x**2*(1+a[10]*x**2))
        rho_sol = newton(func=f,fprime=df, x0=r2, tol=1e-12)
        z=0.27*pr/(rho_sol*tr)
        dzdro=df(rho_sol)-r2/rho_sol**2
        dzdpr=0.27/(tr*z)*dzdro/(1+rho_sol*dzdro/z)
        cg=(1/pr-1/z*dzdpr)/presion_critica
        return z,cg
    else:
        print("La correlación no es válida para dicho rango")
        return None
    
def Dranchuk_Purvis_Robinson(presion_critica,temperatura_critica, presion, temperatura):
 #Correlación de Dranchuk_Purvis_Robinson, calcula el factor Z y la compresibilidad del gas
#llama a la correlación mediante z,cg=Dranchuk_Purvis_Robinson(presion_critica,temperatura_critica, presion, temperatura) 
    a = [0.31506237, -1.0467099, -0.57832720, 0.53530771, -0.61232032, -0.10488813, 0.68157001, 0.68446549]
    pr=presion/presion_critica
    tr=temperatura/temperatura_critica
    if 1.05<=tr<=3 or 0.2<=pr<=30:
        t1=a[0]+a[1]/tr+a[2]/tr**3
        t2=a[3]+a[4]/tr
        t3=a[4]*a[5]/tr
        t4=a[6]/tr**3
        t5=0.27*pr/tr
        f=lambda x: 1+t1*x+t2*x**2+t3*x**5+t4*x**2*(1+a[7]*x**2)*exp(-a[7]*x**2)-t5/x
        df=lambda x: t1+2*t2*x+5*t3*x**2+2*t4*x*(1+a[7]*x**2-a[7]**2*x**4)*exp(-a[7]*x**2)+t5/x**2
        rho_sol = newton(func=f,fprime=df, x0=t5, tol=1e-12)
        z=0.27*pr/(rho_sol*tr)
        dzdro=df(rho_sol)-t5/rho_sol**2
        dzdpr=0.27/(tr*z)*dzdro/(1+rho_sol*dzdro/z)
        cg=(1/pr-1/z*dzdpr)/presion_critica
        return z, cg
    else:
        print("La correlacion no funciona en el rango proporcionado")
    return None

