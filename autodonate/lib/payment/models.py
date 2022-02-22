"""File for payment models."""

from abc import abstractmethod, ABC
from autodonate.lib.utils.cron import register_function
from autodonate.lib.payment.api import register_payment_service
from autodonate.lib.payment.urls import urlpatterns as global_urlpatterns
from autodonate.lib.payment.currencies import Currency
from autodonate.models import PaymentProcess, Payment
from django.http.response import HttpResponse, Http404
from django.http.request import HttpRequest
from django.urls import path, include
from typing import Callable, Optional, Tuple


class BasePaymentService(ABC):
    """Abstract class representing payment gateway.

    Attributes:
        logo_path: Path to payment service logo in staticfiles.
        name: Payment service name (like: "Qiwi").
    """

    logo_path: Optional[str]
    name: str = ""
    currencies: Tuple[Currency, ...]

    def __init__(self) -> None:
        """__init__() method. Register a new payment system."""
        register_payment_service(self)

        self.urlpatterns: list[path] = []
        global_urlpatterns.append(path(f"{self.name}/", include(self.urlpatterns)))

        self.callbacks: list[Callable[[], None]] = []
        self.urlpatterns.append(path(f"generate_url", self.generate_response_intermediate))

    @abstractmethod
    def generate_response(self, process: PaymentProcess) -> HttpResponse:
        """Method for generating payment response, often just HttpResponseRedirect.

        Usually called when the user clicked on the button of the payment system.

        The function itself should take care of the subsequent identification of
        the user's payment, for example, add a random identifier to the payment
        comment and after recognize it in self.ping or self.callback_view

        Args:
            process: PaymentProcess object.
        """

    def generate_response_intermediate(self, request: HttpRequest) -> HttpResponse:
        """View wrapper over generate_response to make it easier to get a PaymentProcess.

        Args:
            request: Default Django request object.

        Raises:
            Http404: When ID not valid or
              when there are existing link with PaymentProcess or
              when in PaymentProcess there are no object with id from request.GET.get("id").
        """
        id = request.GET.get("id")
        if not id:
            raise Http404("id not valid")
        try:
            process = PaymentProcess.objects.get(id=id)
            try:
                # Check existing linked Payment with PaymentProcess
                Payment.objects.get(process=process)
                raise Http404("PaymentProcess already linked with Payment")
            except Payment.DoesNotExist:
                return self.generate_response(process=process)
        except PaymentProcess.DoesNotExist:
            raise Http404("PaymentProcess with given id doesnt exist")

    def register_callback(self, function: Callable[[], None]) -> None:
        """Register function that be called on each payment.

        Args:
            function: Signature: def callback(payment: autodonate.lib.payment.Payment)
        """
        self.callbacks.append(function)


class FetchingPaymentService(BasePaymentService):
    """PaymentService self-fetching information from payment gateway.

    Attributes:
        ping_interval: Ping interval, aka timeout for auto-updates.
    """

    ping_interval: int

    def __init__(self):
        super().__init__()
        register_function(self.fetch, self.ping_interval)

    @abstractmethod
    def fetch(self) -> None:
        """Method for pinging payment service and getting updates from them.

        Must call all self.callbacks functions passing item.
        """


class WebhookPaymentService(BasePaymentService):
    """PaymentService receiving updates via webhook from payment service.

    Webhook url format: /api/payment/{service_name}/callback
    """

    def __init__(self):
        super().__init__()
        self.urlpatterns.append(path(f"callback", self.callback_view))

    @abstractmethod
    def callback_view(self, request: HttpRequest) -> HttpResponse:
        """View for callback-like payment services.

        Args:
            request: Default Django request object.
        """
