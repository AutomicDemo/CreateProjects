import sys
import urllib3
import csv
from pyral import Rally, rallyWorkset

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

options = [arg for arg in sys.argv[1:] if arg.startswith('--')]
args = [arg for arg in sys.argv[1:] if arg not in options]
server, user, password, apikey, workspace, project = rallyWorkset(options)

rally = Rally(server, user, password, workspace=workspace, project=project, verify_ssl_cert=False)
rally.enableLogging(dest=b'CreateProjects.log', attrget=True)

with open('project_list.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    previous = ""

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if row[1] == "_previous":
                row[1] = "https://rally1.rallydev.com/slm/webservice/v2.0/project/{}".format(previous)

            project_data = {
                "Name": row[0],
                "Parent": row[1],
                "State": "Open"
            }

            print('Creating project {project_name} with parent {parent_name}'.format(project_name=row[0], parent_name=row[1]))
            project = rally.put('Project', project_data)
            previous = project.ObjectID
            print('Created project {project_name} OID {object_id}'.format(project_name=project.Name, object_id=project.ObjectID))

            line_count += 1

    print(f'Processed {line_count} lines.')
