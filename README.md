# W+M1 
Web app that aims to aggregate common penetration testing tools into easy-to-use guis that still provide full control over what happens. 

## Setting up locally
1) Create your desired workspaces in the `workspace` folder
2) Copy `Example-Manifest.xml` to `manifest.xml` in each workspace root
3) Add an `nmap` and `temp` folder to each workspace 
4) Update `workspaces.xml` to reflect changes

### You're now ready to start contributing, but keep in mind the following:
* Try to avoid modifying core and base files when your focus isnt them
* Try to stay within the layout of the project, avoid leaving source files lying around in random folders

## Known issues
* Reloading the page sends you back to the dashboard
* Typing "exit" in the terminal causes an IO error, requiring an app restart to resolve
* Having no active workspaces causes a server error
* After running for some time, the server can throw: KeyError: 'Session is disconnected'
* Revshell floods console
* Setting up a nightmare