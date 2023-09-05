from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient


@component
def Webapp():
 ## Creating state
    alltodo = use_state([])
    First_name, set_First_name = use_state("")
    Last_name,set_Last_name=use_state("")
    Username,set_Username=use_state("")
    Email,set_Email=use_state("")
    password, set_password = use_state("")
    Gender,set_Gender=use_state("Male")
    Age,set_Age=use_state("")


    def mysubmit(event):
        newtodo = {
        "First_name": First_name,"Last_name":Last_name,
        "Gender":Gender,"Age":Age,"Username":Username,
        "Email":Email,"password": password
        }

 # push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])
        login(newtodo)  # function call to login function using the submitted data


 # looping data from alltodo to show on web
    list = []
    def handle_event(event):
        print(event)
        
        
    return html.div(
      {"style": 
         {
        "padding": "30px",
        "background_image":"url(https://reactpy.neocities.org/1.jpg)", 
        "background-size":"cover",
        "min-height": "700px",
        "min-width":"700px"
}
           },
          html.img(
        {
        "src": "https://reactpy.neocities.org/photo/reactpy-logo-landscape.png",
         "class_name": "img-fluid",
         "style": {"width": "310px","height":"100px",
        "justify_content": "right"},
        "alt": "picture",}),
        html.br(),
        html.br(),

## creating form for submission
        html.form(
 # Heading
               {"on submit": mysubmit},
                html.b(html.h1(
                    {"style": {"font-family": "Time New Roman", "font-size": "36px","color":"PowderBlue"}}
                    ,"ReactPy")),
                    html.b(html.h2(
                    {"style": {"font-family": "Time New Roman", "font-size": "22px","color":"PowderBlue"}}
                    ,'Sign-Up')),

                html.label(
                    {"style": {"font-family": "Arial", "font-size": "14px","color":"LightCyan"}}
                    ,"First name"),
                html.br(),
                 html.input(
                    {
                        "type": "text",
                        "placeholder": "First name",
                        "on_change": lambda event: set_First_name(event["target"]["value"]),
                          "style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "font-color":"Azure",
                             "padding": "5px 5px",
                            "border": "2px solid gray",
                            "border-radius": "12px",
                            "margin": "5px auto",
                            "width": "25%",
                            "box-sizing": "border-box",
                            "outline": "none"}
                            }
                    ),
                html.br(),

                html.label(
                    {"style": {"font-family": "Arial", "font-size": "14px","color":"LightCyan"}}
                    ,"Last name"),
                html.br(),
                html.input(
                    {
                        "type": "text",
                        "placeholder": "Last name",
                        "on_change": lambda event: set_Last_name(event["target"]["value"]),
                         "style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "padding": "5px 5px",
                            "border": "2px solid gray",
                            "border-radius": "12px",
                            "margin": "5px auto",
                            "width": "25%",
                            "box-sizing": "border-box",
                            "color": "#555",
                            "outline": "none"}
                    }
                ),
                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial", "font-size": "14px","color":"LightCyan"}}
                    ,"Gender"),
                html.br(),
                html.select(
                    {  
                        "on_change": lambda event: set_Gender(event["target"]["value"]),
                        "style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "padding": "5px 5px",
                            "border": "2.5px solid gray",
                            "border-radius": "12px",
                            "margin": "5px auto",
                            "width": "25%",
                            "background":" linear-gradient(180deg,rgb(12, 39, 27),rgb(92, 138, 138))",
                            "text-shadow":"0 0 1px black",
                            "color":"LightCyan",
                            "outline": "none"}
                        

                    },
                    html.option(
                    {
                        "value":"Male",
                        "style":{
                             "font-family": "Time New Roman",
                             "font-size": "12px",
                             "padding": "5px 5px",
                            "border": "2px solid gray",
                            "border-radius": "12px",
                            "margin": "5px auto",
                            "width": "25%",
                            "box-sizing": "border-box",
                            "background-color": "#1a1a1a",
                            "color": "LightCyan",
                            "outline": "none"}
                    },"Male"),
                    html.option(
                    {
                        "value":"Female",
                        "style":{
                             "font-family": "Time New Roman",
                             "font-size": "12px",
                             "padding": "5px 5px",
                            "border": "2px solid gray",
                            "border-radius": "12px",
                            "margin": "5px auto",
                            "width": "25%",
                            "box-sizing": "border-box",
                            "background-color": "#1a1a1a",
                            "color": "LightCyan",
                            "outline": "none"}
                    },"Female")
                ),
                html.br(),
                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial", "font-size": "14px","color":"LightCyan"}}
                    ,f"Age {Age}"),
                html.br(),
                html.input(
                    { 
                    "type":"range",
                    "min":0,
                    "max":80,
                    "value":Age,
                    "on_change":lambda event: set_Age(event['target']['value']),
                    "style":{
                             "padding": "0px 0px",
                            "border": "4px solid white",
                            "border-radius": "12px",
                            "margin": "10px auto",
                            "width": "25%",
                            "box-sizing": "border-box",
                            "outline": "none"
                            }
                }

                ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial", "font-size": "14px","color":"LightCyan"}}
                    ,"Username"),
                html.br(),
                html.input(
                    {
                        "type": "text",
                        "placeholder": "Username",
                        "on_change": lambda event: set_Username(event["target"]["value"]),
                           "style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "padding": "5px 5px",
                            "border": "2px solid gray",
                            "border-radius": "12px",
                            "margin": "5px auto",
                            "width": "25%",
                            "box-sizing": "border-box",
                            "color": "#555",
                            "outline": "none"}
                    }
                    ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial", "font-size": "14px","color":"LightCyan"}}
                    ,"Email"),
                html.br(),
                html.input(
                    {
                        "type": "Email",
                        "placeholder": "Email",
                        "on_change": lambda event: set_Email(event["target"]["value"]),
                          "style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "padding": "5px 5px",
                            "border": "2px solid gray",
                            "border-radius": "12px",
                            "margin": "5px auto",
                            "width": "25%",
                            "box-sizing": "border-box",
                            "color": "#555",
                            "outline": "none"}
                    }
                ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial", "font-size": "14px","color":"LightCyan"}}
                    ,"Password"),
                html.br(),
                html.input(
                    {
                        "type": "Password",
                        "placeholder": "Password",
                        "on_change": lambda event: set_password(event["target"]["value"]),
                          "style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "padding": "5px 5px",
                            "border": "2px solid gray",
                            "border-radius": "12px",
                            "margin": "2px auto",
                            "width": "25%",
                            "box-sizing": "border-box",
                            "color": "#555",
                            "outline": "none"}
                    }
                ),
                
                html.br(),
                html.p(""),
 # creating buttons on form
                html.button(
                    {
                        "type": "Create an Account",
                        "on_click":event(lambda event:mysubmit(event)),
                          "style":{
                             "font-family": "Time New Roman",
                             "font-size": "18px",
                             "padding": "2px 2px",
                            "border": "2.5px solid gray",
                            "border-radius": "12px",
                            "margin": "2px auto",
                            "width": "15%",
                            "box-sizing": "border-box",
                            "color": "LightCyan",
                            "background":" linear-gradient(180deg,rgb(12, 39, 27),rgb(92, 138, 138))",
                            "text-shadow":"0 0 1px black",
                            "outline": "none"}
                    },
                    "Create an Account",
                ),
