from rest_framework.decorators import api_view

from api.utils import createTicket, deleteTicket, getTicketDetail, getTicketsList, updateTicket, createComment, getTicketComments, deleteComment



# Comment
@api_view(['POST'])
def createNewCommentOnTicket(request,pk):
    return createComment(request,pk)

@api_view(['GET'])
def getCommentsTicket(request,pk):
    return getTicketComments(request,pk)

@api_view(['DELETE'])
def deleteCommentOnTicket(request, pk):
    return deleteComment(request,pk)

# Ticket

@api_view(['GET'])
def getTickets(request):
    return getTicketsList(request)

@api_view(['GET'])
def getTicket(request,pk):
    return getTicketDetail(request,pk)

@api_view(['POST'])
def createNewTicket(request):
    return createTicket(request)

@api_view(['PATCH'])
def updateStatusTicket(request,pk):
    return updateTicket(request,pk)

@api_view(['DELETE'])
def deleteThisTicket(request,pk):
    return deleteTicket(request,pk)