import thai_national_id_smartcard


def test_sanity():
    assert 1 + 1 == 2


def test_add():
    assert thai_national_id_smartcard.add_numbers(1, 2) == 3
