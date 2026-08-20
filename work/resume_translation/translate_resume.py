from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree
import re, shutil, tempfile

SRC = Path('work/resume_translation/source.docx')
OUT = Path('work/resume_translation/Jinhua_Du_CV_English.docx')

T = {
'主研项目(课题负责)': 'Primary Research Project (Project Lead)',
'面向基础模型深度复杂推理的关键技术研究': 'Key Technologies for Deep and Complex Reasoning in Foundation Models',
' 博士理论课题': ' Doctoral Theoretical Research',
'基础模型复杂推理研究': 'Complex Reasoning with Foundation Models',
'子课题/科技部重点研发计划': 'Subproject / National Key R&D Program of China',
'清华大学、天津大学、智谱AI': 'Tsinghua University, Tianjin University, and Zhipu AI',
'论文《Glm-4.5: Agentic, reasoning, and coding (arc) foundation models》': 'Paper: "GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models"',
'论文《A Survey of Post-Training Scaling in Large Language Models》': 'Paper: "A Survey of Post-Training Scaling in Large Language Models"',
'论文《': 'Paper: "',
'》（在审）': '" (under review)',
'AAAI在投': 'Submitted to AAAI',
'面向医疗大数据分析与利用的自然语言处理技术研究': 'Natural Language Processing for Medical Big Data Analysis and Utilization',
' 博士应用课题': ' Doctoral Applied Research',
'支持卫生健康数据要素的医疗知识图谱': 'Medical Knowledge Graphs Supporting Healthcare Data Elements',
'子课题': 'Subproject',
'论文《中文电子病历命名实体识别的研究与进展》': 'Paper: "Research and Advances in Named Entity Recognition for Chinese Electronic Medical Records"',
'电子学报': 'Acta Electronica Sinica',
'论文《KrNER：A Novel Named Entity Recognition Method Based on Knowledge Enhancement and ': 'Paper: "KrNER: A Novel Named Entity Recognition Method Based on Knowledge Enhancement and ',
'论文《KLDP: A Data Profiling Technique Based on Knowledge Graph and LLM》': 'Paper: "KLDP: A Data Profiling Technique Based on Knowledge Graph and LLM"',
'面向数据和知识双轮驱动的智慧医疗大模型研究 AiMed': 'AiMed: Smart Healthcare LLMs Driven by Both Data and Knowledge',
'报告《ChatGPT创造了AI狂潮》': 'Talk: "ChatGPT Has Sparked an AI Craze"',
' 微软邀约': ' Invited by Microsoft',
'论文《AiMed: Artificial Intelligence large language model for chinese Medicine》': 'Paper: "AiMed: Artificial Intelligence Large Language Model for Chinese Medicine"',
'软著': 'Software Copyright',
'论文《Towards Artificial Intelligence for Science': 'Paper: "Towards Artificial Intelligence for Science',
'SCI一区': 'SCI Q1',
'论文《Large Language Models Driven Reliable Clinical Decision-Making》': 'Paper: "Large Language Models Driven Reliable Clinical Decision-Making"',
'论文《Toward a Large Language Model-Driven Medical Knowledge Retrieval and QA System: ': 'Paper: "Toward a Large Language Model-Driven Medical Knowledge Retrieval and QA System: ',
'  SCI一区': '  SCI Q1',
'负责选择课题、课题调研、文献综述、理论创新、相关实验和论文书写': 'Led topic selection, background research, literature review, theoretical innovation, experiments, and paper writing',
'杜晋华': 'Jinhua Du',
'唐杰教授 ': 'Prof. Jie Tang ',
'大语言模型方向四年级博士2027-2028毕业（': 'Fourth-year Ph.D. student specializing in LLMs; expected graduation: 2027-2028 (',
'科研经历': 'Research Experience',
'竞赛获奖': 'Competition Awards',
'评奖评优': 'Honors and Awards',
'国家奖学金、国家励志奖学金、清华大学优秀研究生干部、金奖支队队长、硕博论坛卓越奖': 'National Scholarship; National Encouragement Scholarship; Outstanding Graduate Student Leader, Tsinghua University; Captain of a Gold Award Student Team; Excellence Award at the Master\'s and Doctoral Forum',
'第一名': 'First Place',
'全区公安机关外聘专家、北京市优秀本科毕业生、北京市优秀本科毕业论文、北地先锋“十佳学生”': 'External Expert for regional public security agencies; Outstanding Undergraduate Graduate of Beijing; Outstanding Undergraduate Thesis of Beijing; "Top Ten Student" of Beidi Pioneer',
'国家级竞赛': 'National Competitions',
'一等奖：美国大学生数学建模、青创北京2024年“挑战杯”首都大学生创业计划竞赛主赛道金奖': 'First prizes: MCM/ICM; Gold Award in the main track of the 2024 "Challenge Cup" Capital University Student Entrepreneurship Competition',
'二等奖：全国高校计算机能力挑战赛、Robocup机器人世界杯中国赛': 'Second prizes: National University Computer Skills Challenge; RoboCup China Open',
'省部级竞赛': 'Provincial/Ministerial Competitions',
'一等奖：蓝桥杯全国软件和信息技术专业人才大赛、移动应用创新赛': 'First prizes: Lanqiao Cup National Software and IT Professionals Competition; Mobile Application Innovation Competition',
'其他有代表性共计50余项目竞赛获奖，参见抬头靠右二维码或个人主页': 'More than 50 additional representative competition awards; see the QR codes above or the personal homepage',
'学历技能': 'Education and Skills',
'               计算机科学与技术系工学博士                        清华大学': '               Ph.D. in Computer Science and Technology                  Tsinghua University',
'专业主修：高级机器学习（A）、大数据分析与处理（A）、计算语言学（A）、信息检索的前沿研究（A）、网络计算与区块链技术（A）、数智安全与标准化（A）、数据挖掘原理与算法、知识工程、人工智能原理等': 'Selected coursework: Advanced Machine Learning (A), Big Data Analysis and Processing (A), Computational Linguistics (A), Frontiers of Information Retrieval (A), Network Computing and Blockchain Technology (A), Digital-Intelligence Security and Standardization (A), Principles and Algorithms of Data Mining, Knowledge Engineering, Principles of Artificial Intelligence, etc.',
'研究方向：大模型、自然语言处理、机器学习、大数据分析': 'Research interests: Large language models, natural language processing, machine learning, and big data analytics',
'主要成果：论文13篇': 'Key achievements: 13 papers',
'：ML方向CCF-A 1篇，NLP方向CCF-A 1篇，CCF ': ': 1 CCF-A paper in ML, 1 CCF-A paper in NLP, 2 CCF-',
'-2篇，LLM方向CCF A-2篇，SCI一区-2篇，三区-1篇，': ' papers, 2 CCF-A papers on LLMs, 2 SCI Q1 papers, and 1 SCI Q3 paper; ',
'完整训练5个大模型：GLM、LogicGLM、MalayGLM、AiMed、公安大模型': 'trained five large models end-to-end: GLM, LogicGLM, MalayGLM, AiMed, and a public-security LLM',
'               计算机科学与技术系工学学士              中国地质大学（北京）': '               B.Eng. in Computer Science and Technology       China University of Geosciences (Beijing)',
'专业主修：C++程序设计（100）、科学工程与计算（100）、高性能计算（99）、人工智能（97.9）、操作系统原理（97）、数据结构（94）、软件工程（优秀）等': 'Selected coursework: C++ Programming (100), Scientific Engineering and Computing (100), High-Performance Computing (99), Artificial Intelligence (97.9), Principles of Operating Systems (97), Data Structures (94), Software Engineering (Excellent), etc.',
'研究方向：机器学习、数值分析、机器人（多智能体）': 'Research interests: Machine learning, numerical analysis, and robotics (multi-agent systems)',
'主要成果：论文6篇': 'Key achievements: 6 papers',
'：机器学习与数值计算/建模方向3篇论文（2篇EI，1篇核心），机器学习与智能控制、机器人方向3篇论文（1篇SCI，1篇EI，1篇核心）': ': 3 papers on machine learning and numerical computing/modeling (2 EI-indexed and 1 core-journal paper), and 3 papers on machine learning, intelligent control, and robotics (1 SCI, 1 EI-indexed, and 1 core-journal paper)',
'英语水平：IELTS(7.0)、CET6(525)、CET4(580)': 'English proficiency: IELTS 7.0; CET-6 525; CET-4 580',
'相关技能：掌握 Python、C/C++、熟悉 JAVA、Lua、Go 等编程语言，熟悉使用 MATLAB 进行数值分析与计算': 'Technical skills: Proficient in Python and C/C++; familiar with Java, Lua, Go, and other languages; experienced with MATLAB for numerical analysis and computing',
'绩点': 'GPA',
'性别：男': 'Gender: Male',
'院系：计算机系': 'Department: Computer Science',
'排名': 'Rank',
'年龄：2': 'Age: 2',
'面貌：中共党员': 'Political affiliation: CPC Member',
'职务：': 'Roles: ',
'计算机系研究生党支部书记、计研五三班级带班助理': 'Secretary, Graduate Student Party Branch; Class Advisor, CS Graduate Class 53',
'辅导员': 'Counselor',
'学工经历': 'Student Leadership and Service',
'唐杰教授《高级机器学习》课程助教，第一作者负责书籍': 'Teaching assistant for Prof. Jie Tang\'s Advanced Machine Learning; lead author responsible for the book ',
'《大语言模型》': 'Large Language Models',
'的编写和修改，设立对应网站': ', including writing, revision, and development of its companion website',
'担任清华大学研团实践部定岗组长': 'Appointed team leader in the Practice Department of the Tsinghua Graduate Youth League Committee',
'，构建优化“同行实践平台”微信小程序，持续服务全校硕博研究生': '; developed and optimized the "Tongxing Practice Platform" WeChat mini program serving master\'s and doctoral students university-wide',
'在清华大学新闻网上': 'Published on Tsinghua University News ',
'以第一通讯员身份发表文章': 'as the primary correspondent',
'担任计算机系研团实践部书记': 'Served as Secretary of the Practice Department, Computer Science Graduate Youth League Committee',
'，作为队长负责联络宣传带队全部的七系联合产业行活动，包括北京字节跳动、腾讯、美团、九坤投资、网易有道、杭州13家科技企业走访，主稿23篇推送': '; led coordination, publicity, and all joint industry visits across seven departments, including visits to ByteDance, Tencent, Meituan, Ubiquant Investment, NetEase Youdao, and 13 technology companies in Hangzhou; drafted 23 official posts',
'担任带班助理，': 'Served as a class advisor; ',
'获得3次集体荣誉': 'received three collective honors',
'：笃行班团、卓越班团（全校仅5个）、清华大学甲级团支部': ': Duxing Model Class/League Branch, Outstanding Class/League Branch (only five university-wide), and Tsinghua University Class-A Youth League Branch',
'获得10次个人荣誉': 'Received 10 individual honors',
'：专业二等奖学金、社会工作二等奖学金、社会实践奖学金、清华大学优秀共青团员、校研团组长任职经历证明、计算机系研团书记任职经历证明、团支部书记任职聘书、新生骨干优秀学员': ': Second-Class Academic Scholarship, Second-Class Social Work Scholarship, Social Practice Scholarship, Outstanding Communist Youth League Member of Tsinghua University, certificates of service as a Graduate Youth League team leader and departmental secretary, appointment letter as Youth League Branch Secretary, and Outstanding New Student Leader',
'担任校学生会体育部骨干，长期坚持跑步和健身，获得': 'Core member of the University Student Union Sports Department; maintained long-term running and fitness training; earned ',
'马拉松10km奖牌，半马奖牌，健美小组第五名': 'a 10 km race medal, a half-marathon medal, and fifth place in the bodybuilding group',
'实习经历': 'Internship Experience',
'中国北京智谱华章科技股份有限公司-AI院': 'Beijing Zhipu Huazhang Technology Co., Ltd. - AI Institute, China',
'AI研发岗': 'AI R&D Engineer',
'中国湖南网数科技有限公司-网络大数据研究中心': 'Hunan Wangshu Technology Co., Ltd. - Network Big Data Research Center, China',
'中国科学院信息工程研究所': 'Institute of Information Engineering, Chinese Academy of Sciences',
'助理研究岗': 'Assistant Researcher',
'中国阿里云原生团队': 'Alibaba Cloud Native Team, China',
'算法岗': 'Algorithm Engineer',
'中国地质大学（北京）信息技术创新中心': 'Information Technology Innovation Center, China University of Geosciences (Beijing)',
'竞赛主管': 'Competition Program Supervisor',
'个人陈述': 'Personal Statement',
'参研项目(技术)': 'Participating Project (Technical Contributor)',
'区块链链上链下数据可信交互关键技术研究': 'Key Technologies for Trusted On-Chain/Off-Chain Data Interaction in Blockchain',
'纵向-科技部': 'Government-funded - Ministry of Science and Technology',
'大模型与区块链': 'Large Language Models and Blockchain',
'网站《Open Data Entry 数据开放入口》': 'Website: "Open Data Entry"',
'公共服务': 'Public Service',
'论文《Is ChatGPT All That MedNLP Needs? A Systematic Evaluation of Knowledge Discovery ': 'Paper: "Is ChatGPT All That MedNLP Needs? A Systematic Evaluation of Knowledge Discovery ',
'在投': 'Submitted',
'论文《OpenMonet：Open Model Orchestration Network》': 'Paper: "OpenMonet: Open Model Orchestration Network"',
'在研': 'In Progress',
'负责专业技术交叉研究、相关理论创新与应用落地、论文书写': 'Conducted interdisciplinary technical research, theoretical innovation, application implementation, and paper writing',
'老年肾功能减退临床综合评估管理及早期预警体系建立': 'Comprehensive Clinical Assessment, Management, and Early-Warning System for Declining Renal Function in Older Adults',
'数智涌现的新一代智慧医疗': 'Next-Generation Smart Healthcare through Digital-Intelligence Emergence',
'论文《Research of Client Selection Algorithm in Cross-device Federated Learning》': 'Paper: "Research of Client Selection Algorithm in Cross-Device Federated Learning"',
'软件学报': 'Journal of Software',
'医疗数据标注系统、中文分词处理系统': 'Medical Data Annotation System and Chinese Word Segmentation System',
'相关服务': 'Related Services',
'负责医工学科交叉研究、相关场景创新与应用落地、论文书写': 'Conducted interdisciplinary medical-engineering research, scenario innovation, application implementation, and paper writing',
'创业项目(项目负责)': 'Entrepreneurial Project (Project Lead)',
'基于强化学习的足球机器人教练系统研发': 'Development of a Reinforcement Learning-Based Coaching System for Robot Soccer',
'国家级': 'National-Level Project',
'基于ROS的多级足球机器人系统的开发': 'Development of a Multi-Level ROS-Based Robot Soccer System',
'论文《基于Ubuntu下ros变种rocos等操作系统架构的研究》': 'Paper: "Research on the Architecture of Operating Systems Such as ROCOS, a ROS Variant, under Ubuntu"',
'科技核心': 'Chinese Science and Technology Core Journal',
'论文《System Composition and Optimization of Small Soccer Robot》': 'Paper: "System Composition and Optimization of Small Soccer Robot"',
'外文EI': 'English-Language EI-Indexed',
'论文《基于改进人工势场和新型网格的路径规划》': 'Paper: "Path Planning Based on an Improved Artificial Potential Field and a Novel Grid"',
'北大核心': 'Peking University Core Journal',
'负责项目整体研究思路梳理和研究内容分工，完成核心AI算法开发和系统搭建': 'Developed the overall research plan and task allocation; completed core AI algorithm development and system implementation',
'合作项目(组长)': 'Collaborative Project (Team Lead)',
'论文《基于主成分分析对禁瓶令效果的研究》': 'Paper: "Study on the Effectiveness of a Bottle Ban Based on Principal Component Analysis"',
'国家刊物': 'National Journal',
'论文《Global epidemic classification based on K-nearest neighbor algorithm》': 'Paper: "Global Epidemic Classification Based on the K-Nearest Neighbor Algorithm"',
'论文《Mid-term and long-term prediction of carbon emissions in Jiangsu Province based on ': 'Paper: "Mid-Term and Long-Term Prediction of Carbon Emissions in Jiangsu Province Based on ',
' 外文EI': ' English-Language EI-Indexed',
'负责AI算法开发与实验，文献查阅和调研': 'Responsible for AI algorithm development and experiments, literature review, and background research',
'外包项目(项目负责)': 'Outsourced Project (Project Lead)',
'AiMed 医学知识大模型应用服务系统': 'AiMed Medical-Knowledge LLM Application Service System',
' 软件著作权': ' Software Copyright',
'风力发电机气动平衡检测系统、智慧型半人工酒店系统': 'Wind Turbine Aerodynamic Balance Detection System; Intelligent Semi-Automated Hotel System',
'控制项目进度，负责建立系统框架，核心程序开发，方案展示及答辩': 'Managed project schedules; built system frameworks; developed core programs; delivered solution presentations and defenses',
'认真负责，严谨细致，逻辑思维和学习能力强；拥有良好的人际沟通能力且善于团队合作。希望经过博士阶段系统的科研训练，在未来做出真正造福世界、改变世界，助力全人类向善、向好、向幸福的事。': 'Responsible, rigorous, and detail-oriented, with strong logical reasoning and learning ability. I communicate effectively and collaborate well in teams. Through systematic doctoral research training, I hope to create work that genuinely benefits and improves the world, contributing to a kinder, better, and happier future for all.',
}

