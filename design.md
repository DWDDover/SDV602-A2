<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 9.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>
<a href="#gdcalert8">alert8</a>
<a href="#gdcalert9">alert9</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>


SDV602

Declan Dover

Assessment 2

Data Explorer Application


[TOC]



# 
    Design and Storyboarding


## Introduction

This document is the design specification for my data explorer application (DEA). The application will be a data exploration tool with interactive data explorer screens (DES). The application exists to allow for collaboration and visualisations of multiple different data sets. 


## Purpose

The purpose of the application is to provide a collaborative space that allows multiple users to visualise data and send messages back and forth about different sets of data. While there is tools that exist that allow visualisation and analysis of data, the main problem to be solved by this application is that current tools only support a single user. This application will allow teams to collaborate on the same dataset and analyse and discuss the data in a group session.


## Scope

The application will include 2 modes, remote and local. The local mode will load data from the local disk and render each DES with adjustable chart options and text descriptions. Remote mode will include user logins and authentication, a session management screen, real time chat between users, and the uploading of data to a shared remote server. 

This project will use version controlled development with regular commits and a development log.


## Project Plan

After the requirements for the application are identified, screen designs will be created for the application. Storyboards will then be made based on these screen designs identifying how user requirements can be met through interaction with the UI. 

The structure of the code repository will then be created, identifying the different classes and modules that the application will require.

Implementation will then begin for the applications design, each feature of the application will be completed separately, starting with the local mode and followed by the remote mode, and connected to a main UI screen that allows users to use each of the different features. 

The application will be developed in a way that the main logic of the application is not attached to the UI in such a way that headless testing is impossible.

After the application is completed it will undergo testing in order to check if the non functional requirements are met.

A development log will be kept throughout the project with a slightly more detailed explanation of commit messages.


## Intended Audience

The intended audience of the application is any users that need to analyse or visualise datasets, particularly those working within teams that require collaboration. The application will have two types of users, local, and remote-mode. Local users will be working offline with their own locally saved data while remote users will be working and collaborating within shared sessions.

Users of the application are assumed to have some technical knowledge and to have used data analysis and visualisation tools before.


## Intended Usage

Local mode, viewing a graph:



* User opens the application
* User selects a locally stored data set to load
* User selects the axis labels and title for the data visualisation
* User adjusts different settings for the graph such as colors and orientation
* User closes the DES and selects a new dataset to load.

Remote mode, registering as a user



* User opens the application
* On the login screen, user selects the ‘register’ option
* On the registration screen the user enters a new username and password
* If requirements are met, the account is created and the user can now log in

Remote mode, creating a lobby



* User opens the application
* On the login screen, the user logs in using their existing account details
* On the main screen the user can see a list of active lobbies
* The user clicks ‘New DES’ and selects either public or private
* The user uploads a new dataset to the database and sets the chart settings
* Within the new DES the user can now send messages to the shared chat between members in that lobby


## Software Requirements


### Functional Requirements


#### Local mode

The system must allow the user to load .csv files from local disk

The system must allow the user to select labels for the x and y axis of the chart

The system must allow the user to select a title for the chart

The system must render a chart to the user based on the selected parameters

The system must allow the user to change the charts colors and orientation

The system must allow the user to load a new dataset without closing the application


#### Remote mode

The system must allow a user to view a list of active and available lobbies

The system must allow a user to create a new lobby and select whether it is public or private

The system must allow a user to join an existing session

The system must allow a user to upload data to the shared server

The system must allow the user to select which data to be used as the active data source for a DES

The system must update the DES for all users in a lobby when a new data source is selected


#### User login and authentication

The system must allow users to log in using stored details

The system must allow new users to register by selecting a username and password


#### Real time chat

The system must allow users within a lobby to send messages to that lobbies chat

The system must display the username of the messages sender as well as the messages content

The system must display the messages in order based on the time they were sent


### Non-Functional Requirements


#### Usability

The system must be usable for a first time user of the application

Each buttons functionality must be able to be inferred based on its text


#### Performance

The system shall display a DES within 3 seconds of selecting a dataset

The system shall update a DES within 2 seconds of changing a parameter or chart setting

Chat messages shall display for other users within 1.5 seconds of being sent


#### Reliability

The system must ensure that the application can run without errors or crashing


#### Maintainability

The code of the application must have descriptive comments to ensure maintainability

Headless testing must be possible to test features separately from UI interactions


#### Security

User passwords must be hashed before storage in the database

Login requests passwords must be hashed in order to compare to stored hashes


### System Requirements.

The application must be developed using python

Development shall be carried out in a python virtual environment

The application will use free simple GUI for the user interface

The application will use MatPlotLib for rendering each DES


## System Design


### Login/Register



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")



### Home - Local



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")



### Home - Remote



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")



### Lobby



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")



## Storyboards



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")




<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")




<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image7.png "image_tooltip")




<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image8.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image8.png "image_tooltip")




<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image9.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image9.png "image_tooltip")
