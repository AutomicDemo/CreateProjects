# CreateProjects
Pyral based python script to quickly create projects out of a CSV formatted txt file

## Installation
Install Python 3.6 or higher
Install pyral with the following command:
`pip install pyral`


## Configuration
Modify rally-v2.0.cfg to include your user credentials and workspace name.  With this script, the project setting is ignored.

project_list.txt is a CSV file and must exist in the same directory as the script

### project_list.txt Structure
The first row is a header and must be present in the file

Project name is always required.  

Project parent is optional.  If you do not specify a project parent, the project will be created at the root of your hierarchy.  If you wish to create this project under another project, a `_ref` to a parent project needs to be specified in this field.

`_previous` is a special keyword for the parent project field and if used, it will parent itself to the previously created project.  Rally limits project hierarchy to 10 levels, so don't go too crazy

## Execution
`python create_projects.py`
