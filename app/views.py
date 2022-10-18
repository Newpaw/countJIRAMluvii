from flask import render_template, request
from app import app
from outputForWeb import getUserTime


#pocetHodin = "8"
#pocetDni = "1"
# worklogAuthors = ["62f9fcb31e82e839c24f4417", "61a73fa8c75da80072f8fb5e"]


allUsers = {'login mluvii': '5d6f8b05dc6e480dbc021590', 'stepan.dostal@mluvii.com': 'qm:36e95ce4-f090-461b-88d1-8e7b47761510:6194dd75-4ec3-4e5e-abec-d00e07782442', 'ondrej.vondra@mluvii.com': 'qm:36e95ce4-f090-461b-88d1-8e7b47761510:cfd0731b-c068-485b-a435-08ffee4306a7', 'Mluvii Test Helpdesk': 'qm:36e95ce4-f090-461b-88d1-8e7b47761510:1e5b4a77-2526-4468-b034-5187f5eeba7c', 'login@mluvii.com': 'qm:36e95ce4-f090-461b-88d1-8e7b47761510:e45c7b48-e0a8-414a-bbb2-a9dfb8a1c6fa',\
     'karolina.branikova@mluvii.com': 'qm:36e95ce4-f090-461b-88d1-8e7b47761510:04d026f6-001f-43a2-a7ac-becf11566322', 'alzbeta.brozova@mluvii.com': 'qm:36e95ce4-f090-461b-88d1-8e7b47761510:dc9e9184-e39a-4a9d-9ab5-1dbfff44f241', 'barbora.dankova@mluvii.com': 'qm:36e95ce4-f090-461b-88d1-8e7b47761510:0b4d7718-2bfe-4803-bd14-5365b01d56b5', 'jan.novopacky@mluvii.com': 'qm:36e95ce4-f090-461b-88d1-8e7b47761510:9260274e-ea9a-4503-b503-22e554ab660d', 'michael.hausner@mluvii.com': 'qm:36e95ce4-f090-461b-88d1-8e7b47761510:e792a14b-ad62-4254-b488-048b5e32c6d4', 'Jan Novopacký': '5b1e72e2edacc156e2f35ad3', '102085dd-1ee2-4322-bc20-23dc18779e1d': '606ec870b845ed006ec7b018', 'Atlassian Assist': '5cb4ae0e4b97ab11a18e00c7', 'Automation for Jira': '557058:f58131cb-b67d-43c7-b30d-6b58d40bd077', 'Blanka Morikawa': '6017d584d04785006887ffbb', 'Chat Notifications': '5b70c8b80fd0ac05d389f5e9', 'Clockify Integration': '5eb3c2949ce9ee0b898683aa', 'Clockwork Automated Timesheets Free': '5d710216522f790d9c773bce', 'Confluence Analytics (System)': '557058:cbc04d7b-be84-46eb-90e4-e567aa5332c6', 'Confluence Google Drive': '557058:eb0bdb70-01b2-431f-b665-fdebfb16c665', 'Dana Adamová': '6116adaf2ba37b0067c9d78e', 'David Rosko': '62dd1e7dbc2c449f3d938cec', 'Git Integration for Jira': '557058:f33197a6-29c6-4af0-b9b8-d0048c78da35', 'GitLab for Jira (gitlab.com)': '5d6d3f563803ee0db6cee1d0', 'Gliffy Diagram for Confluence': '557058:a952278b-16e8-496c-95bf-6fa96e9cdb3c', 'Issue Checklist': '5c6145a82cdb124474b3dda9', 'Jan Matura': '5d258d9aa459740c4cdcf965', 'jan.skrle': '62cc3528bd54f8d3ffb5ebc9', 'Jaroslav Čech': '557058:e3640400-9c6c-414b-9e2d-dfe253caaa4d', 'Jira Ops Confluence integration': '5bbd7c592995be2f0a42d77d', 'Jira Outlook': '5d53f3cbc6b9320d9ea5bdc2', 'Jira Service Management Widget': '557058:950f9f5b-3d6d-4e1d-954a-21367ae9ac75', 'Jira Spreadsheets': '5cf112d31552030f1e3a5905', 'Karolína Brániková': '5b2cbffaba383e081400b28e', 'Lucidchart Diagrams Connector': '557058:9ab63286-11ed-497d-8147-88b76e6c8a56', 'Martin Kikerle': '619e3fef6d002b006b7d8a15', 'Mermaid for Confluence': '5ed27bd1a04d9c0c221d501f', 'Microsoft Teams for Confluence Cloud': '6035864ce2020c0070b5285b', 'Microsoft Teams for Jira Cloud': '60e5a86a471e61006a4c51fd', 'Ondřej Fogatoš': '5b1e72f1927da916aaaa7429', 'Ondřej Vondra': '5b1a938282e05b22cc7d666b', 'Opsgenie Incident Timeline': '5d9afe0010f4800c341a2bba', 'Opsgenie Integration': '5dd64082af96bc0efbe55103', 'Pavel Chmela': '62e7c57850bd9783f62a64de', 'Petr Částek': '61a73fa8c75da80072f8fb5e', 'Petr Dobroucký': '5b1e72f7d2f5b64e4d2147d1',\
     'Quantify AI': '5abdcbec9fde9a645c7684af', 'Sabina Lepicová': '6019314c4e258e006950bd2a', 'sd-no-app-access-local-user-addon': '5b95d5f04d21642beb810cae', 'Connor Tomáš': '62f9fcb31e82e839c24f4417'}




@app.route("/", methods=['GET', 'POST'])

def answer():

    if request.method == 'POST':
        form_data = request.form
        form_data_str = str(form_data["comp_select"])
        UserOutput = getUserTime(form_data_str)
        diskOfIdTimedict = zip(UserOutput[2], UserOutput[3])
        return render_template("table.html", pocetHodin=UserOutput[0], pocetDni=UserOutput[1], diskOfIdTimedict = diskOfIdTimedict, allUsers=allUsers)
    else:
        return render_template("table.html", allUsers= allUsers)


