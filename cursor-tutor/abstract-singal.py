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
        prompt=f"简单总结该段文字中发明的效果：\n\n{text}\n\n具体发明效果：",
        max_tokens=2000,     
    )

    # 提取回复
    reply = response.choices[0].text.strip()
    return reply

# 示例文本

text = """
本发明公开了一种防强光和蓝光的新型眼镜，其包括由树脂单体固化成型的光学镜片基体，光学镜片基体具有前折射率凸面与后折射率凹面；后折射率凹面具有位于中央的主视表面、位于上侧的上偏光表面、及位于下侧的下偏光表面；通过无影胶粘接于上偏光表面的上偏光树脂基底层；通过无影胶粘接于下偏光表面的下偏光树脂基底层；其中，上偏光树脂基底层与下偏光树脂基底层由添加防蓝光基材的树脂单体固化成型，且表面镀覆有多个低折射率膜层与高折射率膜层。本发明通过在光学镜片基体的内侧上下分别粘接上偏光树脂基底层与下偏光树脂基底层，利用低折射率膜层与高折射率膜层不断折射强光，基片防蓝关，避免以往眼镜片抗强光、防蓝光功能性差的麻烦。
"""

# 使用示例文本调用函数
problems = extract_problem_from_text(text)
print(problems)

