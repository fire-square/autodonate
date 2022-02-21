"""API for retrieving all registered PaymentService."""
services: list[object] = []


def register_payment_service(service: object) -> None:
    """Register new PaymentService.

    Args:
        service: Service which need be registered.
    """
    services.append(service)


def get_services() -> list[object]:
    """Get all PaymentServices.

    Returns:
        List with PaymentService objects.
    """
    return services
