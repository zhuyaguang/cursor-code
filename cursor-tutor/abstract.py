# -*- coding: utf-8 -*-
import openai

openai.api_key = "33f883816ed544de8216dda2d14c69f5"
openai.api_base =  "https://365-a.openai.azure.com/" # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2023-03-15-preview' # this may change in the future




import concurrent.futures

def extract_problem_from_text(text):
    def call_gpt3():
        # 调用GPT-3.5 API  gpt-35-turbo (version 0301)
        result = openai.ChatCompletion.create(
            engine="patent",
            temperature = 0.05,
            max_tokens=1000,
            messages=[
                {"role": "user", "content": "一句话简单总结该段文字中发明的效果。尽量用原文中文字描述"},
                {"role":"user","content":"摘要:本发明公开了一种防眩光抗紫外线防护镜片，包括镜片基体，镜片基体包括前基片、后基片、及复合于前基片与后基片之间的纳米复合膜层，纳米复合膜层具有位于中央的防眩光膜层，及位于防眩光膜层至少一侧的多个薄膜层，多个薄膜层包括1.5折射率膜层、1.67折射率膜层及抗紫外线膜层；其中，前基片与后基片的外表面分别环设半圈对应的弧度凹槽，弧度凹槽用于安装硅胶夹持架。本发明通过在前基片与后基片之间设置纳米复合膜层，实现防眩光、抗紫外线，同时半圈弧度凹槽嵌合装夹硅胶夹持架，方便取用，避免掉落磕碰的麻烦。"},
                {"role":"assistant","content":"该发明的效果是：防眩光、抗紫外线，并且方便取用，避免掉落磕碰的麻烦"},  
                {"role": "user", "content": f"{text}"},
            ]
        )
        reply = result["choices"][0]["message"]["content"]
        return reply

    timeout_seconds = 10  # 设置超时时间，可以根据需要调整

    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(call_gpt3)
            reply = future.result(timeout=timeout_seconds)
        return reply
    except concurrent.futures.TimeoutError:
        return "抱歉，函数执行超时，请稍后再试。"




# To handle timeout errors, we can wrap the API call in a try-except block and catch the `openai.error.APIError` exception. We can then check if the error message contains the string "timeout" and retry the API call if it does. We can set a maximum number of retries to avoid an infinite loop. Here's an example:

def extract_problem_from_text2(text):
    # 调用GPT-3 API text-davinci-003
    max_retries = 3
    retries = 0
    while retries < max_retries:
        try:
            response = openai.Completion.create(
                engine="patent-03",
                prompt=f"简单总结该段文字中发明的效果：\n{text}",
                temperature = 0.05,
                max_tokens=1000,
            )
            break
        except openai.error.APIError as error:
            if "timeout" in str(error).lower():
                retries += 1
                continue
            else:
                raise error
    
    # 提取回复
    reply = response.choices[0].text.strip()
    return reply


import mysql.connector


# 数据库连接配置
config = {
    "user": "root",
    "password": "itech4u123",
    "host": "10.101.32.33",
    "database": "itech4u",
    "port": 30306, 
}

# 连接到数据库
connection = mysql.connector.connect(**config)

# 创建一个游标对象
cursor = connection.cursor()

# SQL 查询语句
query = '''
SELECT application_no, abstract
FROM `patent-20230322`
WHERE patent_type = '中国实用新型专利授权公告标准化全文文本数据'
AND technical_field NOT LIKE '%机器人%'
ORDER BY RAND()
LIMIT 4995'''

# 执行查询
cursor.execute(query)

# 获取查询结果
results = cursor.fetchall()
count = 0 
# 打印查询结果
for row in results:
    application_no, abstract = row
    count = count+1
    print(count)
    print(f"Application No: {application_no}, Abstract: {abstract}")
    problems = extract_problem_from_text(abstract)
    # 拼接两个字符串
    combined_text = application_no+"\n"+abstract + "\n" + problems + "\n" +"######" + "\n"
    # 将拼接后的字符串写入文件
    with open("random.txt", "a", encoding="utf-8") as file:
        file.write(combined_text)


# 关闭游标和数据库连接
cursor.close()
connection.close()