han = re.compile(r'[\u3400-\u9fff]')
ns = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
}
W = '{%s}' % ns['w']
A = '{%s}' % ns['a']

with ZipFile(SRC, 'r') as zin:
    files = {name: zin.read(name) for name in zin.namelist()}

changed = 0
unmapped = []
for name, data in list(files.items()):
    if not name.endswith('.xml'):
        continue
    try:
        root = etree.fromstring(data)
    except etree.XMLSyntaxError:
        continue
    dirty = False
    for el in root.iter():
        if etree.QName(el).localname not in ('t', 'delText') or el.text is None:
            continue
        src = el.text
        if not han.search(src):
            continue
        if src not in T:
            unmapped.append((name, src))
            continue
        el.text = T[src]
        changed += 1
        dirty = True
        # Ensure Latin text uses a reliable font while preserving existing size/weight.
        parent = el.getparent()
        while parent is not None and etree.QName(parent).localname not in ('r',):
            parent = parent.getparent()
        if parent is not None:
            if parent.tag == W + 'r':
                rpr = parent.find(W + 'rPr')
                if rpr is None:
                    rpr = etree.Element(W + 'rPr')
                    parent.insert(0, rpr)
                rfonts = rpr.find(W + 'rFonts')
                if rfonts is None:
                    rfonts = etree.SubElement(rpr, W + 'rFonts')
                for attr in ('ascii', 'hAnsi', 'eastAsia', 'cs'):
                    rfonts.set(W + attr, 'Arial')
                lang = rpr.find(W + 'lang')
                if lang is None:
                    lang = etree.SubElement(rpr, W + 'lang')
                lang.set(W + 'val', 'en-US')
            elif parent.tag == A + 'r':
                rpr = parent.find(A + 'rPr')
                if rpr is None:
                    rpr = etree.Element(A + 'rPr')
                    parent.insert(0, rpr)
                rpr.set('lang', 'en-US')
    if dirty:
        files[name] = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone='yes')

if unmapped:
    print('UNMAPPED CHINESE TEXT:')
    for item in unmapped:
        print(item)
    raise SystemExit(2)

with ZipFile(OUT, 'w', ZIP_DEFLATED) as zout:
    for name, data in files.items():
        zout.writestr(name, data)

print(f'Wrote {OUT} with {changed} translated text nodes.')
