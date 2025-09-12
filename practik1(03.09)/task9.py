school = {'1а': 25, '1б': 28, '2а': 30, '2б': 27, '3а': 26}

def school_manager():
    while True:
        print("\n1 - Узнать количество учащихся")
        print("2 - Изменить количество учащихся")
        print("3 - Добавить новый класс")
        print("4 - Удалить класс")
        print("5 - Показать все классы")
        print("0 - Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            class_name = input("Введите класс: ")
            print(f"Учащихся в {class_name}: {school.get(class_name, 'Класс не найден')}")
        
        elif choice == '2':
            class_name, count = input("Введите класс и новое количество (например: 1а 30): ").split()
            if class_name in school:
                school[class_name] = int(count)
                print(f"Обновлено: {class_name} - {count} учащихся")
            else:
                print("Класс не найден")
        
        elif choice == '3':
            class_name, count = input("Введите новый класс и количество (например: 4а 28): ").split()
            school[class_name] = int(count)
            print(f"Добавлен класс {class_name} с {count} учащимися")
        
        elif choice == '4':
            class_name = input("Введите класс для удаления: ")
            if class_name in school:
                del school[class_name]
                print(f"Класс {class_name} удален")
            else:
                print("Класс не найден")
        
        elif choice == '5':
            print("\nКлассы и количество учащихся:")
            for cls, count in school.items():
                print(f"{cls}: {count} человек")
        
        elif choice == '0':
            break

school_manager()