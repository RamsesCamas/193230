import threading
import time


class TenedorFilosofo(threading.Thread):
    def __init__(self, tenedores, filosofosNum):
        threading.Thread.__init__(self)
        self.tenedores = tenedores
        self.filosofosNum = filosofosNum
        self.datoTemporal =  (filosofosNum + 1) % 5
        self.start()
   
    def hilosFilosofos(self):
        print("Filosofo iniciando", self.filosofosNum)
        time.sleep(2)
        self.tenedores[self.filosofosNum].acquire()
        time.sleep(1)
        print("Filosofo ", self.filosofosNum, "recoge tenedor del lado derecho")
        time.sleep(1)

        self.tenedores[self.datoTemporal].acquire()
        print("Filosofo ", self.filosofosNum, "recoge tenedor del lado izquierdo")
        time.sleep(0.5)

        print("Filosofo ", self.filosofosNum, "libre izquierdo")
        self.tenedores[self.datoTemporal].release()
        time.sleep(0.5)

        print("Filosofo ", self.filosofosNum, "libre derecho")
        self.tenedores[self.filosofosNum].release()
        time.sleep(2)

    def run(self):
        self.hilosFilosofos()
        


tenedorArray = [1,1,1,1,1]

if __name__ == '__main__':
    for i in range(0,5):
        tenedorArray[i] = threading.BoundedSemaphore(2)

    for i in range(0,5):
        total = TenedorFilosofo(tenedorArray, i)
        time.sleep(2)