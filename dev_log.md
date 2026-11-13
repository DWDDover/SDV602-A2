# Development log for SDV602 Assessment 2

Initial project work involved setting up the repository and file layout for the application.

I decided to keep modules that are used in both modes within the data_explorer folder, which contains a sub folder for the local and remote modes. Modules used only by these modes will be kept within the relevant folder.

I started by taking code excerpts and modules form the in class sessions that are reusable and refactoring them for the application.

The login window was the first, I updated the layout to more represent my designs and added a third button to start in local mode. The login window imports both a local_run and remote_run function from their relevant modules. This seperation will allow me to work on each mode seperately as they will both have different requirements and functionality.

The current login window and app are set up to just login and launch the chat app so i seperated the functions and removed the chat app parts. The chat app will be refactored and used later as part of the remote modes DES lobby. I also updated the config file to point to a new database that will store users, chat messages, and data sources. The register button could be kept as is as I already gave it functionality to create user accounts, the same is true for the login button, which on a successful login will pass a user object to  the remote_run method to keep track of the user that is logged in.

I was finding it difficult to start the project cleanly and decide what to take from class sessions. Below is a structure i will use that separates classes and lists them out, as well as labelling each one as model, view, or controller as part of the MVC architecture

## classes

### View

LoginView - The login GUI for remote mode
RegisterView - The registration GUI for remote mode
LocalView - The main GUI for local mode
RemoteView - The main GUI for remote mode
DESView - The DES window for a local session
LobbyView - The DES window for a remote lobby

### Model

FileManager - Reads data from a file
DatabaseManager - Performs database operations
DataSource - Holds the data read from a file
User - Holds user information
Message - Holds message information
DESSession - Holds session information for a DES
ChatRoom - Holds session information for a remote lobby chat room

### Controller

app - Parses the command line arguments and starts the relevant mode
test_app - App for testing, runs through the functionality of the app
DataVisualiser - Maps the data to a chart
local_app - The local app
remote_app - The remote app

## Data

The original app.py always loaded the login screen and local mode was launched through a button there, to completemly decouple the modes
the local, remote, and testing modes now launch through argparse. This means that local mode can be launched when no database exists as the previous login screen imported and depended on pymongo.

## DataSource

The first class i made is datasource. I started by making a constructor that takes the name of the data source and its data, the constructor has handlers to replace empty data with and empty list. I looked into the unittesting module and made a test class for the datasource class which tests the columns method with real data, empty data, none data, a compltely empty constructor. and a test to ensure that two data sources do not have a shared state. The way i originally made the class meant that each instance would always reference the same empty list as a default value when no data was given. to fix this the new empty list is made within the constructor rather than in the default values for the method parameter.

Next i gave it an is_empty method to check whether a data source has any rows, this will be used within other methods as a helper. I also gave it a method to check if two data sources are compatible that will be used before appending some data to other data. This method jsut checks that either one or both sources are empty or that the column names are an exact match. Im unsure if thjis will need to be changed later if potentially i need to append data with the same base columns and also some new columns, or if the same colums exist but in another order. Tests were added to test these two new methods.

In data source i decided to add the append method here rather than in file manager because data source is responsible for the data when it is in memory. this means file manager will be responsible for the saving and loading of the files but not manipulating the actual data. The append method will first check compatibility and return an exception is that check fails. this will be used later in a GUI dialogue popup. As with the other methods I added tests to the test class for each case and continued running them as i go. This method completes datasource fucntionailiy for what is needed in local mode.

## FileManager

To continue with the pattern of making tests as I go i created 5 different .csv files to test different behaviour, a vlid csv file, an empty file, duplicate headers, extra fields, missing fields, an invalid file, and a file with only headers. The current file_manager starter code prints errors to the console but this will be chanegd to return exception that can be displayed in GUI popups. The append_file method was removed as this is handled by DataSource now. As I am writing the local mode functionality first the methods write_file, read_file, and print_file are unnecessary and are also removed. With just read_file left i wrote out the unit tests to check behaviour on each of the types of files ensuring they are all handled correclty.

At this point i decided to create an exceptions module to handle the exceptions in the code so far. This module contains classes that inherit from exception to handle unique cases within the application. The module is currently imported into DataSource and FileManager and handles empty CSV files, invalid file paths, and incompatible data for appending.

## DataVisualiser

