def load_env(env_file_path):
    env_vars = {}
    with open(env_file_path, 'r') as file:
        for line in file:
            # Extract key-value pairs
            key, value = line.strip().split('=', 1)
            env_vars[key] = value

    return env_vars
    
env_file_path = "./credentials"  
env_variables = load_env(env_file_path)

# Access variables from the returned dictionary
DB_NAME = env_variables.get('dbname')
USERNAME = env_variables.get('user')
PASSWORD = env_variables.get('password')
HOST = env_variables.get('localhost')
PORT = env_variables.get('port')

# Print the variables
#print(DB_NAME, USERNAME, PASSWORD)
