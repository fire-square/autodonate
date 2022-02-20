from abc import abstractmethod, ABC
from autodonate.lib.utils.cron import register_function
from autodonate.lib.payment.api import register_payment_service
from autodonate.lib.payment.urls import urlpatterns as global_urlpatterns
from autodonate.lib.payment.currencies import Currency
from autodonate.models import PaymentProcess, Payment
from django.http.response import HttpResponse, Http404
from django.http.request import HttpRequest
from django.urls import path, include
from typing import Callable


class PaymentService(ABC):
    """Abstract class representing payment gateway (like Qiwi).

    Attributes:
        pinging: Should the model itself fetch updates from the payment service?
        ping_interval: Ping interval.
        logo_path: Path to payment service logo in staticfiles.
        name: Payment service name (like: "Qiwi").
    """

    pinging: bool = True
    ping_interval: int = 5
    logo_path: str | None = None
    name: str = ""
    currencies: tuple[Currency] = (Currency.RUB,)

    def __init__(self) -> None:
        """__init__() method. Register a new payment system."""
        register_payment_service(self)

        self.urlpatterns: list[path] = []
        global_urlpatterns.append(path(f"{self.name}/", include(self.urlpatterns)))

        self.callbacks: list[Callable[[], None]] = []

        if self.pinging:
            register_function(self.ping, self.ping_interval)
        else:
            self.urlpatterns.append(path(f"callback", self.callback_view))

        self.urlpatterns.append(path(f"generate_url", self.generate_response_intermediate))

    def ping(self) -> None:
        """Optional abstract method for pinging payment service and getting updates from them.

        Must call all self.callbacks functions passing item.
        """

    @abstractmethod
    def generate_response(self, process: PaymentProcess) -> HttpResponse:
        """Method for generating payment response, often just HttpResponseRedirect.

        Usually called when the user clicked on the button of the payment system.
        The function itself should take care of the subsequent identification of
        the user's payment, for example, add a random identifier to the payment
        comment and after recognize it in self.ping or self.callback_view
        """

    def generate_response_intermediate(self, request: HttpRequest):
        """View wrapper over generate_response to make it easier to get a PaymentProcess."""
        _id = request.GET.get("id")
        if not _id:
            raise Http404
        try:
            process = PaymentProcess.objects.get(id=_id)
            try:
                # Check existing linked Payment with PaymentProcess
                Payment.objects.get(process=process)
                raise Http404
            except Payment.DoesNotExist:
                return self.generate_response(process=process)
        except PaymentProcess.DoesNotExist:
            raise Http404

    def register_callback(self, function: Callable[[], None]) -> None:
        """Register function that be called on each payment.

        Args:
            function: Signature: def callback(payment: autodonate.lib.payment.Payment)
        """
        self.callbacks.append(function)

    def callback_view(self, request: HttpRequest) -> HttpResponse:
        """Optional abstract method. View for callback-like payment services."""
