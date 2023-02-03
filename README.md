# ECSE3038

Aaron Samuel 620141792

# update_todo_by_id()

Purpose: To handle incoming PATCH requests from the demo site.

Expanation: The update_todo_by_id function is added to handle incoming PATCH requests. 

The function accepts the todo_id in the URL path, and the updated todo as a JSON object in the request body. It "scans" over the fake_database to find the todo with a matching id.  

If/When the id is found, it uses the update() method to merge the updates into the todo In this case, the frint end version of the website is programmed to strikethrough the text and place a check arrow, indicating a completed task.

Finally, it returns a success message indicating that the todo has been updated. 
If the todo is not found, the function returns a message indicating that the todo was not found.

# delete_todo_by_id()

Purpose: To handle incoming DELETE requests from the demo site.

The delete_todo function handles incoming DELETE requests by accepting the todo_id in the URL path, and matching it over the fake_database. 

After it finds the todo with a matching id, it deletes the todo from the fake_database using the del statement. This is nly the case IF the id of the item is found.

Finally, it returns a success message indicating that the todo has been deleted. If the todo is not found, the function returns a message indicating that the todo was not found.

# Favourite Pokemon

Actually never watched pokemon, that being said, 