The skeleton of data visualiser from the starter code contains unnecessary methods that can be found in other classes now, i started by removing these methods, load_data, append_data, load_data_source, and _load_csv. plot_line_chart will be seperated so that the actual display happens in the DES view class to be made later and this class jsut prepares the data to be visualised. This decoupling was done to adhere to the MVC architecture and enable further testing that doesnt require a GUI. I decided to make a chart data class that can be returned by this method and passed into the actual chart view that contains everything matplotlib needs to draw the chart. plot_line_chart is now called create_chart_data. the chart data class holds the title of the chart, the two axis labels, and a dictionary of the series of the chart, with a series name and a pair of lists, x and y values, for each series.

At this point I reanranged the structure to include a folder for each of view, model, and controller and moved the relevant files into each one. I also moved the test files into a testing folder and created scripts for running each one in order to save time typing out the file paths into the terminal each time.

Fully rearranged the structure of the project at this point, now 5 folders, testing, model, view, controller, and data. data folder will hold classes that access the data sucha s database_manager and the new message_repository and user_repository classes. file_manager was also moved here as it provides a similar function by accessing local files.

## User

simple user class in the model folder, holds a user_id and a username, as well as dundermethod for defining its string representation, mostly for debugging.

## User repository

Made a user repository class responsible for accessing the users collection. This class contains the login and save methods that used to belong to user, now called login and register. This class also creates an instance of database manager in its constructor so it can use its save and find by id methods. Progress is much faster at this point as I have decided to forego making unit tests alongside development, as well as the work from my original attempt being more usable.

## Login view

At this point I wanted to start making the login controller that will access the user repository. I decided to make the login_view first as the buttons and fields on the form will determine the event readers in the controller. This only required some minor adjustments to the login_view I had previously created.

It seems like the best way to go forward would be to create all the views first as close as possible to the ones im my designs, FreeSimpleGUI does not make this easy but I will at least ensure they have all the buttons and fields from my designs. Making the views first will also allow me to easily see all the events I need handlers for in the various controllers.

The login view also has a button that opens the register window, the logic behind this window also lives in the LoginController class, This logic needed to be updated slightly to add some input validation, for now it will only check that all fields are filled out and that the password matches the repeat password. This is the login part of the application finished for now, it will only exist when launching the remote app. I decided to do this part first as it was the closest to being what I had already made in class sessions.

A small problem I had with the login controller logic holding the logic for the register view too was forgetting to have the register happen within a run loop. I just had the buttons as if statements within the "register" event so if creating a user failed the first time, e.g. 'username in use' the form would then become unusable. To fix this I added a similar loop to the logins 'while user is None' that uses instead 'while new_user is none" this ensure the window keeps reading inputs until its closed or a user is successfuly created.

## Local view, Local controller

While making the local view I realised that it would make sense to make the view and the controller alongside each other. My local view was kept the same as the design, just asking the user to select a file, the x and y axis labels, and the series key. I used an event on file selection to update the series key dropdown with the column list from the chosen file. This was done by creating a DataSource object upon file selection and using its columns() method I had made previously.

An issue I encountered here during testing was selecting a non numeric x axis to pass into the data visualiser. I created a new exception to handle this error that could be passed up to the local window and display the error to the user. This error will be caught when creating chart data and returns the non numeric value. While doing this i also wrapped the other parts of local_controller in their own try excepts, such as for when the file cant be read as a csv, or no selection was made in one of the dropwdowns. I also added new exceptions in data visualiser to check that the x key, y key, and series key are all actually columns in the given data.

## Local DES view, DES controller

Previously I was passing a local des view into des controller from local controller and passing that view the chart data I had created, I realised this wouldnt work for headless testing as I couldnt create that view without making a window. In order to fix this and also ensure DES controllers run method works with either a local or remote DES view the des controller is now passed both the chart data and a factory contsructor for the type of view. The run method then creates the window based on the type of view its given and the chart data, this also means that the same run method in DES controller will work with both local and remote views using an if statement.

In order to append new data, the local controller now passes both the chart data, and the datasource used to make it. Because of this the DES controller can use the append method to append a new CSV file and then use the data visualiser to replace its chart data with that of the appended file. I decided to pass in both instead of just the data source so that the local controller can catch any errors in the users inputted attributes before making the DES window. I also changed data source to hold a chart title that will be used within the DES window.

I used a canvas in the window in order to draw the chart, and the defualt matplotlib toolbar. An issue I'm having is the x axis values being sorted alphabetically on the chart, meaning each age is sorted seperately and not in order.

I decided this is not actually an issue and its fine to plot the data this way. I moved the updating of the dropdown list values into a method within local DES view that the controller calls rather than having the controller manipulate the window diretctly. This means that headless testing will work better for this controller.

