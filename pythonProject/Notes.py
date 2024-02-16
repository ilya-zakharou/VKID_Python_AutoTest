import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print(fun(5))
#selenium_env\Scripts\activate.bat //активировать
#selenium_env\Scripts\deactivate.bat  //деактивировать
#python -m pip install selenium==3.14.0    // установить библиотеку селениум
# python setup.py install  // установть
# path - проверка установленных драйверов (chrome driver)
#