from .phases_data import data as phases 

## Defino una clase donde voy a almacenar cada par de puntos del grafico (con su temp y $ de C)
class punto:
    def __init__(self, porc, temp):
        self.porc = porc
        self.temp = temp


A = punto(0, 1500)
C = punto(4.3, 1147)
D = punto(6.67, 1320)
E = punto(2.06, 1147)
F = punto(6.67, 1147)
G = punto(0, 911)
P = punto(0.02, 723)
S = punto(0.8, 723)
Q = punto(0, 20)


## Defino una funcion para sacar temp en fn del porcentaje de C dentro de una linea (por interpolacion)
## Obtinene el valor de la temperatura para la linea entre 2 puntos para un cierto porc
def interp_temp(punto1, punto2, porc):
    temp = punto1.temp + ((punto2.temp - punto1.temp) / (punto2.porc - punto1.porc)) * (
        porc - punto1.porc
    )
    return temp


## Defino una funcion para sacar % de C en fn de la temp dentro de una linea (por interpolacion)
## Obtinene el valor del porc para la linea entre 2 puntos para un cierto temp
def interp_porc(punto1, punto2, temp):
    porc = (
        ((temp - punto1.temp) * (punto2.porc - punto1.porc))
        / (punto2.temp - punto1.temp)
    ) + punto1.porc
    return porc


## Defino una funcion que calcule el % de los componentes a la izq y a la derecha segun la ley de segmento opesto
def segm_op(porc_sat_izq, porc_sat_der, porc_mezcla):
    long_seg = porc_sat_der - porc_sat_izq
    porc_izq = (porc_sat_der - porc_mezcla) / long_seg
    porc_der = (porc_mezcla - porc_sat_izq) / long_seg
    return porc_izq * 100, porc_der * 100


