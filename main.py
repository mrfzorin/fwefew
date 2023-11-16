import openai

def generate_response(message: str) -> str:
    # Замените 'YOUR_OPENAI_API_KEY' на ваш API ключ.
    openai.api_key = 'sk-fewfedf'

    response = openai.Completion.create(
        model="gpt-4-1106-preview",  # Замените на актуальную модель, если это необходимо
        prompt=message,            # Ваш запрос к модели GPT
        max_tokens=1000             # Максимальное количество токенов в ответе
    )

    return response.choices[0].text.strip()
