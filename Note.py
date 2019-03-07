class Note:
    def __init__(self, title, text, category):
        self.__title = title
        self.__text = text
        self.__category = category

    def get_title(self):
        return self.__title

    def get_text(self):
        return self.__text

    def get_category(self):
        return self.__category
