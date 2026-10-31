from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: list[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        alb_name = next((an for an in self.albums if an.name == album_name), None)
        if not alb_name:
            return f"Album {album_name} is not found."
        if alb_name.published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(alb_name)
        return f"Album {album_name} has been removed."

    def details(self):
        result = [f"Band {self.name}"]
        for album in self.albums:
            result.append(f"{album.details()}")
        return "\n".join(result)


