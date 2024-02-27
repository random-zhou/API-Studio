import argparse
from openai import OpenAI
from tqdm import tqdm

# Define your base prompt as before
base_prompt='................................................................（你的需求，什么场景，什么情况，干什么）'

def load_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    return data

def get_response(prompt):
    client = OpenAI(
        api_key='sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        base_url='https://oneapi.run.place/v1',
    )

    messages = [{
        'role': 'system',
        'content': base_prompt,
    }, {
        'role': 'user',
        'content': prompt
    }]

    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        #如有可换为gpt4 以及其他模型
        messages=messages,
        temperature=0.3,
    )
    return completion.choices[0].message.content

def run(file_path):
    prompts = load_txt(file_path).split('\n')

    for prompt in tqdm(prompts):
        response = get_response(prompt)
        with open(f'conversation.txt', 'a', encoding='utf-8') as f:
            f.write(response + "\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process conversation inputs.')
    parser.add_argument('--file_path', type=str, required=True, help='Path to the input text file')
    args = parser.parse_args()

    run(args.file_path)