# sonar-report
By Eduardo Perez

[![#](https://img.shields.io/badge/python-3.x-yellow.svg)](#)
[![#](https://img.shields.io/badge/docker-2.3.x-099cec.svg)](#)

This project is a terminal report generated by a sonarqube docker. <br>
This project was created because of my laziness of having to access the site every time I want to see the coverage and code smells

Hope you enjoy it =)

#project configuration

This project uses a .conf file to get variables to run.

````
{
    "name": "OSGI",
    "key": "osgi",
    "sonar_url": "http://localhost:9000",
    "metrics": ["code_smells", "coverage", "duplicated_blocks"], 
    "details": {
        "code_smells" : {
            "name": "CODE_SMELL",
            "sort" : "type",
            "types" : ["MINOR", "MAJOR", "CRITICAL", "BLOCKER"]
        },
        "security" : {
            "name" : "SECURITY_HOTSPOT",
            "sort" : "status",
            "types" : ["MINOR", "MAJOR", "CRITICAL", "BLOCKER"]
        }
    },
    "specific_data" : {
        "code_smells" : {
            "types" : ["MINOR", "MAJOR", "CRITICAL", "BLOCKER"],
            "itens" : ["severity", "component", "status", "message"]
        }
    }
}
````

variables:<br>
* name: project name (just set what you want to show it in the report)
* key: project key (the one you put in sonar docker when creating your project profile)
* metrics: these are the porcentage generated on the sonar, you should put the same of the sonar API documents
* detais: these are some detais of the metrics, in a simple way, it's the number of each kind of code smell and security problens (not implemented yet)
* specific data: these are some messages of  data, I'm trying to use that to get code smell messages.
