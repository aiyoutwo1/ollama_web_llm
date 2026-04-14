'''
根据提问 调用大模型 把对应结果返回
'''
import json

'''
import ollama

def get_response(prompt):
    res = ollama.chat(
        model='deepseek-r1:1.5b',
        messages=[{
            "role": "user",
            "content":prompt
        }]
    )
    return res.message.content


if __name__ == '__main__':
    res1 = get_response('你是谁')
    print(res1)'''

import ollama

def get_res(prompt):
    res = ollama.chat(model='deepseek-r1:1.5b', messages=[{
        'role': 'user',
        'content': prompt
    }])
    return res.message.content

print(get_res('你是谁?'))


def read_data():
    with open('./1.json', 'r') as f:
        return json.load(f)


def write_data(data):
    with open('./1.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False,indent=4)


if __name__ == '__main__':
    l1 = [
        {
            'role': 'ai',
            'content': '你好，我是黑马智聊机器人，有什么可以帮助您的吗！'
        }
    ]
    write_data(l1)
