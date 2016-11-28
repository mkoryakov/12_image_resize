# 12_image_resize
Скрипт принимает на вход путь к изображению (обязательный параметр) и изменяет его размеры в соответствии с заданными пользователем значениями. Необязательные параметры: width - ширина результирующей картинки, height - её высота, scale - во сколько раз увеличить изображение (может быть меньше 1), output - куда класть результирующий файл.

## Примеры использования:
* python image\_resize.py picture.png --height 150 --output new\_picture.png
* python image\_resize.py picture.png --height 150 --width 200
* python image\_resize.py picture.png --scale 0.8 
