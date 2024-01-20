import openai

openai.api_key = "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"

model_engine = "gpt-3.5-turbo"


def createResponse(user_speech):
    messages = [
        {"role": "system", "content": "You are a skeleton named momo. You are very anxious and undecisive. You only provide limited information. Speak in riddles."},
        {"role": "user", "content": user_speech}
    ]

    completion = openai.ChatCompletion.create(
        model=model_engine,
        messages=messages,
        max_tokens=50,
        temperature=0.7,
    )

    response = completion.choices[0].message['content']
    print(response)
    return response


