import pytest

from notes import Note


class TestNotes:
    def test_equality(self):
        assert Note(20, 'PLN') == Note(20, 'PLN')

    def test_inequality(self):
        assert Note(20, 'PLN') != Note(20, '$')
        assert Note(10, '$') != Note(20, '$')

    def test_clone(self):
        note: Note = Note(20, 'PLN')
        assert note == note.clone()

    def test_less_than(self):
        assert Note(1, 'PLN') < Note(2, 'PLN')
        assert not Note(3, 'PLN') < Note(2, 'PLN')

    def test_greater_or_equal(self):
        assert Note(15, 'PLN') >= Note(15, 'PLN')
        assert not Note(15, 'PLN') >= Note(16, 'PLN')

    def test_illegal_comparison(self):
        with pytest.raises(ValueError):
            assert Note(1, 'PLN') < Note(2, '$')

    def test_sorting(self):
        assert (
            sorted([Note(7, 'PLN'), Note(1, 'PLN'), Note(20, 'PLN')])
            ==
            [Note(1, 'PLN'), Note(7, 'PLN'), Note(20, 'PLN')]
        )
