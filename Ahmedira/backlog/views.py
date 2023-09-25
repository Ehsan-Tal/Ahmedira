from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    template = loader.get_template("backlog/index.html");
    context = {}
    project_URL = "Tal-Tal";
    board_cards = {
        "project_id":0,
        "board_id": 0,
        "board_name" :"",
        "cards": [],
        "extra_board_id": 0,
        "extra_board_name" :"",
        "extra_cards": []
        };
    
    cards = [];
    card = {};
    last_active_board = 0;

    board_cards["project_id"] = _find_project_id_by_URL(project_URL);
    board_cards["board_id"] = _find_backlog_by_project(board_cards["project_id"]);
    board_cards["board_name"] = "Backlog"

    # get backlog
    cards = _get_cards_JSON_by_board_id(board_cards["board_id"]);
    
    for card in cards:
        #card = { "id":0, "name":"" }
        board_cards["cards"].append(card);

    last_active_board = _get_last_active_board(board_cards["project_id"]);
    last_active_board = 2;

    if last_active_board:
        board_cards["extra_board_id"] = last_active_board;
        board_cards["extra_board_name"] = _get_board_name_by_board_id(board_cards["board_id"]);
        board_cards["extra_board_name"] = "Sprint 1";
        board_cards["extra_cards"] = _get_cards_JSON_by_board_id(board_cards["board_id"]);
    
    context = {
        "board_cards": board_cards
    }

    return HttpResponse(template.render(context, request));

def create_card_json(icon="", name="", code="", progress=""):
    return {"icon":icon,"name":name,"code":code,"progress":progress}

def collect_cards_from_board_id(request):
  
    # assume we can get the board_id
    
    board_id = int(request.GET.get("id"));

    card_json = _get_cards_JSON_by_board_id(board_id)

    return JsonResponse(card_json);


def create_card_into_board(request):

    board_id = int(request.GET.get("id"));
    card_code = _create_card_into_DB(board_id)
    card_json = create_card_json(code=card_code)
    
    return JsonResponse(card_json)

def update_card_into_board(request):

    board_id = int(request.GET.get("id"));
    code = request.GET.get("code");

    _update_card_into_DB(board_id, code)
    # return okay

    return JsonResponse()

def delete_card_into_board(request):

    board_id = int(request.GET.get("id"));
    code = request.GET.get("code");

    _delete_card_into_DB(board_id, code)
    # return okay ?

    return JsonResponse()


def collect_task_icons():
    return JsonResponse()

def collect_assignees_by_project(request):
    """
    assignee_pool = { "assignees": [
    {
        "id":"",
        "name": "",
        "img": ""
    }
    ]}
    where id is an immutable identifier of the record in the database
    where name is a mutable value
    where img is a the filename of the img - leaving the link to other items
    """
    assignee_pool = {}
    
    #project_id = int(request.GET.get("project_id"));
    #assignee_pool = MODEL method 

    assignee_pool = {"assignees": [
        {   
        "id":"1",
        "name": "Ehsan",
        "img": "ehsan.jpg"
    },
        {
        "id":"2",
        "name": "Ali",
        "img": "ali.jpg"
    },
        {
        "id":"3",
        "name": "Tal",
        "img": "tal.jpg"
    }
    ]}

    return JsonResponse(assignee_pool)








def _create_card_into_DB(board_id):
    card_code = "RT-1"
    return card_code

def _update_card_into_DB(board_id, code):
    return 

def _delete_card_into_DB(board_id, code):
    return 

def _find_project_id_by_URL(project_URL):
    print("NOTE:    PLACEHOLDER BOTH IN LOCATION AND IN FUNCTION");
    return 1


def _find_backlog_by_project(project_id):
    print("NOTE:    PLACEHOLDER BOTH IN LOCATION AND IN FUNCTION");
    return 1


def _get_board_name_by_board_id(board_id): 
    print("NOTE:    PLACEHOLDER BOTH IN LOCATION AND IN FUNCTION");
    return ""

def _get_cards_JSON_by_board_id(board_id):
    print("NOTE:    PLACEHOLDER BOTH IN LOCATION AND IN FUNCTION");

    card_json = {
                'cards':[
                {"icon":"🎃", "code":"RT-1", "name": "Code", "progress":"Todo"},
                 {"icon":"🎃", "code":"RT-2",  "name": "Feed", "progress":"Doing"}
                 ]
    }


    return card_json

def _get_last_active_board(project_id):
    print("NOTE:    PLACEHOLDER BOTH IN LOCATION AND IN FUNCTION");
    return 2
