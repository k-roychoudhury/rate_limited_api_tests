r""" backend.service module """


# importing standard modules ==================================================
from typing import List, Tuple, Dict, Any, Self
from random import randint


# class definitions ===========================================================
class RandomAttachmentGenerator:


    media_types: Tuple[str, ...] = tuple([
        "image/jpeg",
        "image/png",
        "image/tiff",
        "application/json",
        "application/xml",
    ])


    sample_filenames: Tuple[str, ...] = tuple([
        "orangutan",
        "elephant",
        "rhino",
        "dog",
        "hippopotamus",
        "alligator"
    ])


    def __sample_media_type__(self) -> str:
        return self.media_types[randint(0, len(self.media_types)-1)]


    def __sample_filename__(self) -> str:
        file_basename: str = "_".join((
            self.sample_filenames[randint(0, len(self.media_types)-1)],
            self.sample_filenames[randint(0, len(self.media_types)-1)]
        ))
        return file_basename

    
    def __construct_filename__(self, media_type: str) -> str:
        file_extension: str = media_type.rsplit("/", 1)[-1].strip()
        return ".".join((self.__sample_filename__(), file_extension))


    def __init__(self, num_items: int):
        self._items_to_generate: int = num_items
        self._counter: int = 0
        return


    def __iter__(self) -> Self:
        self._counter = 0   # making sure '_counter' is 0
        return self
    

    def __next__(self) -> Dict[str, Any]:
        if self._counter <= self._items_to_generate:
            random_media_type: str = self.__sample_media_type__()
            random_filename: str = self.__construct_filename__(
                random_media_type
            )
            next_result: Dict[str, Any] = {
                "media_type": random_media_type,
                "filename": random_filename
            }
            self._counter += 1
            return next_result
        
        else:
            raise StopIteration
    

    pass # end of RandomAttachmentGenerator


# method definitions ==========================================================
def get(ucid: str) -> Dict[str, Any]:
    r""" Method - Get
    - arguments:
        - `ucid`: a string
    - returns
        - a 'dict' object
            - to be used as the response content
    """
    attachments: List[Dict[str, Any]] = [
        _attachment_meta_data for _attachment_meta_data in \
            RandomAttachmentGenerator(randint(5, 10))
    ]
    response: Dict[str, Any] = {
        "ucid": ucid,
        "attachments": attachments,
        "items": len(attachments)
    }
    return response