I decided to reverse the change made earlier which had a single DES controller for the local and remote modes. there is now a local DES controller and a remote DES controler. This is because the remote controller will need extra values passed into it in order to work.

This completes the local mode of the application

## Remote mode

To start the remote mode i made the two missing models, session and chat message. session will hold the session name, user id of the host, a session id, and a list of the user ids of the users currently in the session. Message will hold a user id of the writer, the session ID of the session it weas written in, and the message content. The remote mode will use a repository module type as part of the MVC, the repositories will be as follows

data_source_repository
message_repository
session_repository
user_repository


The user repository consists of a class containing two methods, login and register. These methods were taken from the previously existing user model to seperate responsibility. Repository modules will import the database manager class and will be responsible for all database operations.

These repositories will correspond to four collections in the database, 

users
    - user_id
    - name
    - password
messages
    - session_id
    - creator_id
    - content
    - timestamp
sessions
    - host_id
    - users
    - data_source_id
    - public
    - timestamp
data_sources
    - data_source_id
    - user_id
    - data
    - title

I started with the session model and repository. I used the fields name, host_id, private, users, data_source_id=None, and session_id in the constructor. I decided to use a data_source_id as reference to the other collection to prevent storing large data files in the session collection that are repeated in the data_source collection. The session repository will follow the pattern of the users repository but with quite a few more methods. The first was create_session that creates a new session object by taking the attributes as parameters, creates a new document using the sessions attributes, and returns the session object. Returning the session object will prevent an extra step later where a user makes a session, a session window opens, and all the session info has to be retrieved from the database. The session repostory has a get session by id that uses the database managers get one by id and then creates a session object. I realised at this point that all the methods were going to repeat the code where the values from the document were passed into a constructor to create a new session object so I created a helper function that takes the document as session_data and returns a session object. This will be used in any method that is retrieving a session from the database.

Also at this point I added a delete_one_by_id and update_one_by_id to database manager as these were not made previosly and not required by the user repository.

I decide to go back and remove the user list from the session model as it won't be used anywhere else and creates some issues with saving and updating session data. I also misunderstood private in terms of a remote session. I will make it so private sessions only have the host in them. I couldn't work out how to have the session removed from the database upon the process for that session terminating. 

I changed chat messages model to include a username instead of a user ID. This is because the only purpose of the user ID was to find the username to display later in the remote des window. I also added a delete session messages later that will be used alongside deleleting a session in the remote des controller. This uses pymongos delete_many function. I also added a message ID in order to make the polling more efficient as pymognos ID system increases the IDs over time. Using this i will sort the message list returned by each message_id. To fix the polling i added an extra parameter to get messages by session for the last_message_id, this also required using mongos $gt operator as a second query on the find to only return greater IDs. This also reqwuired importing bson into the message repository to convert the string 'last_message_id" back into and object ID for comparison.

The final data module to make is data source repository, as well as some chanegs to the DataSource class

An issue encountered immediately is that the current datasource object does not have a name attribute. This will be required when uses are selecting from their uploaded datasource so this extra paramater was added to the constructor with a default =None as the local mode will not use it. The data source collection will include a user ID but it wont be present in thje data source object, this is becuase local mode does not require it and the only time it will be used is to show a user a list of their own uplodaded sources to pick from. This list also requires that the DataSource object also has an optional ID parameter so that the list picker has something the controller can find the correct source from. This method returns DataSource objects with no data so the picker can display the name and the controller can retrieve the datasource_id. The changes made to the datasource constructor will not affect the finished local mode as they have defualt attributes.

This finishes the data modules for remote mode

## Remote View - Main form

The remote view main form has three areas, the join session list, which doubles as the manage sessions allowing hosts to delte their own sessions, the create session frame, where the user can choose a name, and whether the session is private, and create a session. It also has an upload data source area, in which users can select a file on their local machine and upload it to the database with a new name.

## Remote controller

The remote controller needs to wire up the componenets of the remote view with different behaviiours for each event. These will be:

Create - make a new session object and add it to the database, while also opening the window for that session for the user that created it

Delete - delete the session that is selected if it is hosted by the current user

Join - open the window for the selected session

Refresh - repopulate the session list with current sessions

Logout - return the user to the login screen

Upload CSV - upload the selected CSV to the database with the name given by the user

