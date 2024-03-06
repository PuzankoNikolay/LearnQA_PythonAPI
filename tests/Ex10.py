class TestEx10:
    def test_phrase_len(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Длина фразы не короче 15 символов, а равна {len(phrase)}"
