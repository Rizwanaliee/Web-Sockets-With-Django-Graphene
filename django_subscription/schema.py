import graphene
from rx import Observable
import random


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info, **kwargs):
        return "world"


class Subscription(graphene.ObjectType):

    count_seconds = graphene.Int(up_to=graphene.Int())
    say_somthing = graphene.String()

    def resolve_count_seconds(root, info, up_to=5):
        return (
            Observable.interval(1000)
            .map(lambda i: "{0}".format(i))
            .take_while(lambda i: int(i) <= up_to)
        )

    def resolve_say_somthing(root, info):
        return Observable.interval(1000).map(lambda i: f"Random data: {random.randint(1, 100)}")


schema = graphene.Schema(query=Query, subscription=Subscription)

