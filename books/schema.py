import graphene
from .queries import Query as BookQuery
from .mutations import CreateBookMutation, UpdateBookMutation, DeleteBookMutation

class Query(BookQuery, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    create_book = CreateBookMutation.Field()
    update_book = UpdateBookMutation.Field()
    delete_book = DeleteBookMutation.Field()
