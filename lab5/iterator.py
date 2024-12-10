from csv import DictReader


class ImageIterator:

    def __init__(self, annotation_file: str):
        self.images = []
        with open(annotation_file, 'r') as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                self.images.append(row['Absolute_path'])
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.images)-1:
            raise StopIteration
        self.index += 1
        image_path = self.images[self.index]
        return image_path


    def __back__(self):
        if self.index <= 0:
            raise StopIteration
        self.index -= 1
        image_path = self.images[self.index]
        return image_path

    def get_current_element(self):
        if 0 <= self.index < len(self.images):
            return self.images[self.index]