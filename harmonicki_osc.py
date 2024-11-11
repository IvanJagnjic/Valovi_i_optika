######################################################################
"""/*if self.brzina > 0:
    otpor = -otpor_zraka
else:
    otpor = otpor_zraka
self.brzina = self.brzina + a * self.dt + self.dt * otpor / self.m"""
#############################################################################
import numpy as np
import math as m
import matplotlib.pyplot as plt


class Oscilator:
    def __init__(self, k, x0, brzina, dt, m,koef_otpora):
        self.brzina = brzina
        self.x0 = x0
        self.brzina = brzina
        self.k = k
        self.dt = dt
        self.m = m
        self.koef_otpora=koef_otpora

    def move(self, dt):
        self.x0 = self.x0 + dt * self.brzina
        pass

    def poz(self):
        print("X:", self.x0)
        pass


    def graf(self,n):
        poc_brzina = self.brzina
        poc_x0 = self.x0

        period = 0
        x_pocetna = self.x0
        lista_x = []
        lista_t = []
        lista_a = []
        lista_v = []

        while period < 10:
            otpor =m.fabs(pow(self.brzina,n)*self.koef_otpora)
            Fel = -1 * self.k*self.x0-np.sign(self.brzina)*otpor
            a = Fel / self.m
            self.move(self.dt)

            self.brzina = self.brzina + a * self.dt
            period = period + self.dt
            # self.poz()
            lista_x.append(self.x0)
            lista_t.append(period)
            lista_a.append(a)
            lista_v.append(self.brzina)
        self.brzina = poc_brzina
        self.x0 = poc_x0
        self.x0 = x_pocetna
        period = 0

        return [lista_x, lista_v, lista_a, lista_t]

    def graf_po_dt(self, t1, t2, n):
        lista_t = np.linspace(t1, t2, n)
        lista_lista_x = []
        lista_lista_t = []
        for i in lista_t:
            self.dt = i
            [lista_x, b, c, lista_t] = self.graf()
            lista_lista_x.append(lista_x)
            lista_lista_t.append(lista_t)
        br = 0
        for i in lista_lista_x:
            plt.plot(lista_lista_t[br], i)
            br = br + 1

        plt.title("x/t graf u ovisnosti o koraku dt")
        plt.show()
        pass

    def period_titranja_numericki(self):
        return (2 * m.pi * m.sqrt(float(self.m) / self.k))

    def prikazi_graf(self):
        [y1, y2, y3, x] = self.graf(1)
        [y12, y22, y32, x2] = self.graf(2)

        plt.subplot(1, 3, 1)
        plt.plot(x, y1,label="Ovisnost o v")
        plt.plot(x2, y12,label="Ovisnost o v^2")
        plt.title("Ovisnost x o vremenu:")
        plt.legend()

        plt.subplot(1, 3, 2)
        plt.plot(x, y2,label="Ovisnost o v")
        plt.plot(x2, y22,label="Ovisnost o v^2")
        plt.title("Ovisnost v o vremenu:")
        plt.legend()

        plt.subplot(1, 3, 3)
        plt.plot(x, y3,label="Ovisnost o v")
        plt.plot(x2, y32,label="Ovisnost o v^2")
        plt.title("Ovisnost a o vremenu:")
        plt.legend()
        plt.show()


cestica = Oscilator(150, 6, 15, 0.001, 10,0.25)
cestica.prikazi_graf()