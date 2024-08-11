import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for transactions in range(100):
            random_deposit = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            elif self.balance < 500 and self.lock.locked():
                self.balance += random_deposit
                print(f'Пополнение: {random_deposit}. Баланс: {self.balance}')
                self.lock.release()
            sleep(0.001)

    def take(self):
        for transactions in range(100):
            random_take = randint(50, 500)
            print(f'Запрос на {random_take}')
            if random_take <= self.balance:
                self.balance -= random_take
                print(f'Снятие: {random_take}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
