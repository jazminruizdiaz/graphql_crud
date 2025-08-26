import graphene
from books.inputs import BookInput
from books.models import Book
from books.types import BookType


class CreateBookMutation(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, input):
        book = Book.objects.create(**input)
        return CreateBookMutation(book=book)

class UpdateBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = BookInput(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, id, input):
        book = Book.objects.filter(pk=id).first()
        if not book:
            return UpdateBookMutation(book=None)

        for field, value in input.items():
            setattr(book, field, value)
        book.save()
        return UpdateBookMutation(book=book)
    
class DeleteBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()

    def mutate(self, info, id):
        book = Book.objects.filter(pk=id).first()
        if not book:
            return DeleteBookMutation(message=None)     
        
        book.delete()
        return DeleteBookMutation(message="Book deleted successfully")


    