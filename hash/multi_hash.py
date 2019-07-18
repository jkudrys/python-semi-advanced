from random import randint


class MultiHashSet:
    INIT_BUCKET = 4
    INCREASE_FACTOR = 2

    def __init__(self, payload_factor=0.75):
        self.buckets = [[] for i in range(self.INIT_BUCKET)]
        self.payload_factor = payload_factor
        self.length = 0

    def __str__(self):
        result = '{'
        for bucket in self.buckets:
            result += '[ '
            for element in bucket:
                result += str(element)
                result += ', '
            result += ']'
        # result = result[:-2]
        result += '}'
        return result

    def increase_number_of_buckets(self):
        new_buckets = [[] for i in range(self.INCREASE_FACTOR * len(self.buckets))]
        for bucket in self.buckets:
            for element in bucket:
                new_buckets_idx = hash(element) % len(new_buckets)
                new_buckets[new_buckets_idx].append(element)
        self.buckets = new_buckets

    def add(self, entry):
        # policzyc hash
        # wrzucić do odpowiedniego kubełka
        if self.length / len(self.buckets) > self.payload_factor:
            self.increase_number_of_buckets()

        idx = hash(entry) % len(self.buckets)
        self.buckets[idx].append(entry)
        self.length += 1

    def contains(self, element):
        # czy jest w kolekcji
        index = hash(element) % len(self.buckets)
        return element in self.buckets[index]

    def __contains__(self, item):
        return self.contains(item)

    def remove(self, element):
        index = hash(element) % len(self.buckets)
        self.buckets[index].remove(element)

    @property
    def len(self):
        count = 0
        for bucket in self.buckets:
            count += len(bucket)
        return count

    def add_from_list(self, lst):
        for item in lst:
            self.add(item)

    def clear(self):
        self.buckets = [[] for i in range(self.INIT_BUCKET)]


if __name__ == '__main__':

    def make_words(n):
        words = []
        letters = list('abcdefghijklmnopqrstuvwxyz')
        for number_of_words in range(n):
            word = ''
            word_len = randint(4, 7)
            for letter in range(word_len):
                word += letters[randint(0, len(letters) - 1)]
            print(word)
            words.append(word)
        return words


    mhs = MultiHashSet()
    mhs2 = MultiHashSet()

    words = make_words(13)
    words2 = make_words(7)

    mhs.add_from_list(words)
    mhs2.add_from_list((words2))

    print(mhs)
    print(mhs2)
    print(40 * '*')
    print(mhs.contains(words[3]))
    print(words[2] in mhs)

    mhs.remove(words[0])
    print(mhs)
    print(mhs.len)

    mhs.clear()
    print(mhs)
    print(mhs.len)
