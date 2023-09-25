from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/collectCards/", views.collect_cards_from_board_id, name="read_cards_from_board"),
    path("api/createCard/", views.create_card_into_board, name="create_card_into_board"),
    path("api/updateCard/", views.update_card_into_board, name="update_card_into_board"),
    path("api/deleteCard/", views.delete_card_into_board, name="delete_card_into_board"),

    path("api/fetchAssigneePool/", views.collect_assignees_by_project, name="fetching_assignees_by_project_id"),
    path("api/fetchTaskIcons/", views.collect_task_icons, name="collecting_task_icons"),
]