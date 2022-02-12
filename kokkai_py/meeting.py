from datetime import datetime, date

from typing import List, Dict, Optional


class MeetingRecord():
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

    def _set_to_json(self):
        keys = [
            k for k in vars(self).keys() if not (k[0] == "_")
        ]
        for k in keys:
            self._json[k] = vars(self)[k]

    def to_json(self):
        return self._json


class MeetingRecordList():
    def __init__(self, results: Dict):
        """[summary]

        Args:
            results (Dict): [description]

        Returns:
            [type]: [description]
        """

        self._results = results

        self.record_list: List[MeetingRecord] = []
        self.meeting_list: List[str] = []

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

        meeting_records = self._results["meetingRecord"]

        # meeting_records
        self.record_list = [
            self._create_meeting_record(m) for m in meeting_records
        ]
        # print(self.speech_list)

    def _create_meeting_record(self, meeting_record: Dict) -> MeetingRecord:
        """[summary]

        Args:
            speech_record (Dict): [description]

        Returns:
            MeetingRecord: [description]
        """

        meeting_object = MeetingRecord(meeting_record)
        # self.meeting_list.append(meeting_object.speech)

        return meeting_object
