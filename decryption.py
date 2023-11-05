import pyAesCrypt
import os


# функция дешифровки 

def decryption(file, password):
    # задаем размер буфeра
    buffer_size = 512 * 1024
    
    # вызываем метод дешифровки 
    
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
    
    # выводим результат
    
    print("[Файл '" + str(os.path.splitext(file[0]) + "' зашифрован]"))
    
    # удаляем исходный файл 
    
    os.remove(file)
    
    
    
    
# функция обхода директорий 


def walking_by_dirs(dir, password):
    # перебираем все поддиректории в указанной директории
    
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        
        # если находим файл то дешифруем его 
        
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию , то продалжаем цикл в поисках файлов
        
        else:
            walking_by_dirs(dir, password)
            
            
password = input("Введите пароль для шифрования: ")
walking_by_dirs("/home/daniil/myStaf", password)