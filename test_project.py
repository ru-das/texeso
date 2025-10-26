import pytest
from project import create_matrix, is_match, is_game_end
from components.card import Card


# To test create_matrix()
def test_create_matrix() -> None:
    matrix1 = create_matrix(3,4)
    assert isinstance(matrix1, list)
    assert len(matrix1) == 3
    for row in matrix1:
        assert isinstance(row, list)
        assert len(row) == 4
        for col in row:
            assert isinstance(col, int)

    with pytest.raises(ValueError):
        matrix2 = create_matrix(3,3)


# To test is_match()
def test_is_match() -> None:
    card1 = Card(1, 1, 1, 4)
    card2 = Card(1, 3, 4, 4)
    card3 = Card(2, 2, 2, 4)

    assert is_match(card1, card2) == True
    assert is_match(card1, card3) == False
    assert is_match(card1, card1) == False


# To test is_game_end()
def test_is_game_end() -> None:
    assert is_game_end(total_matches=7, max_matches=8) == False
    assert is_game_end(total_matches=6, max_matches=6) == True

    with pytest.raises(ValueError):
        is_game_end(total_matches=10, max_matches=8)