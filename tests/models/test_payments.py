import pytest

from autodonate.models import *


@pytest.mark.django_db(transaction=True)
def test_donation():
    i = Item(
        currency=0,
        price=99.9,
        rcon_command="test {nickname}",
        require_nick=True,
    )
    i.save()

    pp = PaymentProcess(item=i, nickname="cof ob,")
    pp.save()
    pp.cleanup_nickname()
    assert pp.nickname == "cofob"

    p = Payment(process=pp)
    p.save()
    assert p.format_rcon() == "test cofob"
