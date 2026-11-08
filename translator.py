from openai import OpenAI

BASE_URL = "https://api.groq.com/openai/v1"
MODEL = "openai/gpt-oss-120b"

SYSTEM_PROMPT = (
    "Переклади вхідний текст на мову: {lang}. "
    "Відповідай ЛИШЕ перекладом. Без вступів, пояснень, коментарів, "
    "лапок навколо тексту та фраз на кшталт «Ось переклад»."
)


def translate(api_key, target_lang, text):
    if not api_key.strip():
        return "Введіть API-ключ."
    if not text.strip():
        return "Введіть текст."

    system = SYSTEM_PROMPT.format(lang=target_lang.strip() or "українська")
    try:
        client = OpenAI(api_key=api_key.strip(), base_url=BASE_URL)
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": text},
            ],
            temperature=0.3,
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"Помилка виклику LLM: {e}"
