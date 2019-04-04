from vng_api_common.filtersets import FilterSet

from brc.datamodel.models import Besluit


class BesluitFilter(FilterSet):
    class Meta:
        model = Besluit
        fields = (
            'identificatie',
            'verantwoordelijke_organisatie',
            'besluittype',
            'zaak',
        )
