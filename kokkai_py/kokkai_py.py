"""Main module."""
from .base import KokkaiBase
from .speech import SpeechRecordList


from typing import Optional, List


class Kokkai(KokkaiBase):
    '''
    '''

    def __init__(self):
        self.speech_records: Optional[SpeechRecordList] = None

    def speech(self, comment: str, speaker: str) -> List[str]:

        params = {
            'any': comment,
            'speaker': speaker,
        }
        query = self.query(params)

        path = "speech" + query
        response = self.request(path)
        results = self.convert_to_dict(response)

        self.speech_records = SpeechRecordList(results)

        return self.speech_records.speech_list
