from math import ceil


class PhotoAlbum:
    PAGE_SIZE = 4
    def __init__(self, pages: int):
        self.pages = pages
        self.photos:list[list[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count : int) -> object:
        pages = ceil(photos_count / cls.PAGE_SIZE)
        return cls(pages)

    def add_photo(self, label:str):
        for page, pictures in enumerate(self.photos):
            if len(pictures) < self.PAGE_SIZE:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(pictures)}"
        return f"No more free slots"

    def display(self):
        result = ""
        for page in self.photos:
            result += f"{'-' * 11}" + '\n'
            result += ' '.join("[]" for _ in page) + '\n'
        result += f"{'-'* 11}"
        return result




album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
