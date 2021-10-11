import time
import threading
import logging
import queue

class Philosopher:
    def __init__(self,num) -> None:
        self.name = f'Filósofo {num}'

    def __str__(self) -> str:
        return self.name

    def eat(self):
        return 'Está comiendo'
    
    def grab_forks(self):
        return 'Toma los 2 tenedores'
    
    def finish_meal(self):
        return 'Terminó de comer'
    
lock = threading.Lock()

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def show_elements(my_queue):
    while not my_queue.empty():
        item = my_queue.get()
        with lock:
            logging.info(f'El {item} {item.grab_forks()}')
            logging.info(f'El {item} {item.eat()}')
            time.sleep(1)
            logging.info(f'El {item} {item.finish_meal()}')
        my_queue.task_done()

        time.sleep(0.5)

if __name__ == '__main__':
    total_philo = int(input("Ingrese cuantos filósofos cenarán: "))
    queue_philo = queue.Queue(maxsize=total_philo)
    i=1
    while not queue_philo.full():
        new_philo = Philosopher(i)
        queue_philo.put(new_philo)
        i+=1

    for _ in range(4):
        thread = threading.Thread(target=show_elements,args=([queue_philo]))
        thread.start()