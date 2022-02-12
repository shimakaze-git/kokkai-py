"""Main module."""
from .base import KokkaiBase
from .speech import SpeechRecordList
from .meeting import MeetingRecordList

from .utils import convert_group_name

from typing import Optional, List


class Kokkai(KokkaiBase):
    '''
    '''

    def __init__(self):
        self.speech_records: Optional[SpeechRecordList] = None
        self.meeting_records: Optional[MeetingRecordList] = None

    def speech(
        self, comment="", speaker="", start=1, maximum=100
    ) -> List[str]:

        params = {
            'any': comment,
            'speaker': speaker,
            'startRecord': start,
            'maximumRecords': maximum,
        }
        query = self.query(params)

        path = "speech" + query
        response = self.request(path)
        results = self.convert_to_dict(response)

        self.speech_records = SpeechRecordList(results)

        return self.speech_records.speech_list

    def meeting(self):
        params = {
            # 'any': comment,
            # 'speaker': speaker,
        }
        query = self.query(params)

        path = "speech" + query
        response = self.request(path)
        results = self.convert_to_dict(response)

        self.meeting_records = MeetingRecordList(results)

        return self.meeting_records.meeting_list

    def speech_speaker_group(self, speaker_group: str) -> Optional[List]:

        # 政党名を変換
        speaker_group = convert_group_name(speaker_group)

        if 0 >= len(self.speech_records.speech_list):
            print("speech_listには値が入っていません")
            return None

        # return []

        for i, r in enumerate(self.speech_records.record_list):
            if r.speaker_group is None:
                # print("None", None, r.speaker)
                if speaker_group is None:
                    print("None", r.speaker)
            else:
                if speaker_group in r.speaker_group:
                    self.speech_records._caches_record_list.append(r)

        return self.speech_records._caches_record_list
        # print("self.speech_records.speech_list", self.speech_records.record_list)
