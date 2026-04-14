# 智聊机器人的前台界面程序
# 1- 导入相关的库: streamlit  后台服务模块

import streamlit as st
from chat_utils import get_res


# 2- 设置页面
# 2.1 设置标题
st.title('黑马程序AI')
# 2.2 添加一条横线 用于分割
st.divider()
# st.session_state 在页面反复执行时候 可以记住之前的数据  当成字典用
# 因为 Streamlit 每点一次按钮，就会从头到尾重新运行一遍代码！
# 如果不用 session_state：
# 你输入的内容会消失
# 计数器会清零
# 所有变量都会重置
# session_state 就是用来 “记住” 东西的。

# 3 判断是否有历史记录
if 'messages' not in st.session_state:  # st.session_state是类字典  session:(一段连续的)活动时间,会话期 state:声明,状态
    st.session_state['messages'] = []  # 如果不在的话 创建一个空列表  第一次运行时，创建一个空列表；后续每次运行，列表里已经有历史消息了，就不会再重置，完美保住聊天记录！
    st.session_state['messages'].append(  # st.session_state的结构{'messages':[]           }
        {
            'role': 'ai',
            'content': '你好，我是黑马智聊机器人，有什么可以帮助您的吗！'
        }
    )
# 3.1 如果没有就创建, 并存储消息记录， 添加机器人欢迎语 你好，我是黑马智聊机器人，有什么可以帮助您的吗！
# 3.2 如果有就展示 聊天信息
for msg in st.session_state['messages']:

    with st.chat_message(msg['role']):  # with st.chat_message()方法 是 图片 + 说话 .
        st.write(msg['content'])

# 3.3 遍历 聊天记录展示到页面上


# 4 设置用户输入的聊天框：
prompt = st.chat_input('请输入您的问题')
# 4.1 如果用户已经输入了内容， 将用户输入的内容写入到聊天区
if prompt:
    st.session_state['messages'].append({  # KeyError 键错误 streamlit 没有找到键 可能键拼写错误
        'role': 'user',
        'content': prompt
    })
    with st.chat_message('user'):
        st.write(prompt)
    with st.spinner('ai正在运行,请稍后'):
        res = get_res(prompt)
    st.session_state['messages'].append({
        'role': 'ai',
        'content': res
    })
    with st.chat_message('ai'):
        st.write(res)
# '''
# 写一下:st.session_state里面的数据
# {'model':'deepseek-r1:1.5b'
# 'messages':[
# {"role": "ai", "content": "你好..."},
# {"role": "user", "content": "你好"}
# ]
# }
# st.session_state 最终存储的真实样子
# 字典 {}：用来分类存放不同的东西（模型、历史记录、用户名...）
# 列表 []：用来按顺序存放聊天记录，一条接一条
# 小字典 {}：用来规范每一条消息的格式（谁发的？发了什么？）
# 这叫嵌套数据结构
# '''
# 4.2 根据 用户调用大模型，获取结果
# 4.3 将回答显示到页面上

# '''
# st.session_state['messages'] = [
#     # 第1轮：AI欢迎语
#     {"role": "ai", "content": "你好，我是黑马智聊机器人，有什么可以帮助您的吗！"},
#     # 第2轮：用户提问
#     {"role": "user", "content": "帮我写一个Python爬虫"},
#     # 第3轮：AI回复
#     {"role": "ai", "content": "好的，这是一个简单的爬虫示例..."},
#     # 第4轮：用户追问
#     {"role": "user", "content": "能不能加个代理？"},
#     # ... 无限追加
# ]
# 用列表是为了「按顺序存多轮对话」，字典是「单条消息的格式」，列表 + 字典组合，就是聊天记录的标准结构！


