from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    @staticmethod
    def __add_object_if_not_exists(obj, collection: list, compare) ->list|None:
        if not any(compare(x, obj) for x in collection):
            collection.append(obj)

    def add_category(self, category: Category):
        self.__add_object_if_not_exists(category, self.categories, lambda x, y: x.id == y.id)

    def add_topic(self, topic: Topic):
        self.__add_object_if_not_exists(topic, self.topics, lambda x, y: x.id == y.id)

    def add_document(self, document: Document):
        self.__add_object_if_not_exists(document, self.documents, lambda x, y: x.id == y.id)


    @staticmethod
    def __find_by_id(id_value, collection: list) -> Topic|Document|Category|None:
        return next((c for c in collection if c.id == id_value), None)

    def edit_category(self, category_id: int, new_name: str):
        category = self.__find_by_id(category_id, self.categories)
        if category is not None:
            category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_by_id(topic_id, self.topics)
        if topic is not None:
            topic.edit(new_topic, new_storage_folder)


    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__find_by_id(document_id, self.documents)
        if document is not None:
            document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__find_by_id(category_id, self.categories)
        if category is not None:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__find_by_id(topic_id, self.topics)
        if topic is not None:
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__find_by_id(document_id, self.documents)
        if document is not None:
            self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__find_by_id(document_id, self.documents)
        if document is not None:
            return document.__repr__()

    def __repr__(self):
        return '\n'.join(d.__repr__() for d in self.documents)











