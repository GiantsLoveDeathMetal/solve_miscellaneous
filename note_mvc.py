import pickle


def fuzzy_match(title, iterable):
    print("Yup, not found! Try:")
    print(iterable)


def load_meta():
    with open('note_data.pkl', 'rb') as _input:
        return pickle.load(_input)


class Model:

    def __iter__(self):
        raise NotImplementedError

    def get(self, item):
        """Returns an object with a .items() call method
        that iterates over key, value pairs of its information."""
        raise NotImplementedError

    @property
    def item_type(self):
        raise NotImplementedError

# 1.)
# The order is part of the model, so it should go there.
# A raw pull of "all data" would return the data in the
# sorted order, and there is no interface to choose the
# sort order.

def tui_object(x, y, z):
    return zip(x, y, z)


class NotesModel(Model):
    notes = load_meta()

    def get(self, title):
        try:
            return self.notes[title]
        except KeyError as e:
            fuzzy_match(title, self.notes.keys())

    def get_info(self, iterable):
        return [self.notes[item]['description']
                for item in iterable]

    def get_subinfo(self, iterable):
        return [self.notes[item]['sub_headings']
                if 'sub_headings' in self.notes[item] else None
                for item in iterable]

    def items(self):
        return self.notes.keys()

    def sort_items(self):
        iterable = self.notes
        sort = sorted(iterable, key=lambda x: x[0].lower())
        return tui_object(sort, self.get_info(sort), self.get_subinfo(sort))

    def get_views(self, title):
        return self.get(title)['views']


if __name__ == '__main__':
    note_model = NotesModel()
    print(note_model.get_views('drops'))
