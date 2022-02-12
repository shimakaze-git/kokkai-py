from kokkai_py import Kokkai


def test_init():
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

    # comment = "プログラミング"
    # speaker = "あべしんぞう"
    # kokkai = Kokkai()
    # speech_list = kokkai.speech(comment, speaker)

    comment = "ほげ"
    speaker = "あべしんぞう"
    kokkai = Kokkai()
    kokkai.speech(comment, speaker)

def test_comment():
    comment = "プログラミング"
    kokkai = Kokkai()
    speech_list = kokkai.speech(comment=comment)

    print("speech_list", len(speech_list))
    # print("number_of_records", kokkai.speech_records.number_of_records)

def test_speaker_group():
    comment = "ふげふげ"
    speaker = "あべしんぞう"
    kokkai = Kokkai()
    speech_list = kokkai.speech(comment=comment, speaker=speaker)

    print("speech_list", len(speech_list))
    print("number_of_records", kokkai.speech_records.number_of_records)
    kokkai.speech_speaker_group("自民党")

    comment = "プログラミング"
    kokkai = Kokkai()
    speech_list = kokkai.speech(comment=comment)

    print("speech_list", len(speech_list))
    print("number_of_records", kokkai.speech_records.number_of_records)
    speech_records = kokkai.speech_speaker_group("自由民主党")
    print("speech_records", speech_records)
