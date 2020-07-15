## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## ticket get all status path
* get_all_ticket
  - Email_form
  - form{"name": "Email_form"}
  - form{"name": null}
  - action_Get_all_status_Token

## ticket create request path
* create_ticket
  - Email_form
  - form{"name": "Email_form"}
  - form{"name": null}
  - action_Create_request_Token

## ticket getcase request path
* get_case_request_status
  - Email_form
  - form{"name": "Email_form"}
  - form{"name": null}
  - action_getcase_request_Token

## ticket create request path
* update_request_status
  - Email_form
  - form{"name": "Email_form"}
  - form{"name": null}
  - requestId_form
  - form{"name":"requestId_form"}
  - form{"name": null}
  - action_update_request_Token

## ticket close request path
* close_request_status
  - Email_form
  - form{"name": "Email_form"}
  - form{"name": null}
  - requestId_form
  - form{"name":"requestId_form"}
  - form{"name": null}
  - action_close_request_Token


## fro the testing process
* testing_process
  - utter_greet_sentence