from autodonate.lib.payment.models import BasePaymentService
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from autodonate.models import PaymentProcess
from autodonate.lib.payment.currencies import Currency
from autodonate.models import Item, PaymentProcess
import pytest


class ExampleService(BasePaymentService):
    name = "example"

    def ping(self) -> None:
        pass

    def generate_response(self, process: PaymentProcess) -> HttpResponse:
        return HttpResponse(b"ok")

    def callback_view(self, request: HttpRequest) -> HttpResponse:
        pass


e = ExampleService()


def test_name():
    e.name = "example"


@pytest.mark.django_db(transaction=True)
def test_view(client):
    item = Item(currency=Currency.RUB.value, price=10)
    item.save()
    process = PaymentProcess(item=item, nickname="test")
    process.save()
    assert client.get(f"/api/payment/example/generate_url?id={process.id}").content == b"ok"
