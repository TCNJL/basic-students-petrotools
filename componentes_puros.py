class ComponentePuro:
    _tabla_propiedades_criticas = {
      # Alcanos lineales
    "metano": {
        "presion": 666.4,        # psia
        "temperatura": 343.0,    # °R
        "volumen_critico": 1.59, # ft³/lbmol
        "z_critico": 0.286,      # Factor de compresibilidad crítico (adimensional)
        "factor_acentrico": 0.011,
        "peso_molecular": 16.04  # lb/lbmol (g/mol)
    },
    "etano": {
        "presion": 706.5,
        "temperatura": 549.6,
        "volumen_critico": 2.37,
        "z_critico": 0.284,
        "factor_acentrico": 0.099,
        "peso_molecular": 30.07
    },
    "propano": {
        "presion": 616.3,
        "temperatura": 665.7,
        "volumen_critico": 3.20,
        "z_critico": 0.276,
        "factor_acentrico": 0.152,
        "peso_molecular": 44.10
    },
    "n-butano": {
        "presion": 550.7,
        "temperatura": 765.3,
        "volumen_critico": 4.08,
        "z_critico": 0.274,
        "factor_acentrico": 0.193,
        "peso_molecular": 58.12
    },
    "isobutano": {
        "presion": 529.1,
        "temperatura": 734.6,
        "volumen_critico": 4.21,
        "z_critico": 0.275,
        "factor_acentrico": 0.183,
        "peso_molecular": 58.12
    },
    "n-pentano": {
        "presion": 488.6,
        "temperatura": 845.4,
        "volumen_critico": 5.01,
        "z_critico": 0.262,
        "factor_acentrico": 0.251,
        "peso_molecular": 72.15
    },
    "isopentano": {
        "presion": 490.4,
        "temperatura": 828.8,
        "volumen_critico": 5.14,
        "z_critico": 0.268,
        "factor_acentrico": 0.227,
        "peso_molecular": 72.15
    },
    "neopentano": {
        "presion": 464.0,
        "temperatura": 789.6,
        "volumen_critico": 5.31,
        "z_critico": 0.269,
        "factor_acentrico": 0.197,
        "peso_molecular": 72.15
    },
    "n-hexano": {
        "presion": 436.9,
        "temperatura": 913.3,
        "volumen_critico": 5.93,
        "z_critico": 0.260,
        "factor_acentrico": 0.301,
        "peso_molecular": 86.18
    },
    "2-metilpentano": {
        "presion": 436.6,
        "temperatura": 899.6,
        "volumen_critico": 6.02,
        "z_critico": 0.264,
        "factor_acentrico": 0.279,
        "peso_molecular": 86.18
    },
    "3-metilpentano": {
        "presion": 453.1,
        "temperatura": 905.4,
        "volumen_critico": 5.98,
        "z_critico": 0.263,
        "factor_acentrico": 0.275,
        "peso_molecular": 86.18
    },
    "2,2-dimetilbutano": {
        "presion": 447.3,
        "temperatura": 870.5,
        "volumen_critico": 6.21,
        "z_critico": 0.266,
        "factor_acentrico": 0.232,
        "peso_molecular": 86.18
    },
    "2,3-dimetilbutano": {
        "presion": 453.9,
        "temperatura": 896.4,
        "volumen_critico": 6.10,
        "z_critico": 0.265,
        "factor_acentrico": 0.248,
        "peso_molecular": 86.18
    },
   "agua": {
        "presion": 3208.2,       # psia
        "temperatura": 1165.1,    # °R (647.3 K × 1.8)
        "volumen_critico": 0.0509, # ft³/lbmol (0.0560 m³/kmol → ft³/lbmol)
        "z_critico": 0.229,       # Factor de compresibilidad crítico
        "factor_acentrico": 0.344,
        "peso_molecular": 18.015  # lb/lbmol (g/mol)
    },
   "monoxido_de_carbono": {
        "presion": 507.6,         # psia
        "temperatura": 239.3,     # °R (132.9 K × 1.8)
        "volumen_critico": 1.49,  # ft³/lbmol
        "z_critico": 0.295,
        "factor_acentrico": 0.066,
        "peso_molecular": 28.01
    },
   "dioxido_de_carbono": {
        "presion": 1070.6,        # psia
        "temperatura": 547.6,     # °R (304.2 K × 1.8)
        "volumen_critico": 1.51,  # ft³/lbmol
        "z_critico": 0.274,
        "factor_acentrico": 0.225,
        "peso_molecular": 44.01
    },
   "acido_sulfhidrico": {
        "presion": 1306.0,        # psia
        "temperatura": 672.4,     # °R (373.6 K × 1.8)
        "volumen_critico": 1.66,  # ft³/lbmol
        "z_critico": 0.284,
        "factor_acentrico": 0.100,
        "peso_molecular": 34.08
    },
   "nitrogeno": {
        "presion": 492.8,         # psia
        "temperatura": 227.3,     # °R (126.2 K × 1.8)
        "volumen_critico": 1.44,  # ft³/lbmol
        "z_critico": 0.289,
        "factor_acentrico": 0.040,
        "peso_molecular": 28.01
    }
   }
    def __init__(self, nombre):
        self.nombre=nombre
        buscar = lambda prop: self._tabla_propiedades_criticas.get(self.nombre, {}).get(prop, 0)
        self.PresionCritica = buscar("presion")
        self.TemperaturaCritica=buscar("temperatura")
        self.VolumenCritico=buscar("volumen_critico")
        self.FactorZ=buscar("zcritico")
        self.FactorAcentrico=buscar("factor_acentrico")
        self.PesoMolecular=buscar("peso_molecular")

