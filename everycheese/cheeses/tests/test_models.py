import pytest
from ..models import Cheese

pytestmark = pytest.mark.django_db

def test__str__():
    cheese = Cheese.objects.create(
        name='Stracchino',
        description='Fromage mi-sucré qui se marie bien avec les amidons',
        firmess=Cheese.Firmess.SOFT 
    )
    assert cheese.__str__() == 'Stracchino'
    assert str(cheese) == 'Stracchino'