from kokkai_py import Kokkai


def test_init():
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

    comment = "プログラミング"
    speaker = "あべしんぞう"
    kokkai = Kokkai()
    kokkai.speech(comment, speaker)