class C6Plus:
    _tabla_katz_firoozabadi = {
    "peso_molecular": {
        "a1": -131.11375,
        "a2": 24.96156,
        "a3": -0.34079022,
        "a4": 2.4941184e-3,
        "a5": 468.32575
    },
    "temperatura_critica": {
        "a1": 915.53747,
        "a2": 41.421337,
        "a3": -0.7586859,
        "a4": 5.8675351e-3,
        "a5": -1.3028779e3
    },
    "presion_critica": {
        "a1": 275.56275,
        "a2": -12.522269,
        "a3": 0.29926384,
        "a4": -2.8452129e-3,
        "a5": 1.7117226e3
    },
    "temperatura_ebullicion": {
        "a1": 434.38878,
        "a2": 50.125279,
        "a3": -0.9097293,
        "a4": 7.0280657e-3,
        "a5": -601.85651
    },
    "gamma": {
        "a1": 0.86714949,
        "a2": 3.4143408e-3,
        "a3": -2.839627e-5,
        "a4": 2.4943308e-8,
        "a5": -1.1627984
    },
    "volumen_critico": {
        "a1": 5.223458e-2,
        "a2": 7.87091369e-4,
        "a3": -1.9324432e-5,
        "a4": 1.7547264e-7,
        "a5": 4.4017952e-2
    }
}
    def __init__(self, carbonos):
        self.carbonos = carbonos
    def _C7Ppropiedad(self,prop):
        return (self._tabla_katz_firoozabadi[prop]["a1"] +
        self._tabla_katz_firoozabadi[prop]["a2"] * self.carbonos +
        self._tabla_katz_firoozabadi[prop]["a3"] * (self.carbonos)**2 +
        self._tabla_katz_firoozabadi[prop]["a4"] * (self.carbonos)**3 +
        self._tabla_katz_firoozabadi[prop]["a5"] / self.carbonos
        )
    @property
    def PesoMolecular(self):
        return self._C7Ppropiedad("peso_molecular")
    @property
    def TemperaturaCritica(self):
        return self._C7Ppropiedad("temperatura_critica")
    @property
    def PresionCritica(self):
        return self._C7Ppropiedad("presion_critica")
    @property
    def TemperaturaEbullicion(self):
        return self._C7Ppropiedad("temperatura_ebullicion")
    @property
    def PesoEspecifico(self):
        return self._C7Ppropiedad("gamma")
    @property
    def VolumenCritico(self):
        return self._C7Ppropiedad("volumen_critico")
    @property
    def Zcritico(self):
        return self.PresionCritica*self.VolumenCritico*self.PesoMolecular/(10.73*self.TemperaturaCritica)