# add a button
                html.button(
    {
        "type": "Reset",
        "on_click":event(lambda event: set_First_name("") and set_Last_name("") and set_Email("") and set_password("") and  set_Username("")),
        "style": {
            "font-family": "Time New Roman",
            "font-size": "18px",
            "padding": "2px 2px",
            "border": "2.5px solid gray",
            "border-radius": "12px",
            "margin": "2px auto",
            "width": "15%",
            "box-sizing": "border-box",
            "color": "LightCyan",
            "background":" linear-gradient(180deg,rgb(12, 39, 27),rgb(92, 138, 138))",
            "text-shadow":"0 0 1px black",
            "outline": "none"}
    },
    "Reset",),
                ),
        html.ul(list),
      
    )


  




from pymongo import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI


app=FastAPI()

uri = "mongodb+srv://Reactpy:Sanjay123@cluster1.axdrpjp.mongodb.net/"
# Create a new client and connect to the server
client=MongoClient(uri, server_api=ServerApi("1"))
Database=client["reactpy"]
collection=Database["practice1"]
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



def login(
    login_data: dict):  
# removed async, since await makes code execution pause for the promise to resolve anyway. doesnt matter.
    First_name= login_data["First_name"]
    Last_name=login_data["Last_name"]
    Gender=login_data["Gender"]
    Age=login_data["Age"]
    Username=login_data["Username"]
    Email=login_data["Email"]
    password = login_data["password"]

    # categorizing the data in the NOsql database according to the importancy.
    Personal_Information={"First_name": First_name,"Last_name":Last_name,"Gender":Gender,"Age":Age}
    Login_Information={"Username":Username,"Email":Email,"password": password}
    # Create a document to insert into the collection
    document = {"Personal Information":Personal_Information,"Login Information":Login_Information}
    # logger.info('sample log message')
    print(document)

    # Insert the document into the collection
    data = collection.insert_one(document).inserted_id  # insert document
    print(data)

    return {"message": "Login successful"}

configure(app, Webapp)

