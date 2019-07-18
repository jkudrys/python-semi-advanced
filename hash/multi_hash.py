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

    def del_elem(self):
        pass

    def list_to_mhs(self):
        pass




if __name__ == '__main__':
    mhs = MultiHashSet()
    mhs.add('abc')
    mhs.add('bcd')
    mhs.add('cde')
    mhs.add('def')
    mhs.add('efg')
    mhs.add('fgh')
    mhs.add('ghi')
    mhs.add('ghi')

    #    mhs.add('a')
    print(mhs)

    print(mhs.contains('v'))
    print(mhs.__contains__('bcd'))
