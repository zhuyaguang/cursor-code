import openai

openai.api_key = "3a516ff904514b90a4268e33ca517a60"
openai.api_base =  "https://365-a.openai.azure.com/" # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2022-12-01' # this may change in the future

deployment_name='test' #This will correspond to the custom name you chose for your deployment when you deployed a model. 


def extract_problem_from_text(text):
    # 调用GPT-3 API
    response = openai.Completion.create(
        engine="test",
        prompt=f"请从以下文本中提取发明解决的具体问题：\n\n{text}\n\n发明解决的具体问题：",
        max_tokens=2000,     
    )

    # 提取回复
    reply = response.choices[0].text.strip()
    return reply

# 示例文本

text = """[0002]机器人是一种能够半自主或全自主工作的智能机器，具有感知、决策、执行等基本特征，可以辅助甚至替代人类完成危险、繁重、复杂的工作，提高工作效率与质量，服务人类生活，扩大或延伸人的活动及能力范围。[0003]随着技术的不断发展，在实际生活及生产中，越来越多的机器人或机械臂替代或辅助人工工作，在热敏灸时，也会使用到机械臂辅助工作；在现有的技术中，多数热敏灸机械臂均安装在机箱上，而现有的机箱仅仅起到支撑机械手和安装电气装置等功能，导致在热敏灸作业过程中，机箱较为浪费空间，同时使用效率不高。因此，本领域技术人员提供了一种热敏灸机器人机箱，以解决上述背景技术中提出的问题。"""

# 使用示例文本调用函数
problems = extract_problem_from_text(text)
print(problems)

# 拼接两个字符串
combined_text = text + "\n" + problems

# 将拼接后的字符串写入文件
with open("output.txt", "a", encoding="utf-8") as file:
    file.write(combined_text)

print("字符串已成功保存到文件。")