Starting with the bones of the local controller, the remote controller needs to fucntion slightly differently when opening a DES window in a new process. The process needs to know the current user and the current session when it is opened. After refactoring my local controller I realised it reads values directly from the window for its event which will not allow for headless testing. I will now go back and refactor the controller to have a method for each event that is either called through GUI interaction, in which case its paramaters come from window values, or can be called with values i give them in headless testing.

## Decoupling refactor

The first refactor is to pass the file manager and local_view into the initial creation of the local controller in local_app.py. This means when a local controller is created later in testing a real local view does not have to be creaetd in order to run local_cojntroller. the local controllers constructor now takes these two objects rather than creating them itself.

The next part of the refactor is to split each event read logic into a function that can be decoupled from the UI and called outside of a window event for testing. The data_source is now also a parameter in local controllers _init_. This wont affect functionalility but means headless mode can pass in a data source manually. A new method called file chosen was created in local controller, this handles updating the sotred data source for the main local window. As it currently exists the controller reaches into the local view to update the columns for the dropdowns, thjis method will be moved into the local view. The generate DES event still reads values directly from the window so will be decoupled in a similar way.

The local controller now has a method to generate the chart data and to start a new DES process. The actual generate DES event is now the only place the window is read as this logic can only be called through interacting with the GUI. The two new processes can be called in headless testing without a GUI window.

LocalDESController now needs similar refactoring, each event behaviour will be replaced with a method that takes the values that are read from the window, allowing each method to be called in the headless testing. The append, replace, and generate new DES logic was moved into three new methods which take the values they need. The actual events that call the new methods read the values from the window, meaning in my tests these methods can be tested without reliance on the GUI

With these refactors in mind the remote mode equivalents of the controllers will be created with decoupling from the start.

## Remote Controller

I started by making the methods that the window events will use, these are:

create_session - adds the users new session to the database with the name they wrote, opens the DES controller for that new session
join_session - takes the session ID from the session selected in the list and retrieves that session and passes it into a new DES controller
logout - returns the user to the login screen and closes all their open DES windows, also deletes all that users sessions from the database. (Need to work out what happens to other users in these sessions)
delete_session - deletes the selected session from the list, popup denying permission if the user does not own that session. (need to work out as above what happens to users in the session)
upload_data - Uploads the selected file to the database with the users id to identify it as their file

Each method is used inside the run loops relevant event, which takes values from the window to pass into the method, this ensures the methods can be ran with defined values in the headless testing.

I also added a refresh sessions method to the view which takes the sesison list as an argument and a refresh sessions methjod to the controller that passes in the sessions and calls this method. The logout mehotd had to be changed to import the login controller within the function after closing the remote window to prevent a circular import.

An issue now preventing progress is that the sessions in the list are strings and need a way to target the actual sessions the represent. 

The issue turned out to be that reading a list boxes values returned a list of selected values instead of the single session. To fix this i targeted only the first session in the list of selected sessions. 

To address the session closing issue the remoteDEScontroller has a timeout of 2 seconds that checks if its own session is still in the database, if its not the users will be notified and the session closed. This same polling will check for changes to the session made by the host, such as replacing or appending the data

## Remote Des Controller/View

The remote DES view uses the template of the local DES view with some changes. The chat window is added on the right, the chart title is replaced with the session name, the upload and replace sections now use a dropdown of data sources the user has uploaded, and a section to upload new data was added. The session window has a 2 second poll rate that will be used to show any changes made, such as new data, appended data, or new chat messages.

Another issue and workaround I had was updating the sessions current datasource. I was trying the retrieve the data from the combobox but relaised i set it eralier so that the list of a users data sources generated only held hte name and ID. I used this to make the method jsut update the data source for the session in the session collection. The ID is then used again to update the actual data for the session. The windows polling will update this for all users in the session too.

A concession I will make with the data is that each user will set their own x-key, y-key, and series key rather than these being defined session wide.

Rather than updating the sessions data source every 2 seconds the polling will check if the ID has changed and only update if necessary. The old check to see if the host had delted the session is now within this same check. The data source being changed by the user brings back the empty placeholder charts and each user will have to select new x and y valeus. 

I reused the upload method so it functions the same as the one in the main remote form.

The append method within the remote session lets the user pick from one of their uploaded files and append it to the sessions current data source. data sources extend method handles the compatibility checks. The new extended data is then made the sessions current data source for all users.

## Chat function

Remote DES controller will store the ID of the last message seen on self. This will be used when retrieving messages as the current function retrieves all messages after the given ID. For joining a lobby, all messages will be newer than the starting value of None and the chat history for that lobby will be shown. The visual time on messages str representation has been trimmed to just a time. 




