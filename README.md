
# Auto Login

Очередная маленькая лентяйская утилита. Вводит некоторые данные в поле определённого окна и завершается. Например логин в какой-то программе. По сути просто очередная приколюха на питоне).

Конфигурация утилиты выполняется в файле **auto_login.ini**.  
Параметры файла конфигурации:  
`delay` - целое число. Интервал проверки значения (задержка главного цикла программы) в секундах.  
`valid_foreground_window_title` - строка. Заголовок или часть заголовка окна программы, за которой нужно наблюдать.  
`password` - строка. Может быть как паролем, так и чем-нибудь другим.  
`debug_print` - целое число (1 или 0). Вывод различной отладочной информации в консоль. 1 - включено, 0 - выключено.

Скачать EXE-файл утилиты можно [здесь](https://github.com/marfikus/auto-login/releases/). Собирал через [Auto PY to EXE](https://pypi.org/project/auto-py-to-exe/).
