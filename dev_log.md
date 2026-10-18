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
