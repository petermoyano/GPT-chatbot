import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


while True:
    try:
        user_input = input("You...")
        res = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_input,
            max_tokens=100

        )
        print(res.choices[0].text)

    except KeyboardInterrupt:
        print("Exiting...")
        break

print(res)
