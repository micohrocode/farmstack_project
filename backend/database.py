from model import Todo
# mondo db driver
import motor.motor_asyncio

# create client
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
# the database and collection to connect to
database = client.TodoList
collection = database.todo


async def fetch_one_todo(title):
    # get the document by the based in title
    document = await collection.find_one({"title":title})
    return document

async def fetch_all_todos():
    todos = []
    # get all documents from the collection
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    # create a document in the collection
    result = await collection.insert_one(document)
    return result

async def update_todo(title, desc):
    # update todo description from title
    await collection.update_one({"title":title},{"$set":{
        "description":desc
    }})
    document = await collection.find_one({"title":title})
    return document

async def remove_todo(title):
    # delete document by title
    await collection.delete_one({"title":title})
    return True