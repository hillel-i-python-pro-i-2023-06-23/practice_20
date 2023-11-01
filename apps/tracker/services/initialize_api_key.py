def initialize_api_key():
    with open("api_key.txt") as file:
        api_key_value = file.read().strip()

    with open(".env.homework") as file:
        env_template = file.read()

    env_template = env_template.replace("API_KEY='b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'", f"API_KEY='{api_key_value}'")

    with open(".env", "w") as file:
        file.write(env_template)
