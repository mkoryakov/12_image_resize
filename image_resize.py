import argparse
import os.path
import sys
from PIL import Image


def is_valid_program_arguments(scale, width, height):
    if scale and (width or height):
        return '''Не могут быть одновременно указаны аргументы
        scale и width/height'''


def get_new_filepath(filepath, size):
    root, extension = os.path.splitext(filepath)
    return '%s__%dx%d%s' % (root, size[0], size[1], extension)


def get_new_size(path_to_original, new_scale, new_width, new_height):
    original_picture = Image.open(path_to_original)
    old_width = original_picture.size[0]
    old_height = original_picture.size[1]
    if new_scale:
        new_width = old_width * new_scale
        new_height = old_height * new_scale
    elif new_width and new_height:
        if new_width / new_height != old_width / old_height:
            print('''Введённые пропорции width/height не совпадают
            с пропорциями оригинального изображения''')
    elif new_width:
        new_height = new_width * old_height / old_width
    else:
        new_width = new_height * old_width / old_height
    return int(new_width), int(new_height)


def resize_image(path_to_original, path_to_result, new_size):
    original_picture = Image.open(path_to_original)
    result_picture = original_picture.resize(new_size)
    result_picture.save(path_to_result)
    status_message = '''Изображение с новыми размерами сохранено
    в файл с именем %s''' % path_to_result
    return status_message


def get_program_arguments():
    parser = argparse.ArgumentParser(prog='image_resize',
                                     description='''Скрипт, изменяющий размер
                                     картинки в соответствии с заданным
                                     масштабом''')
    parser.add_argument('image', help='путь к исходному изображению')
    parser.add_argument('--width', type=int, default=0,
                        help='новая ширина изображения')
    parser.add_argument('--height', type=int, default=0,
                        help='новая высота изображения')
    parser.add_argument('--scale', type=float, default=0.0,
                        help='коэффициент сжатия/растяжения изображения')
    parser.add_argument('--output', default='',
                        help='имя изменённого изображения')
    arguments = parser.parse_args()
    return (arguments.image, arguments.scale, arguments.width,
            arguments.height, arguments.output)


if __name__ == '__main__':
    path_to_original, new_scale, new_width, new_height, path_to_result = get_program_arguments()
    error = is_valid_program_arguments(new_scale, new_width, new_height)
    if error:
        print(error)
        sys.exit(0)
    new_size = get_new_size(path_to_original, new_scale, new_width, new_height)
    if not path_to_result:
        path_to_result = get_new_filepath(path_to_original, new_size)
    status_message = resize_image(path_to_original, path_to_result, new_size)
    print(status_message)
