import graphene

from graphene_django import DjangoObjectType, DjangoListField
from .models import Country


class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        fields = "__all__"


class Query(graphene.ObjectType):
    all_country = graphene.List(CountryType)
    country = graphene.Field(CountryType, country_id=graphene.Int())

    def resolve_all_country(self, info, **kwargs):
        return Country.objects.all()

    def resolve_country(self, info, country_id):
        return Country.objects.get(pk=country_id)

schema = graphene.Schema(query=Query)