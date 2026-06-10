# soldier

a soldier should be made of these fields
id: unique number identifier
full name: string
rank: string
unit: string
is_active:boolean

# endpoints

POST, /setup, "create new table"
GET, /schema, "returns the structure of the soldiers table" (comes from DESCRIBE soldiers;)

GET, /soldiers/{soldier_id}, get_soldier_by_id
GET, /soldiers, get_soldiers
POST, /soldiers/create, add_soldier
PATCH, /soldiers/update/{soldier_id}, update_soldier
DELETE, /soldiers/remove/{soldier_id}, remove_soldier

the order of connecting to a database server in python is making a connection and then making a cursor and executing commands im pretty sure

# functions

get_soldier_by_id: takes soldier id as int returns the soldier detail
get_soldiers: takes nothing return full list of soldiers details
add_soldier: takes full details of a soldier without id returns status
updata_soldier: takes details to update returns status
remove_soldier: takes soldier id as int returns the soldier

