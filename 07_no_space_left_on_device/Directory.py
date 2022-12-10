from typing import Union

class RootDirectory:
    def __init__(self) -> None:
        self.__shallow_file_size = 0
        self.__deep_size = 0
        self.__is_deep_size_calculated = False
        self.contents = {}
        self.name = '/'

    def add_file(self, file_name: str, file_size: int) -> None:
        self.contents[file_name] = file_size
        self.__shallow_file_size += file_size
    
    def add_directory(self, directory_name: str) -> None:
        self.contents[directory_name] = Directory(parent_directory=self, directory_name=directory_name)
    
    def get_shallow_file_size(self) -> int:
        return self.__shallow_file_size
    
    def get_deep_file_size(self) -> int:
        if not self.__is_deep_size_calculated:
            self.__deep_size = self.__shallow_file_size
            for item in self.contents.values():
                if isinstance(item, Directory):
                    self.__deep_size += item.get_deep_file_size()
            self.__is_deep_size_calculated = True
        return self.__deep_size


class Directory(RootDirectory):
    def __init__(self, parent_directory: Union['Directory', RootDirectory], directory_name: str) -> None:
        super().__init__()
        self.parent = parent_directory
        self.name = directory_name