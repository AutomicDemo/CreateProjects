# CreateProjects
Pyral based python script to quickly create projects out of a CSV formatted txt file

project_list.txt must exist in the same directory as the script
The first row is a header
Required fields are project name and a _ref to a parent project if it is to be a child project
_previous is a special keyword for the parent project field and if used, it will parent itself to the previously created project.
Rally limits project hierarchy to 10 levels, so don't go too crazy
