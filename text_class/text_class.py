from decorators.color_print import color_print_method, color_print_class


@color_print_class('blue')
class Text:
    def __init__(self, path_to_file_with_text):
        self._path_to_file_with_text = path_to_file_with_text
        self._cursor = -1
        self.inited = False
        self._words = None
        # with open(self._path_to_file_with_text) as f:
        #     data = f.read()
        #     self._words = data.strip(',.').split()  # ? comma remains

    def print(self):
        pass

    def read_words(self):
        with open(self._path_to_file_with_text, 'r') as f:
            data = f.read()
            characters_to_remove = ",."
            for character in characters_to_remove:
                data = data.replace(character, '')
            self._words = data.split()
            self.inited = True

    def __iter__(self):
        return self

    # @color_print_method('magenta')
    def __next__(self):
        if not self.inited:
            self.read_words()
        if self._cursor + 1 >= len(self._words):
            raise StopIteration()
        self._cursor += 1
        return self._words[self._cursor]


class LazyText(Text):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cursor = 0

    def get_word(self):
        counter = -1
        yielded_word = None
        with open(self._path_to_file_with_text) as f:
            for line in f:
                for word_item in line.split():
                    counter += 1
                    # print(f'{counter=}')
                    # print(f'{self._cursor=}')
                    if counter == self._cursor:
                        yielded_word = word_item
                        yield yielded_word
                    else:
                        continue

    @color_print_method('BLUE')
    def __next__(self):
        try:
            result = next(self.get_word())
        except StopIteration:
            raise StopIteration()
        self._cursor += 1
        return result


if __name__ == '__main__':
    text = Text('text-sample.txt')
    for word in text:
        print(word)
    text_lazy = LazyText('text-sample.txt')
    for word in text_lazy:
        print(word)
    # expected_result = ['sample-text-2.txt', 'sample-text-3']
    print('\x1b[36msample-text-2txt\033[0m')
    # actual_result = [word for word in Text('sample-text-2.txt')]
    # assert actual_result == expected_result, f'{actual_result=} non equal {expected_result}'
    # gen = text.get_word()
    # print(next(gen))
    # text._cursor += 1

    # __next__(gen)

    color = 'magenta'
    print(color.upper())
    assert color.upper() == 'MAGENTA'
