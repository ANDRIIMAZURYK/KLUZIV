from datetime import datetime


class Tag:
    def __init__(self, name):
        self.name = name


class JournalEntry:
    entries = []  # This list will store all journal entries
    next_id = 1  # ID for the next entry

    def __init__(self, text, date, category, tags=None):
        self.text = text
        self.date = date
        self.category = category
        self.tags = [Tag(tag) for tag in tags] if tags else []
        self.id = JournalEntry.next_id  # Assign a unique ID to each entry
        JournalEntry.next_id += 1

    def is_empty(self):
        return not self.text.strip()


class Journal:
    def __init__(self):
        self.entries = []
        self.categories = set()  # To keep track of unique categories

    def add_entry(self, entry):
        if entry.is_empty():
            print("Запис не може бути порожнім.")
            return False
        if entry.category in self.categories:
            print("Категорія вже існує. Виберіть іншу.")
            return False
        self.entries.append(entry)
        self.categories.add(entry.category)
        return True

    def edit_entry(self, entry_id, text=None, date=None, category=None, tags=None):
        for entry in self.entries:
            if entry.id == entry_id:
                if text:
                    entry.text = text
                if date:
                    entry.date = date
                if category:
                    entry.category = category
                if tags:
                    entry.tags = [Tag(tag) for tag in tags]
                print("Запис оновлено.")
                return True
        print("Запис з таким ID не знайдено.")
        return False

    def delete_entry(self, entry_id):
        for entry in self.entries:
            if entry.id == entry_id:
                self.entries.remove(entry)
                print("Запис видалено.")
                return True
        print("Запис з таким ID не знайдено.")
        return False

    def save_entries(self):
        # Placeholder for saving entries to a file or database
        print("Записи збережено.")

    def is_category_unique(self, category):
        return category not in self.categories


class User:
    def __init__(self, name):
        self.name = name
        self.journal = Journal()


def create_entry(journal):
    while True:
        text = input("Текст запису: ")
        if text.strip():
            break
        else:
            print("Запис не може бути порожнім. Спробуйте знову.")
    while True:
        date = input("Дата (формат: YYYY-MM-DD): ")
        if date.strip():
            try:
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Невірна дата. Спробуйте знову.")
        else:
            print("Дата не може бути порожньою. Спробуйте знову.")
    while True:
        category = input("Категорія: ")
        if category.strip():
            if journal.is_category_unique(category):
                break
            else:
                print("Категорія вже існує. Виберіть іншу.")
        else:
            print("Категорія не може бути порожньою. Спробуйте знову.")
    while True:
        tags = input("Теги (окремо, через пробіл): ").split()
        if tags:
            entry = JournalEntry(text, date, category, tags)
            if journal.add_entry(entry):
                print("Запис створено.")
                break
            else:
                print("Запис не може бути порожнім.")
        else:
            print("Теги не можуть бути порожніми. Спробуйте знову.")


def list_entries(journal):
    for entry in journal.entries:
        print(
            f"ID: {entry.id}, Дата: {entry.date}, Категорія: {entry.category}, Теги: {', '.join([tag.name for tag in entry.tags])}")


def main():
    user = User("User Name")  # Placeholder for user input

    while True:
        print("\n1. Створити запис")
        print("2. Редагувати запис")
        print("3. Видалити запис")
        print("4. Переглянути записи")
        print("5. Зберегти записи")
        print("6. Перевірити унікальність категорій")
        print("7. Вихід")
        choice = input("Виберіть дію: ")

        if choice == "1":
            create_entry(user.journal)
        elif choice == "2":
            list_entries(user.journal)
            entry_id = input("Введіть ID запису для редагування: ")
            text = input("Новий текст запису: ")
            date = input("Нова дата (формат: YYYY-MM-DD): ")
            category = input("Нова категорія: ")
            tags = input("Нові теги (окремо, через пробіл): ").split()
            user.journal.edit_entry(int(entry_id), text, date, category, tags)
        elif choice == "3":
            list_entries(user.journal)
            entry_id = input("Введіть ID запису для видалення: ")
            user.journal.delete_entry(int(entry_id))
        elif choice == "4":
            list_entries(user.journal)
        elif choice == "5":
            user.journal.save_entries()
        elif choice == "6":
            category = input("Введіть категорію для перевірки унікальності: ")
            if user.journal.is_category_unique(category):
                print("Категорія унікальна.")
            else:
                print("Категорія вже існує. Виберіть іншу.")
        elif choice == "7":
            print("До побачення!")
            break
        else:
            print("Невідома опція. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
