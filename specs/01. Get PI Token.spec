Get PI Token Specification
==========================
Date Created    : 11/05/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_pi_token



Invoke PI API using valid username and password and save the access token inside the text file
----------------------------------------------------------------------------------------------
* Given that a user needs to invoke "Get PI Token"
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |N/A                            |
     |isAccessTokenRetrievedFromTextFile|N/A                            |
     |accessTokenString                 |N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#username                       |osanda                   |
     |#password                       |Password1                |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.status      |success        |
* And save the access token which is the attribute value of "data" in the response


