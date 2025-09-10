The project is a tool for providing information for intelligence researchers,
with an emphasis on audio materials

The project is divided into services that divide the responsibility among themselves and transfer tasks to the next service via KAFKA

Service 1:

Goes through the files
Sends metadata and a path to KAFKA

Service 2:

Generates a unique ID
Uploads the file to Mongo and the MD to ES
Sends the ID to Kafka

Service 3

Downloads the file from Mongo
Transcribes it
Updates the transcription to ES
Sends the ID to Kafka

Service 4

Performs risk calculation operations for each ID
(not yet written the queries)
(I know I could put it in the pipeline but I don't have time to learn it...)

I chose to split everything into different services despite the difficulty in writing the function that implements access to information in some of the services in order to imitate the operations in some of the services and make the information that already exists accessible to researchers
In addition, this maintains the principle of "different operations in different places"