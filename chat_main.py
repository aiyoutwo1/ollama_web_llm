import streamlit as st
from chat_utils import read_data, write_data, get_res

st.title('人工智能页面实现')  # 标题
st.divider()  # 画一条横线


  # 因为不知道提问次数 所以?
st.session_state['messages'] = read_data()  # st的session_state是一个存储器 总体是一个字典

for msg in st.session_state['messages']:
    with st.chat_message(msg['role']):
        st.write(msg['content'])

prompt = st.chat_input('请输入您的问题')  # prompt变量接受用户输入的问题 chat_input()的方法是生成一个底部输入框
if prompt:  # 如果确实输入了,执行
    with st.chat_message('user'):
        st.write(prompt)

    st.session_state['messages'].append(
        {
         'role': 'user',
         'content': prompt
         }
     )
    res = get_res(prompt)
    with st.chat_message('ai'):
        st.write(res)

    st.session_state['messages'].append({
     'role': 'ai',
     'content': res
 })
write_data(st.session_state['messages'])