class PseudoComponente:
    _tabla_Riazi_Daubert = {
    "temperatura_critica": {
        "a": 544.4,
        "b": 0.2998,
        "c": 1.0555,
        "d": -1.3478e-4,
        "e": -0.61641,
        "f": 0.0,
    },
    "presion_critica": {
        "a": 4.5203e4,
        "b": -0.8063,
        "c": 1.6015,
        "d": -1.8078e-3,
        "e": -0.3084,
        "f": 0.0,
    },
    "volumen_critico": {
        "a": 1.206e-2,
        "b": 0.20378,
        "c": -1.3036,
        "d": -2.657e-3,
        "e": 0.5287,
        "f": 2.6012e-3,
    },
    "temperatura_ebullicion": {
        "a": 6.77857,
        "b": 0.401673,
        "c": -1.58262,
        "d": 3.77409e-3,
        "e": 2.984036,
        "f": -4.25288e-3,
    }
}
    def __init__(self, PesoMolecular, PesoEspecifico):
        self.PesoMolecular = PesoMolecular
        self.PesoEspecifico = PesoEspecifico
    def _PCpropiedad(self,prop):
        if self.PesoMolecular and self.PesoEspecifico !=0:
            from math import exp
            return (self._tabla_Riazi_Daubert[prop]["a"] *
            self.PesoMolecular**self._tabla_Riazi_Daubert[prop]["b"] *
            self.PesoEspecifico**self._tabla_Riazi_Daubert[prop]["c"] *
            exp(self._tabla_Riazi_Daubert[prop]["d"]*self.PesoMolecular + 
            self._tabla_Riazi_Daubert[prop]["e"]*self.PesoEspecifico +
            self._tabla_Riazi_Daubert[prop]["f"]*self.PesoMolecular*self.PesoEspecifico))
        else:
            return None
    @property
    def TemperaturaCritica(self):
        return self._PCpropiedad("temperatura_critica")
    @property
    def PresionCritica(self):
        return self._PCpropiedad("presion_critica")
    @property
    def VolumenCritico(self):
        return self._PCpropiedad("volumen_critico")
    @property
    def TemperaturaEbullicion(self):
        return self._PCpropiedad("temperatura_ebullicion")
    @property
    def FactorAcentrico(self):
        from math import log10
        return 3*log10(self.PresionCritica/14.7)/(7*(self.TemperaturaCritica/self.TemperaturaEbullicion-1))-1
    @property
    def Zcritico(self):
        return self.PresionCritica*self.VolumenCritico*self.PesoMolecular/(10.73*self.TemperaturaCritica)
  
class MezclaComponentes:
    def __init__(self, componentes: list, fraccionM: list, c7: list):
        self.componentes = componentes
        self.FraccionMolar = fraccionM
        self.c7 = c7
        if all(x > 0 for x in self.c7):
            self.FraccionMolar.append(self.c7[2])
        self._compuestos_cache = None
    
    @property
    def compuestos(self):
        """Property que cachea la lista de compuestos"""
        if self._compuestos_cache is None:
            self._compuestos_cache = [ComponentePuro(x) for x in self.componentes]
            if not any(x == 0 for x in self.c7):
                self._compuestos_cache.append(PseudoComponente(self.c7[1], self.c7[0]))
        return self._compuestos_cache
    
    @property
    def PresionCritica(self):
        return [comp.PresionCritica for comp in self.compuestos]
    
    @property
    def TemperaturaCritica(self):
        return [comp.TemperaturaCritica for comp in self.compuestos]
    
    @property
    def VolumenCritico(self):
        return [comp.VolumenCritico for comp in self.compuestos]
    
    @property
    def PesoMolecular(self):
        pesos_moleculares = [comp.PesoMolecular for comp in self.compuestos]
        return sum(a * b for a, b in zip(self.FraccionMolar, pesos_moleculares))