"""
Реализуйте класс Primes, позволяющий проводить перебор простых чисел на
интервале [A; B) (т.е включая A и не включая B).

Пример использования класса Primes:

a = 1
b = 10

primes = Primes(a, b)
for p in primes:
    print(p)

# 2
# 3
# 5
# 7

В этом файле уже реализована функция is_prime, принимающая число n и
возвращающая логическое значение, отражающее простоту числа n. Вы можете
использовать ее при решении поставленной задачи.


Число называется простым, если оно имеет ровно два различных натуральных
делителя. Например, число 2 считается простым, так как делится только на 1 и 2,
а число 4 - нет (оно делится на 1, 2 и 4).
https://ru.wikipedia.org/wiki/Простое_число
"""


def is_prime(n: int) -> bool:
    n = abs(n)

    if n == 2 or n == 3:
        return True

    if n < 2 or n % 2 == 0:
        return False

    if n < 9:
        return True

    if n % 3 == 0:
        return False

    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


class Primes:
    def __init__(self, start, end):
        ### начало решения
        self.current = start
        self.end = end
        ### конец решения

    def __next__(self):
        ### начало решения
        while True:
            if self.current >= self.end:
                raise StopIteration

            _current, self.current = self.current, self.current + 1

            if is_prime(_current):
                return _current
        ### конец решения

    def __iter__(self):
        ### начало решения
        return self
        ### конец решения