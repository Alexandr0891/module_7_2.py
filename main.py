# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

def custom_write(file_name, strings):
    n = 0
    elem = {}
    for i in info:
        file = open(file_name, 'a', encoding='utf-8')  # файл в режиме записи
        tell = (file.tell())
        n += 1
        file.write(f'{i}\n')
        file.close()
        elem.update({(n, tell):i})
    return elem

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)