from rest_framework import viewsets, permissions

from .models import CreditOffersModel
from .serializers import CreditOffersSerializer
from .services.credit_calculator import calculate_credit_payment


class CreditOffersViewSet(viewsets.ModelViewSet):
    queryset = CreditOffersModel.objects.all()
    serializer_class = CreditOffersSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        credit_offers = CreditOffersModel.objects.all()
        price = self.request.query_params.get("price")
        deposit = self.request.query_params.get("deposit")
        term = self.request.query_params.get("term")
        order = self.request.query_params.get("order")
        if order:
            if order == "rate":
                credit_offers = credit_offers.order_by("rate_min")
            elif order == "-rate":
                credit_offers = credit_offers.order_by("-rate_min")

        if price and deposit and term:
            credit_offers = credit_offers \
                .filter(term_min__lte=term) \
                .filter(term_max__gte=term)
            for offer in credit_offers:
                offer.payment = calculate_credit_payment(price, deposit, term, offer.rate_min)
            return credit_offers
        return super().get_queryset()
