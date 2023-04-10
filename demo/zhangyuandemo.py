#encoding:utf8
import openai
openai.api_key = "33f883816ed544de8216dda2d14c69f5"
openai.api_base =  "https://365-a.openai.azure.com/" # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
deployment_name= 'patent' #This will correspond to the custom name you chose for your deployment when you deployed a model. 
openai.api_version = '2023-03-15-preview' # this may change in the future


result = openai.ChatCompletion.create(
  engine="patent",
  temperature = 0.05,
  messages=[
        # {"role": "system", "content": "你是一个专利权利要求点分析器"},
        {"role": "user", "content": """Help me extract device entities and relationships between device entities from the following patent claim point in turn, and the relationships between entities should be returned in the form of triples (device entities, predicates, device entities) in the order in which they appear in the claim text, and the predicates must appear explicitly in the claim point text:
        claim point:一种机器人，其特征在于，包括：机器人主体；图像采集组件，设于所述机器人主体，所述图像采集组件包括图像采集器；传声组件，设于所述机器人主体，且围设于所述图像采集器。"""},
        {"role":"assistant","content":"device entities:机器人、机器人主体、图像采集组件、图像采集器、传声组件\nrelationships:(机器人,包括,机器人主体)、(机器人,包括,图像采集组件)、(图像采集组件,设于,机器人主体)、(图像采集组件,包括,图像采集器)、(机器人,包括,传声组件)、(传声组件,设于,机器人主体)、(传声组件,围设于,图像采集器)"},
        {"role":"user","content":"claim point:根据权利要求1所述的一种应用于电阻焊机器人第四轴的传动结构，包括偏心安装孔和台阶状沉孔。"},
        {"role":"assistant","content":"device entities:应用于电阻焊机器人第四轴的传动结构、偏心安装孔、台阶状沉孔\nrelationships:(应用于电阻焊机器人第四轴的传动结构,包括,偏心安装孔)、(应用于电阻焊机器人第四轴的传动结构,包括,台阶状沉孔)"},  
        {"role":"user","content":"claim point:每个所述电动伸缩杆一端通过球铰与所述底盘的顶面连接、另一端通过球铰与所述支撑板的底面连接，且三个所述电动伸缩杆与所述底盘的连接点呈三角形分布，三个所述电动伸缩杆与所述支撑板的连接点呈三角形分布。"},
        {"role":"assistant","content":"device entities:电动伸缩杆、球铰、底盘、支撑板\nrelationships:(电动伸缩杆,连接,底盘)、(电动伸缩杆,连接,支撑板)"},  
        {"role":"user","content":"claim point:一种微型吸附式机器人，包括运动装置、吸附装置、控制装置及作为机架的主体框架，其特征是：所述的运动装置的连杆机构有7个活动构件，n＝7；A、C、D三处都是三个构件汇交的复合铰链，各有两个转动副，B、E、F、G处各有一个转动副，故运动低副(转动副)数P所述的吸附装置包括吸附底板(7)、吸盘(8)、真空泵(5)以及硅胶导气管(6)；真空泵(5)通过硅胶导气管(6)连接到吸附底板(7)，吸附底板(7)内部有空腔结构，用以连通硅胶导气管(6)和多个吸盘(8)，以使吸盘(8)与真空泵(5)相连以形成负压；真空泵(5)由Arduino控制板(1)控制，两边的吸附底板(7)上各有多个吸盘(8)及真空泵(5)，当吸附底板(7)落下时，对应的真空泵(5)工作，吸盘(8)产生负压，使吸附底板(7)能牢固的抓住壁面；所述的控制系统包括电源模块(12)、Arduino控制板(1)、双轴减速电机(3)；双轴减速电机(3)安装在主体框架(2)上，Arduino控制板(1)放置在双轴减速电机(3)上面，电源模块(12)安装在主体框架(2)后侧。"},
       


    ]
)
print(result)
print(type(result))
print(result["choices"][0]["message"]["content"])