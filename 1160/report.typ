= 1160. Network

== Условие
Andrew is working as system administrator and is planning to establish a new
network in his company. There will be N hubs in the company, they can be
connected to each other using cables. Since each worker of the company must
have access to the whole network, each hub must be accessible by cables from
any other hub (with possibly some intermediate hubs).


== Входные данные
The first line contains two integer: $N$ - the number of hubs in the network $(2 <=
N <= 1000)$ and $M$ — the number of possible hub connections $(1 <= M <= 15000)$. All
hubs are numbered from 1 to $N$. The following $M$ lines contain information about
possible connections - the numbers of two hubs, which can be connected and the
cable length required to connect them. Length is a positive integer number that
does not exceed 106. There will be no more than one way to connect two hubs. A
hub cannot be connected to itself. There will always be at least one way to
connect all hubs. 

== Результат
Output first the maximum length of a single cable in your hub connection plan
(the value you should minimize). Then output your plan: first output $P$ - the
number of cables used, then output $P$ pairs of integer numbers - numbers of hubs
connected by the corresponding cable. Separate numbers by spaces and/or line
breaks. 

== Примеры
=== исходные данные
```
4 6
1 2 1
1 3 1
1 4 2
2 3 1
3 4 1
2 4 1
```

=== результат
```
1
4
1 2
1 3
2 3
3 4
```

== Успешная попытка
#image("AC.png")

== Решение
На языке Python3.12

#raw(read("1160.py"), lang: "py")

== Про решение 

Использовали алгоритм Краскала для выбора ребер в порядке возрастания весаю.


