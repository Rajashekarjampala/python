SECTION 1 :
----------
    # Deploy Mongo-DB using Docker as database for GPM :

        - We have to pull the docker image from docker hub

        - Pull the mongo image by using below command
            docker pull mongo

        - Check the mongo image created or not by using below command
            docker images

        - Create the docker container on detached mode by using below command 
            docker run --name <container_name> -d -p 27017:27017 mongo

        - Check the docker running containers by using below command
            docker ps -a

        - Access the mongo application by using below command
            VM_IP:<Container_port>   

        - Mongo DB default port number is 27017
            10.208.41.125:27017

        - Deploy the docker by using docker network
        - Create a network for mongodb by using below command
            docker network create <Network_Name>

        - Create Docker Container and run that container in mongo network
            docker run --name <containername> --net <Network_Name> -p 27017:27017 mongo

SECTION 2 :
----------
    # Login to Mongo, run sample tests casess :

        - Login to the mongo container by using below command
            docker exec -it <container_id> /bin/bash

        - Run mango command inside the container
            mongo    

        - To check the dbs in inside the container by using below command
            show dbs 

        - Create the db inside the container by using below command
            use <db_name>

SECTION 3 :
    # Perform CRUD operations on MongoDB :
        
        - MongoDB CRUD operations using the MongoDB Query Language (MQL).
        - CRUD stands for Create, Read, Update, and Delete.

        - Create operation is used to insert new documents in the MongoDB database.
        - Read operation is used to query a document in the database.
        - Update operation is used to modify existing documents in the database.
        - Delete operation is used to remove documents in the database.

        - CREATE Operations :

        - Create DB :
        - Insert One
        - insertOne() allows you to insert one document into the collection.

            db.emp_data.insertOne({
                emp_id: "123",
                name: "raj",
                age: "25",
                address: "hyderabad",
                contact: "1234567890",
                chipped: true                        
            })

        - Insert Many
        - Insert multiple items at one time by calling the insertMany() method on the desired collection.

            db.emp_data.insertMany([
                {emp_id: "123",
                name: "raj",
                age: "25",
                address: "hyderabad",
                contact: "12323455"
                chipped: true},                                    

                {emp_id: "980", 
                name: "sai",
                age: "24",             
                address: "nellur", 
                contact: "34568965"
                chipped: true},

                {emp_id: "678", 
                name: "venkat",
                age: "26",             
                address: "guntur", 
                contact: "7789533"
                chipped: true},

                {emp_id: "690"
                name: "mahesh",
                age: "27",
                address: "chennai",
                contact: "57893455"
                chipped: true},

                {emp_id: "457"
                name: "prashanth",
                age: "23",
                address: "bangulur",
                contact: "90123455"
                chipped: true},                
                ])

        - READ Operations :

        - Find collections :
        - To get all the documents from a collection, we can simply use the find() method on collection.
            db.emp_data.find()
            db.emp_data.find({}).pretty()
            db.emp_data.findOne({"age":"25"})

        - UPDATE Operations :

        - Update operation takes filters and criteria to select the documents you want to update.    
        - Update One :
        - We can update a currently existing record and change a single document with an update operation

        - We use the updateOne() method on a chosen collection
        - We use the “$set” key and provide the fields we want to update as a value.
            db.emp_data.updateOne({emp_id: "123"}, {$set:{address: "pune"}})

        - Update Many :
        - updateMany() allows us to update multiple items by passing in a list of items.
            db.emp_data.updateMany({emp_id:"123"}, {$set: {age: "22"}})  

        - Replace One :
        - The replaceOne() method is used to replace a single document in the specified collection
            db.emp_data.replaceOne({emp_id: "123"}, {emp_id: "321"})

        - DELETE Operations :

        - Delete One
        - deleteOne() is used to remove a document from a specified collection on the MongoDB server
            db.emp_data.deleteOne({emp_id:"321"})

        - Delete Many :
        - deleteMany() is a method used to delete multiple documents from a desired collection
            db.emp_data.deleteMany({name:"sai"})     

SECTION 4 :
    # References
        - https://www.youtube.com/watch?v=v6Xmydb7u4Y
        - https://www.mongodb.com/basics/crud
























                   












