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

    def speech(self, comment="", speaker="", maximum=100, start=1, position=1) -> List[str]:
        # print("---" * 30)

        start_pos = start + (maximum * (position - 1))
        # print("start_pos", start_pos, start, position, maximum * (position - 1))

        speech_list = []

        params = {
            'any': comment,
            'speaker': speaker,
            'startRecord': start_pos,
            'maximumRecords': maximum,
        }
        if self.check_number_of_records(params):
            query = self.query(params)
            path = "speech" + query

            response = self.request(path)
            results = self.convert_to_dict(response)

            self.speech_records = SpeechRecordList(results)
            speech_list = self.speech_records.speech_list

        return speech_list

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

        for _, r in enumerate(self.speech_records.record_list):
            if r.speaker_group is None:
                # print("None", None, r.speaker)
                if speaker_group is None:
                    self.speech_records._caches_record_list.append(r)
            else:
                if speaker_group in r.speaker_group:
                    self.speech_records._caches_record_list.append(r)
        return self.speech_records._caches_record_list
