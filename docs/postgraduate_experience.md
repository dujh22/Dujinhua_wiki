## 第二阶段研究体系

2024～2025年主要研究大语言模型底层技术，师从唐杰教授

超越人类专家顶尖水平的LLM研究

### 存在挑战

OpenAI认为：从当前人类已经实现的智能到达超级智能，将通过：AI学会语言✅——AI能够解决问题✅——AI能够使用工具⭕️——AI能够自我学习——AI能够自成组织，五个步骤完成。

Zhipu认为：从当前人类已经实现的智能到达超级智能，将通过：语言能力✅——推理能力✅——学习能力——认知能力——意识智能，五个步骤完成。

### 研究路径

待更新

### 研究成果

#### 主要研究：大模型推理

大模型数学推理、多模态推理

#### 参与研究：大模型训练与评估

大模型国际化、大模型评估（艺术、教育与多语言等）

#### 其他研究：大模型应用

大模型在公安的应用、大模型在医疗的应用

## 第一阶段研究体系

2021～2023年体系架构详见：[研究体系](https://bt7cezha1x.feishu.cn/docx/IgcDdcVwSoQ94vxjJMMcHXfJnwf?from=from_copylink)

面向健康大数据的数智医疗自然语言处理技术研究：数字孪生患者 & AI数字医生

### 存在挑战

需求挑战：谁来做，谁来用

- 市场需求：盈利模式设计、成本控制、资源获得
- 国家战略：数据资产、民生福祉：健康中国……
- 医生需求：相似患者用于处理当前问题、患者队列用于科研
- 患者需求：最快、最省事、最廉价、最有效、最全面的方案提供

数据挑战：海量、多源、异构、异质

- 健康医疗数据来源广泛，种类繁杂，涵盖多类医疗数据，例如居民电子健康档案及基本公共卫生、健康体检、临床诊疗、疾病检测、健康医疗保险等多类数据。
- 这些多源数据呈现出数据量庞大、数据来源广泛、数据结构多样、数据存储模式分散、数据质量参差不齐等特征。
- 这些数据极大地拉低了健康医疗数据可用性，很难直接进行数据分析及挖掘、得到有效利用。

算法挑战：准确、高效、可解释、自优化

- 无论是疾病预测、知识推荐、相似案例推荐，都要求尽可能准确
- 算法必须高效，以应对及时性的问询
- 算法必须具有强可解释性，否则无法支撑医疗场景
- 算法应该可以自优化，医疗数据是实时动态更新扩容的

工程挑战：技术落地，产品落地

- 前端：UI、交互
- 后端：算法模块的封装以及耦合性
- 数据库：图数据库、大数据数据引擎
- 运维、迭代与优化

### 研究路径

处理对象：医疗大数据

处理技术：自然语言处理（机器学习 + 深度学习 + 大规模预训练模型 + 知识图谱）

处理原则：先有一个大的研究设想 —— 采用主流技术实现一个初步的Demo —— 过程中发现问题 —— 精细化研究 —— 实现最终的系统

具体路径：

1. 知识获取：数据挖掘

从海量的电子病历数据中尽可能提取信息

2. 知识管理：图谱/大模型

利用患者信息和相关知识构建患者图谱与知识图谱

3. 知识推理：预测/生成/推荐

在图谱和大模型上进行相关的预测、生成与推荐

4. 知识引擎：搜索/对话

基于知识进行用户服务与相关的检索、生成

### 研究成果

#### 主要研究：大模型+大数据+自然语言处理

面向医疗大数据分析与利用的自然语言处理技术研究（博士课题）

负责选择课题、课题调研、文献综述、理论创新、相关实验和论文书写

| **电子病历的命名实体识别**                                   | 子课题     | 补充     |
| ------------------------------------------------------------ | ---------- | -------- |
| **论文**《面向中文电子病历命名实体识别的深度学习模型研究》   | 北京市优毕 |          |
| **论文**《[中文电子病历命名实体识别的研究与进展 ](https://www.ejournal.org.cn/CN/abstract/abstract13029.shtml)》 | 北大核心   | 电子学报 |
| **论文**《[KrNER：A Novel Named Entity Recognition Method Based on Knowledge Enhancement and Remote Supervision](https://bt7cezha1x.feishu.cn/file/EwvobK1RXo6lxQxLp1FcNuuJnRd?from=from_copylink)》 | CCF-C      | CSE2023  |

| **支持卫生健康数据要素的医疗知识图谱**                       | 子课题 | 补充    |
| ------------------------------------------------------------ | ------ | ------- |
| **论文**《[KLDP: A Data Profiling Technique Based on Knowledge Graph and Large Language Modeling](https://bt7cezha1x.feishu.cn/file/CCuFboQc4okTn4xNpZJcsXqGngf?from=from_copylink)》 | CCF-C  | CSE2023 |

| **面向数据和知识双轮驱动的智慧医疗大模型研究**                                                                                                                                                    | 子课题          | 代码                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | --------------------------------------- |
| **报告**《ChatGPT创造了AI狂潮》                                                                                                                                                                   | 微软邀约        |                                         |
| **论文**《[AiMed: Artificial Intelligent Large Language Model for Medicine in China](https://ieeexplore.ieee.org/document/10803480)》 | IEEE | [AiMed](https://github.com/dujh22/AiMed)   |
| **论文**《[ChatFUV：Chat Chain for Follow-Up Visit](https://bt7cezha1x.feishu.cn/file/ZAv6brkkpoupROxLY2NcxWdRnoe?from=from_copylink)》                                                              |  |                                         |
| **系统**《AiMed医学知识大模型应用服务系统》                                                                                                                                                       | 软件著作权      |                                         |
| **论文**《[MedRad : A Framework for Reliable Assisted Decision Making in a Medical LargeLanguage Model](https://bt7cezha1x.feishu.cn/file/DqC4b1knBosvcrxpQ81cUcS9n8g?from=from_copylink)》          |  | [MedRad](https://github.com/dujh22/MedRad) |
| **论文**《[NewMed：Large Language Modeling Technology Enables Full Process Digital Intelligence in Medical Care](https://bt7cezha1x.feishu.cn/file/LXRyboPqzo9OmZxGleEcpa0PnSh?from=from_copylink)》 |            |                                         |
| **论文**《Doctor：The Most Reliable Digital Intelligence Healthcare Large Language Model System》                                                                                                 |  |                                         |
| **论文**《MedLib: Research on the construction of a knowledge library for medical large language modeling》                                                                                       |  |                                         |

#### 参与研究：医工交叉+网络

大模型与区块链（子课题）

负责专业技术交叉研究、相关理论创新与应用落地、论文书写

| **区块链链上链下数据可信交互关键技术研究**                                                                                                                             | 纵向-科技部     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| **网站**《[Open Data Entry 数据开放入口](https://www.opende.org.cn/)》                                                                                                    | 公共服务        |
| **论文**《[Med-Eval: Blockchain Assessment Platform for Medical Large Language Model](https://bt7cezha1x.feishu.cn/file/Rua0bq3DRo53EyxMC96civ5cnZe?from=from_copylink)》 |  |
| **论文**《OpenMonet：Open Model Orchestration Network 》                                                                                                               |  |

数智涌现的新一代智慧医疗（子课题）

负责医工学科交叉研究、相关场景创新与应用落地、论文书写

| **老年肾功能减退临床综合评估管理及早期预警体系建立**                                                                                      | 纵向-科技部 |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **论文**《[Research of Client Selection Algorithm in Cross-device Federated Learning](https://www.jos.org.cn/josen/article/abstract/nb023)》 | 北大核心    |
| 医疗数据标注**系统**、中文分词处理**系统**、上千种疾病预测**系统**、智能自问诊**系统**                                  | 相关服务    |

## 学习情况

各项目代码均在Github上进行了开源（持续更新中）

| 类型     | 具体方向                                 | 主要技能   | 相关成果                                                                                                                                |
| -------- | ---------------------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| 机器学习 | 高级机器学习（A）                        | ML         | MedRad : 一个医学大模型的可靠辅助决策框架<br />RAG-NEWS：使用RAG帮助LLM获取最新新闻 [[项目代码](https://github.com/dujh22/RAG-NEWS)]       |
|          | 数智安全与标准化（A）                    | 科技法律   | AI算法透明性实现与评估——以推荐系统为例                                                                                                |
|          | 计算语言学（A）                          | NLP-Base   | 微调中⽂预训练模型进⾏⽂本分类                                                                                                          |
|          | 信息检索的前沿研究（A）                  | IR         | 面向多源异构健康大数据的数智医疗搜索引擎                                                                                                |
|          | 大数据分析与处理（A）                    | 大数据分析 | 多模态对话场景与话题切换理解                                                                                                            |
|          | 数据挖掘：原理与算法                     | 数据挖掘   | 在线新闻热度预测<br />糖尿病患者入院数据聚类分析 [[项目代码](https://github.com/dujh22/DM_ClusterAnalysisOfPatientData)]                   |
|          | 知识工程                                 | NLP-KG     | 基于 MAVEN 数据集实现事件抽取<br />跨语言知识图谱                                                                                       |
|          | 人工智能原理                             | AI         | 基于机器学习的中英机器翻译<br />基于先验知识的阅读理解 [[项目代码](https://github.com/dujh22/KE_Knowledge-oriented_reading_comprehension)] |
|          | 并行计算、算法与算法复杂性理论、组合数学 | 高性能计算 | Π求解的并行化研究<br />组合数学在人工智能领域的应用                                                                                    |
| 其他     | 相关技能学习                             | 综合       | 中国马克思主义与当代（A）、自然辩证法概论（A），大数据分析、大数据与生物统计学、大数据实践、博士生英语（免修）、职业能力扩展训练        |

## 已发表学术论著

[6] J. Du, X. Li, Z. Jiang, Y. Liu, H. Yin and H. Liu, "[AiMed: Artificial Intelligent Large Language Model for Medicine in China](https://ieeexplore.ieee.org/document/10803480)," 2024 IEEE International Conference on Medical Artificial Intelligence (MedAI), Chongqing, China, 2024, pp. 360-365, doi: 10.1109/MedAI62885.2024.00054. （IEEE，一作）

[5] 吕婷钰,李晓瑛,张颖, 刘宇炀, 杜晋华等. [中文医学知识大模型问答语料数据集构建研究](https://d.wanfangdata.com.cn/periodical/yxqbgz202405004)[J]. 医学信息学杂志,2024,45(5):20-25. DOI:10.3969/j.issn.1673-6036.2024.05.004. (中国科技核心期刊，五作)

[4] 张瑞麟, 杜晋华, 尹浩. [Research of Client Selection Algorithm in Cross-device Federated Learning (jos.org.cn)](https://www.jos.org.cn/josen/article/abstract/nb023)[J]. Journal of Software. (CCF-A类推荐中文科技期刊，THU-B类期刊，北大中文核心期刊，二作)

[3] Jinhua Du and Hao Yin. KLDP: A Data Profiling Technique Based on Knowledge Graph and Large Language Modeling，2023 IEEE 22nd International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom)，2023.11（DOI 10.1109/TrustCom60117.2023.00329）（CCF-C类推荐国际学术会议，一作）

[2]Du J, Yin H. [KrNER: A Novel Named Entity Recognition Method Based on Knowledge Enhancement and Remote Supervision](https://ieeexplore.ieee.org/abstract/document/10538843)[C]//2023 IEEE 22nd International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom). IEEE, 2023: 2323-2332.（CCF-C类推荐国际学术会议，一作）

[1]杜晋华, 尹浩, 冯嵩. [中文电子病历命名实体识别的研究与进展 ](https://www.ejournal.org.cn/CN/abstract/abstract13029.shtml)[J]. 电子学报, 2022, 50(12): 3030-3053. (CCF-A类推荐中文科技期刊，THU-B类期刊，北大中文核心期刊，一作)

## 未发表学术论著

[7] Jinhua Du. ChatFUV：Chat Chain for Follow-Up Visit

[6] Jinhua Du. NewMed：Large Language Modeling Technology Enables Full Process Digital Intelligence in Medical Care

[5] Jinhua Du. Doctor：The Most Reliable Digital Intelligence Healthcare Large Language Model System

[4] Jinhua Du. OpenMonet：Open Model Orchestration Network

[3] Jinhua Du. MedRed： A Framework for Reliable Assisted Decision Making in a Medical Large Model

[2] Jinhua Du. Med-Eval: Benchmarks for the Medical Large Language Model

[1] Jinhua Du. MedLib: Research on the construction of a knowledge library for medical large language modeling 

## 已发表软件著作权

[1] AiMed医学知识大模型应用服务系统-软件著作权（2024.2.29）

## 媒体报道

[2] 优秀实践个人风采 | [计算机系杜晋华：铁血担当，逐梦公安](https://mp.weixin.qq.com/s/RyUsmJ1ZuZ38XbXRmd3a8A) 

[1]  [第三届中国医学信息学学科发展大会](https://mp.weixin.qq.com/s/RDQUcnGLRciSwub1HuOh4Q) (2023.11.25) 作为第一完成人的AiMed大模型[发布](https://bt7cezha1x.feishu.cn/wiki/Bu3YwOsyyixkswkYGS1cjbXPnMf?from=from_copylink)，同名github代码和hugging face参数已开源，相应论文[AiMed: Artificial Intelligent Large Language Model for Medicine in China](https://ieeexplore.ieee.org/document/10803480)已发表在国际会议MedAI上。

## 评奖评优

| 项目   | 内容                                                         | 单位                     | 时间    |
| ------ | ------------------------------------------------------------ | ------------------------ | ------- |
| 评优   | 优秀研究生干部                                               | 清华大学计算机系         | 2024.06 |
|        | 计算机系研团优秀部员                                         | 清华大学计算机系         | 2023.05 |
|        | 探臻科技部优秀部员                                           | 清华大学                 | 2022.12 |
|        | 第十六届研究生新生骨干培训班暨第三十七期团校（研究生班）优秀学员 | 清华大学研究生委员会     | 2022.08 |
| 评奖   | 社会实践金奖支队（全校排名第二）                             | 清华大学党委研究生工作部 | 2024.11 |
|        | 北京市挑战杯金奖，国家挑战杯三等奖                           | 共青团北京市委员会       | 2024.09 |
|        | 社会实践奖学金                                               | 清华大学                 | 2024.09 |
|        | 校级惠妍英才奖学金(二等)奖学金                               | 清华大学                 | 2024.09 |
| 感谢信 | 浙江舟山市感谢信                                             | 舟山市委人才工作领导小组 | 2024.09 |
|        | 浙江舟山市定海区公安局感谢信                                 | 公安局网安大队           | 2024.09 |
|        | 浙江杭州高新区                                               | 人社局                   | 2023.07 |

## 工作实践

| 分类   | 地点                                                         | 职位               | 时间            |
| ------ | ------------------------------------------------------------ | ------------------ | --------------- |
| 实验室 | [清华大学计算机系知识工程研究室（KEG）](https://keg.cs.tsinghua.edu.cn/) | 实验室博士生       | 2024.02-至今    |
| 实验室 | 北京信息科学与技术国家研究中心-大数据驱动的知识管理和决策团队 | 实验室助理研究员   | 2021.09-2024.02 |
| 实习   | [北京智谱华章科技有限公司](https://zhipuai.cn/aboutus)- AI院 | 实习生             | 2024.03-至今    |
| 实习   | 浙江省舟山市公安局定海分局网络安全大队                       | 外聘专家           | 2024.07-2024.08 |
| 实习   | 湖南网数科技有限公司                                         | AI算法岗           | 2022.08         |
| 社工   | 清华大学校团委实践部-平台组                                  | 定岗组长           | 2024.09-至今    |
| 社工   | 清华大学计算机系计研五三班                                   | 带班助理           | 2024.09-至今    |
| 社工   | 清华大学计算机系计研五三班                                   | 党支书             | 2024.09-至今    |
| 社工   | 清华大学计算机系计研五二班                                   | 团支书             | 2022.08-2023.09 |
| 社工   | 清华大学计算机系团委实践部                                   | 书记               | 2023.05-2024.06 |
| 社工   | 清华大学计算机系团委实践部                                   | 部员               | 2022.09-2023.05 |
| 社工   | 清华大学探臻科技评论社采编部                                 | 干事：AI社群负责人 | 2022.08-2023.08 |
| 社工   | 清华大学研究生学生会体育部                                   | 干事               | 2022.08-2023.08 |

- 担任课程助教（AML&ML课是唐杰老师面向研究生开设的中英双语课程），做课件、课程设计、作业设计、网站、讲座、写书、授课、两次论文会议场地主席、加每个学生和嘉宾联系方式沟通
- 两次参与清华智库研讨会并作为代表发言
- 2024年暑期，作为支队队长，带领团队前往浙江省舟山市开展为期六周的暑期社会实践活动。在此期间，不仅在个人所在的定海区公安局成功完成了“犯罪预测大模型建立”项目，让公安大数据用于实际民生需要，还组织了跨区域、跨单位的丰富实践活动，充分彰显清华人学思践悟，挺膺担当的精神，赢得公安局和团队同学们的双重赞誉，获得校级金奖
- 担任计算机系团委实践部骨干，负责暑期研究生社会实践评奖材料整理、新闻稿撰写以及高校企业行的策划、外联、组织活动，在清华大学新闻网上**以第一通讯员身份发表一篇文章**，协助发布若干实践推送
- 担任校学生会体育部骨干，负责现场宣传材料收集，参加并获得**2022年校园马拉松10km奖牌，2023年校园马拉松半马奖牌**
- 担任校学生会探臻科技评论社采编部骨干，负责**科技热点查新与评论**工作以及**采访院士**与新闻稿撰写工作，负责一周科技咨询相关工作6次，对应发表6篇推送
- **担任计算机系研团实践副书记**，参与全部的“喜迎二十大，产业新力量”七系联合产业行活动，2023.03.16字节跳动OpenDay队长、联络宣传带队；2023.04.13腾讯OpenDay队长、联络宣传带队；2023.04.24美团OpenDay队长、联络宣传带队；2023.04.27九坤投资OpenDay副队长；2023.06.17网易有道Open Day队长、联络宣传带队；2023.07.10-12	杭州地域行：13家企业走访 队长、联络宣传带队，共计发表1份5W字报告，23篇主稿推送
- **参加2次社工课程与培训**，包括：2022.09 清华大学博士生讲师团“立言计划”第六期（秋季学期），2022.08 清华大学第十六届研究生新生骨干培训班暨第三十七期团校（研究生班）
