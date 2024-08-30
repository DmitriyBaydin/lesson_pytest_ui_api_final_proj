import configparser


def test_conf():
    config = configparser.ConfigParser()
    config.sections()

    config.read('test_config.ini')  # Название файла с конфигурациями
    config.sections()
    sA = config["sectionA"]["prop"]  # Получаем значение переменной prop из секции

    print(sA)
