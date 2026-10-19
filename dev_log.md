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
ChatView - The chat window for a remote DES
LocalDESView - The DES window for a local session
RemoteDESView - The DES window for a remote lobby

### Model

FileManager - Reads data from a file
DatabaseManager - Performs database operations
DataSource - Holds the data read from a file
User - Holds user information
Message - Holds message information
DESSession - Holds session information for a DES
DataVisualiser - Maps the data to a chart
ChatRoom - Holds session information for a remote lobby chat room

### Controller

app - Parses the command line arguments and starts the relevant mode
test_app - App for testing, runs through the functionality of the app
local_app - The local app
remote_app - The remote app

The original app.py always loaded the login screen and local mode was launched through a button there, to completemly decouple the modes
the local, remote, and testing modes now launch through argparse. This means that local mode can be launched when no database exists as the previous login screen imported and depended on pymongo.

The first class i made is datasource. I started by making a constructor that takes the name of the data source and its data, the constructor has handlers to replace empty data with and empty list. I looked into the unittesting module and made a test class for the datasource class which tests the columns method with real data, empty data, none data, a compltely empty constructor. and a test to ensure that two data sources do not have a shared state. The way i originally made the class meant that each instance would always reference the same empty list as a default value when no data was given. to fix this the new empty list is made within the constructor rather than in the default values for the method parameter.

Next i gave it an is_empty method to check whether a data source has any rows, this will be used within other methods as a helper. I also gave it a method to check if two data sources are compatible that will be used before appending some data to other data. This method jsut checks that either one or both sources are empty or that the column names are an exact match. Im unsure if thjis will need to be changed later if potentially i need to append data with the same base columns and also some new columns, or if the same colums exist but in another order. Tests were added to test these two new methods.

In data source i decided to add the append method here rather than in file manager because data source is responsible for the data when it is in memory. this means file manager will be responsible for the saving and loading of the files but not manipulating the actual data. The append method will first check compatibility and return an exception is that check fails. this will be used later in a GUI dialogue popup. As with the other methods I added tests to the test class for each case and continued running them as i go. This method completes datasource fucntionailiy for what is needed in local mode.




