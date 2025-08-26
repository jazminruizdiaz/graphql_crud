import graphene

class BookInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    description = graphene.String()