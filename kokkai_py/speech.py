from datetime import datetime, date

from typing import List, Dict, Optional


class SpeechRecord():
    def __init__(self, record: Dict):
        """[summary]

        Args:
            record (Dict): [description]
        """

        self._record = record

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

        self._init()

    def _init(self):
        """[summary]
        """
        # import pprint

        self.speaker = self._record["speaker"]
        self.speech = self._record["speech"]

        self.date = datetime.strptime(self._record["date"], '%Y-%m-%d').date()


class SpeechRecordList():
    def __init__(self, results: Dict):
        """[summary]

        Args:
            results (Dict): [description]

        Returns:
            [type]: [description]
        """

        self._results = results

        self.record_list: List[SpeechRecord] = []
        self.speech_list: List[str] = []

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

        speech_records = self._results["speechRecord"]

        # speech_record
        self.record_list = [
            self._create_speech_record(s) for s in speech_records
        ]
        # print(self.speech_list)

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
