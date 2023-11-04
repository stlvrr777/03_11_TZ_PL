import sys
import math

args = sys.argv

file1 = args[1]
file2 = args[2]

coord = []
rad = None
counter = 0

def count(coord, rad, check):

    d = math.sqrt((check[0] - coord[0])**2 + (check[1] - coord[1])**2)
    if d > rad:
        return 2
    elif d == rad:
        return 0
    else:
        return 1

try:
    with open(file1, 'r') as file1:
        
        coord = [float(x) for x in file1.readline().strip().split()]
        rad = float(file1.readline().strip())

    with open(file2, 'r') as file2:
        counter = 0
        for line in file2:
            if counter >= 100:
                break  # Прерываем чтение после 100 строк
            t = [float(x) for x in line.strip().split()] 
            print(count(coord, rad, t))
            counter += 1
            
except FileNotFoundError as e:
    print(f"Файл не найден: {e.filename}")
except Exception as e:
    print(f"Ошибка чтения файла: {e}")


    