from datetime import datetime, date
# from copy import copy

from typing import List, Dict, Optional


class SpeechRecord():
    def __init__(self, raw: Dict):
        """[summary]

        Args:
            raw (Dict): [description]
        """

        self._raw = raw

        # "speechID": "120115261X00520200303_105",
        self.speech_id: str = ""

        # "issueID": "120115261X00520200303",
        self.issue_id: str = ""

        # "imageKind": "会議録",
        self.image_king: str = ""

        # "searchObject": 105,
        self.search_object: int = 0

        # "session": 201,
        self.session: int = 0

        # "nameOfHouse": "参議院",
        self.name_of_house: str = ""

        # "nameOfMeeting": "予算委員会",
        self.name_of_meeting: str = ""

        # "issue": "第5号",
        self.issue: str = ""

        # "closing": null,
        self.closing: Optional[bool] = None

        # "speechOrder": 105,
        self.speech_order: int = 0

        # "speakerGroup": "自由民主党・無所属の会",
        self.speaker_group: str = ""

        # "speakerPosition": "内閣総理大臣",
        self.speaker_position: str = ""

        # "speakerRole": null,
        self.speaker_role: Optional[str] = None

        self.speaker: str = ""
        self.speaker_yomi: str = ""
        self.speech: str = ""
        self.date: Optional[date] = None

        # "startPage": 12,
        self.start_page: int = 0

        # "speechURL": "url_type"
        self.speech_url: str = ""

        # "meetingURL": "url_type",
        self.meeting_url = ""

        # "pdfURL": "url_type"
        self.pdf_url: str = ""

        self._json: Dict = {}

        self._init()
        self._set_to_json()

    def _init(self):
        """[summary]
        """

        self.speaker = self._raw["speaker"]
        self.speech = self._raw["speech"]

        self.date = datetime.strptime(self._raw["date"], '%Y-%m-%d').date()

        self.speech_id = self._raw["speechID"]
        self.issue_id = self._raw["issueID"]
        self.image_king = self._raw["imageKind"]
        self.search_object = self._raw["searchObject"]

        self.session = self._raw["session"]
        self.name_of_house = self._raw["nameOfHouse"]
        self.name_of_meeting = self._raw["nameOfMeeting"]

        self.issue = self._raw["issue"]
        self.closing = self._raw["closing"]
        self.speech_order = self._raw["speechOrder"]

        # 発言者所属会派
        self.speaker_group = self._raw["speakerGroup"]

        # 発言者の肩書き
        self.speaker_position = self._raw["speakerPosition"]

        # 発言者の役割
        self.speaker_role = self._raw["speakerRole"]

        self.start_page = self._raw["startPage"]
        self.speech_url = self._raw["speechURL"]
        self.meeting_url = self._raw["meetingURL"]
        self.pdf_url = self._raw["pdfURL"]

    def _set_to_json(self):
        keys = [
            k for k in vars(self).keys() if not (k[0] == "_")
        ]
        for k in keys:
            self._json[k] = vars(self)[k]

    def to_json(self):
        return self._json


class SpeechRecordList():

    def __init__(self, results: Dict):
        """

        Args:
            results (Dict): [description]

        Returns:
            [type]: [description]
        """

        self._results = results

        self.record_list: List[SpeechRecord] = []
        self.speech_list: List[str] = []

        self._caches_record_list: List[SpeechRecord] = []

        self.number_of_records = 0
        self.number_of_return = 0
        self.start_record = 0
        self.next_record_position = 0

        self._init()

    def _init(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        self.number_of_records = self._results["numberOfRecords"]
        self.number_of_return = self._results["numberOfReturn"]
        self.start_record = self._results["startRecord"]
        self.next_record_position = self._results["nextRecordPosition"]

        if self.number_of_return > 0:
            speech_records = self._results["speechRecord"]

            # speech_record
            self.record_list = [
                self._create_speech_record(s) for s in speech_records
            ]

            # print(self.speech_list)
            # self._caches_record_list = copy(self.record_list)

    def _create_speech_record(self, speech_record: Dict) -> SpeechRecord:
        """[summary]

        Args:
            speech_record (Dict): [description]

        Returns:
            SpeechRecord: [description]
        """
        speech_object = SpeechRecord(speech_record)
        self.speech_list.append(speech_object.speech)

        return speech_object

    def add_results(self, results: Dict):
        pass