def get_phase(
    porc, temp
):  ## La funcion va a tomar como parametro el punto, y va a devolver el nombre del estado y los porc en caso de ser mezcla

    if porc > 0 and porc <= 0.02:  ##Para aceros dulces

        if temp >= 1500:  ## Arriba de 1500 para ese % es siempre 100% liquido
            return [{"name": "Liquido", "porc": 100}]  # , porc, "C", 100-porc, "Fe"

        elif temp < 1500 and temp >= interp_temp(
            G, S, porc
        ):  ## En este sector es austenita pura
            return [{"name": "Austenita", "porc": 100}]  # , porc, "C", 100-porc, "Fe"

        elif temp < interp_temp(G, S, porc) and temp >= interp_temp(
            G, P, porc
        ):  ## A partir de aqui una parte de la austenita se hace ferrita
            porc_ferr, porc_aust = segm_op(
                interp_porc(G, P, temp), interp_porc(G, S, temp), porc
            )
            return [
                {"name": "Austenita", "porc": porc_aust},
                {"name": "Ferrita", "porc": porc_ferr},
            ]

        elif temp < interp_temp(G, P, porc) and temp >= interp_temp(Q, P, porc):
            return [{"name": "Ferrita", "porc": 100}]

        elif temp < interp_temp(Q, P, porc) and temp > 0:
            porc_ferr, porc_cement = segm_op(
                interp_porc(Q, P, temp), 6.67, porc
            )  ## Aca directamente no hay una curva sino que es la vertical en Fe3C
            return [
                {"name": "Ferrita", "porc": porc_ferr},
                {"name": "Cementita", "porc": porc_cement, "num": "III"},
            ]

        else:
            return 1

    if porc > 0.02 and porc <= 0.8:  ##Para aceros bajo y medio carbono

        if temp > interp_temp(A, C, porc):
            return [{"name": "Liquido", "porc": 100}]

        elif temp < interp_temp(A, C, porc) and temp >= interp_temp(A, E, porc):
            porc_aust, porc_liq = segm_op(
                interp_porc(A, E, temp), interp_porc(A, C, temp), porc
            )
            return [
                {"name": "Liquido", "porc": porc_liq},
                {"name": "Austenita", "porc": porc_aust},
            ]

        elif temp < interp_temp(A, E, porc) and temp >= interp_temp(G, S, porc):
            return [{"name": "Austenita", "porc": 100}]

        elif (
            temp < interp_temp(G, S, porc) and temp >= 769
        ):  ## A 796 tiene lugar la eutectoide
            porc_ferr, porc_aust = segm_op(
                interp_porc(G, P, temp), interp_porc(G, S, temp), porc
            )
            return [
                {"name": "Austenita", "porc": porc_aust},
                {"name": "Ferrita", "porc": porc_ferr},
            ]
        elif temp < 769 and temp > 0:
            ## Primero veo cuanto era el % de austenita antes de la eutectoide:
            porc_aust_transf, porc_ferr = segm_op(0.02, 0.8, porc)
            ## ahora toda esa austenita se convierte en perlita, el resto de la ferrita deviene en alfa y cementita
            porc_ferr, porc_cement = segm_op(interp_porc(Q, P, temp), 6.67, porc)
            return [
                {"name": "Perlita", "porc": porc_aust_transf},
                {
                    "name": "Ferrita",
                    "pure": True,
                    "porc": porc_ferr * (1 - porc_aust_transf / 100),
                },
                {
                    "name": "Perlita",
                    "num": "III",
                    "porc": porc_cement * (1 - porc_aust_transf / 100),
                },
            ]
        else:
            return 1

    if porc > 0.8 and porc <= 2.06:

        if temp > interp_temp(A, C, porc):
            return [{"name": "Liquido", "porc": 100}]

        elif temp < interp_temp(A, C, porc) and temp >= interp_temp(A, E, porc):
            porc_aust, porc_liq = segm_op(
                interp_porc(A, E, temp), interp_porc(A, C, temp), porc
            )
            return [
                {"name": "Liquido", "porc": porc_liq},
                {"name": "Austenita", "porc": porc_aust},
            ]

        elif temp < interp_temp(A, E, porc) and temp >= interp_temp(S, E, porc):
            return [{"name": "Austenita", "porc": 100}]

        elif (
            temp < interp_temp(S, E, porc) and temp >= 769
        ):  ## ahora la austenita se va a ir transformando en cementita 2
            porc_aust, porc_cement = segm_op(interp_porc(S, E, temp), 6.67, porc)
            return [
                {"name": "Austenita", "porc": porc_aust},
                {"name": "Cementita", "num": "II", "porc": porc_cement},
            ]

        elif temp < 769 and temp > 0:
            ## Primero veo cuanto era el % de austenita antes de la eutectoide:
            porc_aust_transf, porc_cement = segm_op(0.8, 6.67, porc)
            ## Para simplificar asumimos que la relacion se mantiene estable
            return [
                {"name": "Perlita", "porc": porc_aust_transf},
                {"name": "Cementita", "num": "II", "porc": porc_cement},
            ]
        else:
            return 1

    if porc > 2.06 and porc <= 4.3:

        if temp > interp_temp(A, C, porc):
            return [{"name": "Liquido", "porc": 100}]
        elif (
            temp < interp_temp(A, C, porc) and temp >= 1147
        ):  ##1147 es la temperatura del eutectico
            porc_aust, porc_liq = segm_op(
                interp_porc(A, E, temp), interp_porc(A, C, temp), porc
           )
            return [
                {"name": "Liquido", "porc": porc_liq},
                {"name": "Austenita", "porc": porc_aust},
            ]

        elif (
            temp < 1147
        ):  # and temp >= 723:  ###REVISAR TODO ESTO - No se si metalurgicamente es correcto el calculo
            # Primero veo cuanto liquido habia antes de la reacc eutectica
            porc_aust_preeutectica, porc_liq_preeutect = segm_op(2.06, 4.3, porc)
            porc_ledeb_transf = porc_liq_preeutect

            # al bajar de 1147, todo el liquido se convierte en ledeburita, la cual tiene aust y cementita en las sig prop
            porc_aust_ledeb_eutectica, porc_cement_ledeb_eutectica = segm_op(
                2.06, 6.67, 4.3
            )

            # es decir que el total de austenita y cementita contenidas en la ledeburita (respecto del total) es
            porc_aust_ledeb_total = porc_aust_ledeb_eutectica * (
                porc_liq_preeutect / 100
            )
            porc_cement_ledeb_total = porc_cement_ledeb_eutectica * (
                porc_liq_preeutect / 100
            )

            # Ahora, para cualquier temp, la cantidad "total" de cementita y austenita sera:
            porc_aust_total, porc_cement_total = segm_op(
                interp_porc(S, E, temp), 6.67, porc
            )

            # pero las cantidades "sueltas" de aust y cement seran esas menos las que estan contenidas en la ledeb, osea
            porc_aust_suelta = porc_aust_total - porc_aust_ledeb_total
            porc_cement_suelta = porc_cement_total - porc_cement_ledeb_total

            # SI la temperatura esta arriba de la eutectoide, devuelvo:
            if temp >= 723:
                return [
                    {"name": "Austenita", "porc": porc_aust_suelta},
                    {
                        "name": "Ledeburita",
                        "pure": True,
                        "porc": porc_ledeb_transf,
                    },
                    {
                        "name": "Cementita",
                        "num": "II",
                        "pure": True,
                        "porc": porc_cement_suelta,
                    },
                ]

            # si no, tiene lugar la eutectoide y la austenita se transforma en perlita, y la ledeburita I en II
            elif temp > 0:
                return [
                    {"name": "Perlita", "porc": porc_aust_suelta},
                    {
                        "name": "Ledeburita",
                        "num": "II",
                        "porc": porc_ledeb_transf,
                    },
                    {
                        "name": "Cementita",
                        "pure": True,
                        "num": "II",
                        "porc": porc_cement_suelta,
                    },
                ]

        else:
            return 1

    if porc > 4.3 and porc <= 6.67:

        if temp > interp_temp(C, D, porc):
            return [{"name": "Liquido", "porc": 100}]

        elif (
            temp < interp_temp(C, D, porc) and temp >= 1147
        ):  ##1147 es la temperatura del eutectico
            porc_liq, porc_cement = segm_op(interp_porc(C, D, temp), 6.67, porc)
            return [
                {"name": "Liquido", "porc": porc_liq},
                {"name": "Cementita", "num":"I", "porc": porc_cement},
            ]

        elif temp < 1147:
            porc_ledeb, porc_cement = segm_op(4.3, 6.67, porc)
            if temp > 723:
                return [
                    {
                        "name": "Ledeburita",
                        "num": "I",
                        "porc": porc_ledeb,
                    },
                    {
                        "name": "Cementita",
                        "num": "I",
                        "porc": porc_cement,
                    },
                ]
            elif temp > 0:
                return [
                    {
                        "name": "Ledeburita",
                        "num": "II",
                        "porc": porc_ledeb,
                    },
                    {
                        "name": "Cementita",
                        "num": "I",
                        "porc": porc_cement,
                    },
                ]
            else:
                return 1

def main(p,t):
    data = get_phase(p, t)
    anexed =  [ 
        {   
            **item, 
            **next((phase for phase in phases if phase.get('name') == item.get('name')), None)
        } for item in data
    ]
    return anexed
