= 1604. В Стране Дураков

_Ограничение времени: 1.0 секунды_ \
_Ограничение памяти: 64 МБ_


Главный бульдог-полицейский Страны Дураков решил ввести ограничение скоростного
режима на автомобильной трассе, ведущей от Поля Чудес к пруду Черепахи Тортиллы.
Для этого он заказал у Папы Карло n знаков ограничения скорости. Папа Карло
слабо разбирался в дорожном движении и поэтому изготовил знаки с разными
ограничениями на скорость: 49 км/ч, 34 км/ч, 42 км/ч, и т.д. Всего получилось k
различных ограничений: n1 знаков с одним ограничением, n2 знаков со вторым
ограничением, и т.д. (n1 + … + nk = n)

Бульдог-полицейский ничуть не расстроился, получив такие знаки, напротив, он
решил извлечь из этого экономическую выгоду. Дело в том, что по Правилам
дорожного движения Страны Дураков ограничение на скорость действует вплоть до
следующего знака. Если на знаке написано число 60, это означает, что участок от
данного знака до следующего нужно проехать ровно со скоростью 60 километров в
час — не больше и не меньше. Бульдог распорядился расставить знаки так, чтобы
обогатившимся на Поле Чудес автолюбителям во время своего движения по трассе
приходилось как можно больше раз менять скорость. Для этого нужно расставить
имеющиеся знаки в правильном порядке. Если Вы поможете бульдогу это сделать, то
он готов будет поделиться с Вами частью своих доходов.

== Исходные данные

В первой строке дано число k — количество различных типов знаков с ограничением
скорости (1 ≤ k ≤ 10000). Во второй строке через пробел перечислены целые
положительные числа n1, …, nk. Сумма всех ni не превосходит 10000. Результат

Выведите n целых чисел в пределах от 1 до k — порядок, в котором нужно
расставить по трассе имеющиеся знаки. Вне зависимости от того, какой знак стоит
первым, считается, что, проезжая его, водитель меняет скорость, так как до этого
ограничения не действовали. Если задача имеет несколько решений, выведите любое.


== Пример 
*исходные данные* \
2 \
2 2 

*результат*
1 2 1 2 \

_Автор задачи: Александр Ипатов (идея — Александр Торопов)_ \
_Источник задачи: Девятое открытое личное первенство УрГУ (1 марта 2008)_

== Решение
На языке Python

#raw(read("1604.py"), lang: "python")

== Про решение

Используем структуру данных Priority-Queue и ее свойство
$A_0 = max A$, где $A_0$ - первый элемент структуры для поиска самого частого знака.

Чередуем первый и второй элементы пока второй не израсходуется.
Если израсходовали элемент назад его не возвращаем.