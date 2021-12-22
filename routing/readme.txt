1. Нужно написать view simple_route, которая формирует http ответ с пустым телом со статусом 200 на запрос GET (если запросы отличные от GET - возвращать 405) по /routing/simple_route/:

Кейсы:

Метод	Путь	Статус	Тело
get	/routing/simple_route/	200	Пустое
get	/routing/simple_route/blabla	404	-
post	/routing/simple_route/	405	-
put	/routing/simple_route/ 	405	-
Замечание: "-" в столбце "тело" означает, что в грейдере тело не проверяется

2. slug_route - нужно написать view, которая принимает slug и отдает его в теле ответа. В slug допустимы символы: 0-9, a-z, -, _ . Минимальная длина 1 символ, максимальная длина 16.

Кейсы:

Метод	Путь	Статус	Тело
get	/routing/slug_route/a-1s_d2/	200	a-1s_d2
get	/routing/slug_route/1411rwasf123412341234/	404	-
get	/routing/slug_route/.4/24][/	404	-
3. sum_route - нужно написать view, которая принимает 2 числа и их суммирует, например /routing/sum_route/1/2/

Кейсы:

Метод	Путь	Статус	Тело
get	/routing/sum_route/1/2/	200	3
get	/routing/sum_route/1/-2/	200	-1
get	/routing/sum_route/1/b/	404	-
get	/routing/sum_route/a/2/	404	-
4. sum_get_method - нужно написать view, которая принимает 2 числа из GET параметров a и b и суммирует их. Допускается только метод GET. Например /routing/sum_get_method/?а=1&b=2

Кейсы:

Метод	Путь	Статус	Тело
get	/routing/sum_get_method/?a=1&b=2	200	3
get	/routing/sum_get_method/?a=1&b=-2	200	-1
get	/routing/sum_get_method/?a=1&b=b	400	-
get	/routing/sum_get_method/?a=a&b=2	400	-
get	/routing/sum_get_method/	400	-
5. sum_post_method - нужно написать view, которая принимает 2 числа из POST параметров a и b и суммирует их. Допускается только метод POST. Например /routing/sum_post_method/

Кейсы:

Путь	Парам.	Статус	Тело
/routing/sum_post_method/	a=1&b=2	200	3
/routing/sum_post_method/	a=1&b=-2	200	-1
/routing/sum_post_method/	a=1&b=b	400	-
/routing/sum_post_method/	a=a&b=2	400	-
/routing/sum_post_method/	-	400	-
