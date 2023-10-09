# This is the response that we will return
from rest_framework.response import Response
# This is the serializer that we will use
from api.serializers import TicketSerializer, CommentSerializer
# This is the model that we will use
from .models import Tickets, Comment
#Error
from django.core.exceptions import ObjectDoesNotExist
#Status
from rest_framework import status


#Comments
def createComment(request, pk):
    try:
        ticket = Tickets.objects.get(id=pk)
    except Tickets.DoesNotExist:
        print(f"Ticket with ID {pk} does not exist.")  # Check the console for this message
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(ticket)
    data = request.data
    data['ticket'] = ticket.id  # Pass the ticket object to the serialized data
    serializer = CommentSerializer(data=data)  # Use the CommentSerializer to validate and create

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def getTicketComments(request, pk):
    try:
        ticket = Tickets.objects.get(id=pk)
    except Tickets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    comments = Comment.objects.filter(ticket=ticket)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def deleteComment(request, pk):
    try:
        comment = Comment.objects.get(id=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#Tickets

# This function will return the Tickets list
def getTicketsList(request):
    tickets = Tickets.objects.all().order_by('-timestamp')
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)

# This function will return the Ticket Detail
def getTicketDetail(request, pk):
    try:
        ticket = Tickets.objects.get(id=pk)
        serializer = TicketSerializer(ticket, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# This function will create a note
def createTicket(request):
    data = request.data
    ticket = Tickets.objects.create(
        name=data['name'],
        email=data['email'],
        description=data['description']
    )
    serializer = TicketSerializer(ticket, many=False)
    return Response(serializer.data)


# This function will update a note
def updateTicket(request, pk):
    try:
        ticket = Tickets.objects.get(id=pk)
    except Tickets.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = request.data
    serializer = TicketSerializer(instance=ticket, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# This function will delete a ticket
def deleteTicket(request, pk):
    ticket = Tickets.objects.get(id=pk)
    ticket.delete()
    return Response('Note was deleted!')