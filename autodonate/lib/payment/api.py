"""API for retrieving all registered PaymentService.

Funcs:
    register_payment_service(): register new PaymentService

    get_services(): Get all PaymentServices"""
services: list[object] = []


def register_payment_service(service) -> None:
    services.append(service)


def get_services() -> list[object]:
    return services
