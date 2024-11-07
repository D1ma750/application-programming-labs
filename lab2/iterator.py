import csv


class ImageIterator:
    def __init__(self, file_with_annotation: str):
        self.images = []
        with open(file_with_annotation, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.images.append(row['Absolute path'])
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.images):
            image_path = self.images[self.index]
            self.index += 1
            return image_path
        else:
            raise StopIteration