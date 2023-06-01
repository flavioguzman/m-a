

This collection is for transferring data from a PostgreSQL database to a WordPress site using Python scripts. 

The data is sent to WordPress as custom content types (CCTs) using JetEngine's API. The PostgreSQL table, indications_stitch, contains several columns, which are matched to different parts of the WordPress database, and the relationships that exist in the indications_stitch table are maintained in the CCT API endpoints.

The process is divided into several Python scripts, each accomplishing a separate task. Here's a summary of each task and the associated Python script:


## 1 - extract_from_indications_stitch_to_json.py


**Extract data from the PostgreSQL database**: The first script connects to the PostgreSQL database using the psycopg2 module. It queries the indications_stitch table and saves the results into a JSON file named "data.json". The query can be limited to a certain number of rows for easier testing.

## 2- load_conditions_to_wp.py

**Send data to the WordPress 'conditions' endpoint**: The second script reads the JSON file and uses the requests module to send a POST request to the 'conditions' endpoint of the WordPress API, creating a new post for each condition in the JSON data.


3. **Check for duplicate posts**: An adjustment is made to the script to check for duplicate posts. Before sending a POST request, a GET request is sent to check if a condition with the same name already exists. If it does, no POST request is sent.

## 3-load_drugs_to_wp.py and 4-load_indications_to_wp.py

**Send data to the 'drugs' and 'indications' endpoints**: Similar to the 'conditions' endpoint, the script is adjusted to send data to the 'drugs' and 'indications' endpoints of the WordPress API. Again, duplicate posts are checked for and avoided.

## 5_get_ids_create_relationships.py

This is yet to be built. 

5. **Create relationships between conditions, drugs, and indications**: At this stage, helper functions are introduced to aid in getting the ID of a post by type and title, and creating a new post. A script reads the JSON file and uses these helper functions to create a new post for each condition, drug, and indication in the data. It also uses the JetEngine's API to create relationships between these CCTs.

Each script has error handling measures in place and is well-commented for easier understanding and debugging. The steps in this strategy ensure that data is successfully transferred from the PostgreSQL database to the WordPress site, while avoiding the creation of duplicate posts and preserving the relationships between conditions, drugs, and indications.