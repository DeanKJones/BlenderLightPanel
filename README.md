# Blender Lighting Panel

A quickly accessible list of all available lights and their parameters. 

## Installation

- Download `LightPanel.py`
- Store it as you want
- Open Blender (Version 3.1.0 and above)
- Install the add-on in Blender
```
     > Go to Edit -> Preferences 
     > Click on Add-ons -> install 
     > Navigate to the installation directory
     > Select and install the add-on
     > Check the box and save your preferences 
```
- To see the Add-on, move into the 3D View. Press `N` on your keyboard to open the tool window. A tab named "Lights" should appear at the bottom.
- To hide the window again, press `N`

## Usage
Here you will find a list of all available lights in the current scene. If you add or remove a light the list will automatically update. 
- By default you will be able to access the `Color`, `Strength` and `Type` of light
- Toggling `Advanced` on will give you more parameters to edit
- This also allows you to change the rendering mode between `Cycles` and `Eevee`
---
### Limitations
- Eevee Shadows are not supported
---
##### Notes
In a seperate branch: `abClass` I have another approach where each light gets its own UI class. I believe this would give better control over how the user interacts with the panel. This is taking more work though and I have not got it in a stable state yet. 
