from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:
    def __init__(self, file_size: int, message: str=None) ->None:
        self.file_size = file_size
        self.message = message
        
    @property
    def message(self):
        return self.__massage

    @message.setter
    def message(self, value):
        if not value:
            self.__massage = f"File must be less than {self.file_size}MB!"
        else:
            self.__massage = value

    def __call__(self, value:UploadedFile):
        if value.size > self.file_size * 1024 * 1024:
            raise ValidationError(self.message)