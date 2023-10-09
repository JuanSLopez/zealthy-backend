
from django.urls import path
from .views import createNewTicket, deleteThisTicket, getTickets,getTicket, updateStatusTicket, createNewCommentOnTicket, getCommentsTicket, deleteCommentOnTicket

urlpatterns = [
    path('tickets/',getTickets,name='ticket-list'),
    path('tickets/<uuid:pk>/',getTicket,name='ticket-detail'),
    path('tickets/create/',createNewTicket,name='ticket-create'),
    path('tickets/update/status/<uuid:pk>/',updateStatusTicket,name='ticket-status-update'),
    path('tickets/delete/<uuid:pk>/',deleteThisTicket,name='ticket-delete'),
    path('comment/create/<uuid:pk>/',createNewCommentOnTicket,name='create-ticket-comment'),
    path('comment/get/<uuid:pk>/',getCommentsTicket,name='get-ticket-comments'),
    path('comment/delete/<int:pk>/',deleteCommentOnTicket,name='delete-ticket-comment'),
]
