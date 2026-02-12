# Postgraduate Experience

From the fourth year of undergraduate studies through the second year of doctoral studies, the research focus shifted to medical big data and knowledge engineering, with 13 papers published or in progress. The research objective is to harness massive medical data for disease prediction and knowledge discovery, addressing science and engineering problems related to people's livelihoods. The work spans from underlying data processing and algorithmic modeling to high-level system design, supporting the deployment of medical intelligence applications.

After the second year of doctoral studies, the research direction further shifted toward the underlying reasoning capabilities of large language models, with 3 papers currently in progress. Beginning with expansion from medical scenarios to public security, multilingual, and other domains of large model training, it was found that both model reliability and generalization are significantly constrained by underlying reasoning capabilities. This led to systematic research on reasoning abilities, exploring from three perspectives: evaluation methods, data construction, and algorithmic mechanisms.

## Phase 2 Research: Theory-Oriented

Since 2024, the primary focus has been on large language model underlying technologies, under the supervision of Prof. Jie Tang.

LLM research surpassing top human expert levels: *Towards Reliable and Generalizable Reasoning in Foundation Models*

### Existing Challenges

OpenAI's view: From current human-achieved intelligence to superintelligence will be accomplished through five steps: AI learns language ✅ — AI can solve problems ✅ — AI can use tools ✅ — AI can self-learn ⌛️ — AI can self-organize.

Zhipu's view: From current human-achieved intelligence to superintelligence will be accomplished through five steps: Language capability ✅ — Reasoning capability ✅ — Learning capability ⌛️ — Cognitive capability — Conscious intelligence.

### Research Path

As large-scale language models (LLMs) achieve breakthroughs in critical domains such as healthcare, public security, multilingual, mathematics, and code intelligence, their underlying reasoning capabilities have become the core bottleneck affecting model reliability, generalization, and application boundaries. Current models often exhibit issues such as "appearing to solve problems without knowing why they are correct" and "unstable capabilities when switching scenarios," limiting model trustworthiness in high-risk scenarios.

Based on practical experience from cross-domain model training and data system construction, this research aims to systematically study from both theoretical and engineering perspectives: **how to precisely measure, continuously improve, and stably transfer the logical reasoning capabilities of large models across scenarios**, laying theoretical and methodological foundations for trustworthy AI and interpretable intelligence.

### Research Outputs

#### Main Research: Large Model Reasoning

Mathematical reasoning and multimodal reasoning in large models

| Paper | Venue | Author Position | Category |
| ----- | ----- | --------------- | -------- |
| [Glm-4.5: Agentic, reasoning, and coding (arc) foundation models](https://arxiv.org/abs/2508.06471) | Arxiv | Non-first author | Preprint |
| [A Survey of Post-Training Scaling in Large Language Models](https://aclanthology.org/2025.acl-long.140/) | ACL | Non-first author | CCF-A |

| Project | Specific Output | Period |
| ------- | --------------- | ------ |
| Logic | Paper under blind review | 2025.03-present |
| Math | Enhancing Mathematical Reasoning in Multimodal Large Language Models | 2024.03-2024.10 |
| General | Self-Learning: Evaluation & Data & New Scaling Law | 2024.12-2025.01 |

#### Main Research: Large Model Training and Evaluation

| Project | Specific Output | Period |
| ------- | --------------- | ------ |
| Internationalization | Developed "Belt and Road Sovereign Large Model" MalayGLM, partnering with Malaysia's leading family conglomerate to help Malaysia build a national-level sovereign large model and empower the Malaysian large model industry ecosystem. This represents a breakthrough as the first meaningful deployment of a Chinese sovereign large model in a friendly country. (Achieved SOTA results in evaluation.) | 2024.09-2025.03 |
| Internationalization | Resolved ChatGLM mixed Chinese-English response issues | 2024.03-2024.06 |
| Evaluation | Meta-evaluation | 2024.12-2025.02 |
| Evaluation | Leveraging Models as Teachers: A Comprehensive Evaluation of Reasoning Abilities in Large Language Models (Arts, Education, Multilingual, etc.) | 2024.03-2024.09 |
| Evaluation | Generalization evaluation and research of o1-like models | 2024.09-2025.03 |

#### Main Research: Large Model Applications

Applications of large models in public security, healthcare, and sports

- Establishment of crime prediction large model
- Construction of sports multi-agent system

## Phase 1 Research: Engineering-Oriented

System architecture for 2021–2023: [Research System](https://bt7cezha1x.feishu.cn/docx/IgcDdcVwSoQ94vxjJMMcHXfJnwf?from=from_copylink)

Natural language processing technology research for intelligent healthcare with health big data: Digital Twin Patient & AI Digital Doctor

### Existing Challenges

**Demand Challenges** — Who builds it, who uses it

- Market demand: Profit model design, cost control, resource acquisition
- National strategy: Data assets, people's livelihood and welfare (Healthy China, etc.)
- Physician needs: Similar patients for handling current cases, patient cohorts for research
- Patient needs: Fastest, most convenient, cheapest, most effective, most comprehensive solutions

**Data Challenges** — Massive, multi-source, heterogeneous

- Health and medical data come from diverse sources with varied types, including electronic health records, basic public health, health exams, clinical diagnosis and treatment, disease detection, health insurance, and more.
- This multi-source data exhibits characteristics such as large volume, broad sources, diverse structures, dispersed storage, and uneven quality.
- These factors significantly reduce the usability of health and medical data, making direct analysis and mining difficult.

**Algorithm Challenges** — Accurate, efficient, interpretable, self-optimizing

- Whether for disease prediction, knowledge recommendation, or similar case recommendation, maximum accuracy is required
- Algorithms must be efficient to handle time-sensitive queries
- Algorithms must be strongly interpretable to support medical scenarios
- Algorithms should be self-optimizing, as medical data is dynamically updated and expanded in real time

**Engineering Challenges** — Technical and product deployment

- Frontend: UI, interaction
- Backend: Algorithm module encapsulation and coupling
- Database: Graph database, big data engines
- Operations, iteration, and optimization

### Research Path

**Processing object**: Medical big data

**Processing technology**: Natural language processing (machine learning + deep learning + large-scale pre-trained models + knowledge graphs)

**Processing principle**: Start with a broad research vision — Implement an initial demo using mainstream technologies — Identify issues during the process — Refine research — Realize the final system

**Specific path**:

1. Knowledge acquisition: Data mining — Extract as much information as possible from massive electronic medical record data
2. Knowledge management: Graph/LLM — Construct patient graphs and knowledge graphs using patient information and related knowledge
3. Knowledge reasoning: Prediction/Generation/Recommendation — Conduct prediction, generation, and recommendation on graphs and large models
4. Knowledge engine: Search/Dialogue — User service and related retrieval and generation based on knowledge

### Research Outputs

#### Main Research: Large Models + Big Data + Natural Language Processing

Research on natural language processing technology for medical big data analysis and utilization (Doctoral thesis)

Responsible for topic selection, literature review, theoretical innovation, experiments, and paper writing

| **Named Entity Recognition in Electronic Medical Records** | Sub-topic | Note |
| --------------------------------------------------------- | --------- | ---- |
| **Paper** *Research on Deep Learning Models for Chinese Electronic Medical Record Named Entity Recognition* | Beijing Outstanding Thesis | |
| **Paper** [Research and Progress in Chinese Electronic Medical Record Named Entity Recognition](https://www.ejournal.org.cn/CN/abstract/abstract13029.shtml) | Peking University Core | Chinese Journal of Electronics |
| **Paper** [KrNER: A Novel Named Entity Recognition Method Based on Knowledge Enhancement and Remote Supervision](https://bt7cezha1x.feishu.cn/file/EwvobK1RXo6lxQxLp1FcNuuJnRd?from=from_copylink) | CCF-C | CSE2023 |

| **Medical Knowledge Graph Supporting Health Data Elements** | Sub-topic | Note |
| ---------------------------------------------------------- | --------- | ---- |
| **Paper** [KLDP: A Data Profiling Technique Based on Knowledge Graph and Large Language Modeling](https://bt7cezha1x.feishu.cn/file/CCuFboQc4okTn4xNpZJcsXqGngf?from=from_copylink) | CCF-C | CSE2023 |

| **Intelligent Healthcare Large Model Research Driven by Data and Knowledge** | Sub-topic | Code |
| ---------------------------------------------------------------------------- | --------- | ---- |
| **Report** *ChatGPT Created the AI Wave* | Microsoft Invitation | |
| **Paper** [AiMed: Artificial Intelligent Large Language Model for Medicine in China](https://ieeexplore.ieee.org/document/10803480) | IEEE | [AiMed](https://github.com/dujh22/AiMed) |
| **Paper** [ChatFUV: Chat Chain for Follow-Up Visit](https://bt7cezha1x.feishu.cn/file/ZAv6brkkpoupROxLY2NcxWdRnoe?from=from_copylink) | | |
| **System** AiMed Medical Knowledge Large Model Application Service System | Software Copyright | |
| **Paper** [MedRad: A Framework for Reliable Assisted Decision Making in a Medical Large Language Model](https://bt7cezha1x.feishu.cn/file/DqC4b1knBosvcrxpQ81cUcS9n8g?from=from_copylink) | | [MedRad](https://github.com/dujh22/MedRad) |
| **Paper** [Toward a Large Language Model-Driven Medical Knowledge Retrieval and QA System: Framework Design and Evaluation](https://doi.org/10.1016/j.eng.2025.02.010) | Engineering | |
| **Paper** [Towards Artificial Intelligence for Science: A Case Study of Using ChatGPT for Disease Causality Discovery from Biomedical Literature](https://ieeexplore.ieee.org/abstract/document/11373497) | SCI Q1 | |
| **Paper** [Large Language Models Driven Reliable Clinical Decision-Making: Framework and Application](https://www.sciencedirect.com/science/article/pii/S294995342500030X) | SCI Q3 | |
| **Paper** [NewMed: Large Language Modeling Technology Enables Full Process Digital Intelligence in Medical Care](https://bt7cezha1x.feishu.cn/file/LXRyboPqzo9OmZxGleEcpa0PnSh?from=from_copylink) | | |
| **Paper** *Doctor: The Most Reliable Digital Intelligence Healthcare Large Language Model System* | | |
| **Paper** *MedLib: Research on the construction of a knowledge library for medical large language modeling* | | |

#### Participating Research: Medical Engineering + Network

Large models and blockchain (sub-topic)

Responsible for cross-disciplinary research, theoretical innovation, application deployment, and paper writing

| **Key Technologies for Trusted On-chain and Off-chain Data Interaction in Blockchain** | Vertical - Ministry of Science and Technology |
| --------------------------------------------------------------------------------------- | -------------------------------------------- |
| **Website** [Open Data Entry](https://www.opende.org.cn/) | Public Service |
| **Paper** [Med-Eval: Blockchain Assessment Platform for Medical Large Language Model](https://bt7cezha1x.feishu.cn/file/Rua0bq3DRo53EyxMC96civ5cnZe?from=from_copylink) | |
| **Paper** *OpenMonet: Open Model Orchestration Network* | |

Intelligent healthcare of the new generation emerging from digital intelligence (sub-topic)

Responsible for cross-disciplinary research, scenario innovation, application deployment, and paper writing

| **Clinical Comprehensive Assessment Management and Early Warning System for Elderly Renal Function Decline** | Vertical - Ministry of Science and Technology |
| ----------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **Paper** [Research of Client Selection Algorithm in Cross-device Federated Learning](https://www.jos.org.cn/josen/article/abstract/nb023) | Peking University Core |
| Medical data annotation **system**, Chinese word segmentation **system**, disease prediction **system** (1000+ diseases), intelligent self-diagnosis **system** | Related Services |

## Coursework

All project code is open-sourced on GitHub (continuously updated)

| Type | Specific Area | Main Skills | Related Outputs |
| ---- | ------------- | ----------- | --------------- |
| Machine Learning | Advanced Machine Learning (A) | ML | MedRad: A Reliable Assisted Decision Making Framework for Medical LLMs<br />RAG-NEWS: Using RAG to Help LLMs Access Latest News [[Code](https://github.com/dujh22/RAG-NEWS)] |
| | Digital Intelligence Security and Standardization (A) | Tech Law | AI Algorithm Transparency Implementation and Evaluation—Taking Recommendation Systems as Example |
| | Computational Linguistics (A) | NLP-Base | Fine-tuning Chinese Pre-trained Models for Text Classification |
| | Frontiers of Information Retrieval (A) | IR | Intelligent Medical Search Engine for Multi-source Heterogeneous Health Big Data |
| | Big Data Analysis and Processing (A) | Big Data Analysis | Multimodal Dialogue Scenarios and Topic Switching Understanding |
| | Data Mining: Principles and Algorithms | Data Mining | Online News Popularity Prediction<br />Clustering Analysis of Diabetic Patient Admission Data [[Code](https://github.com/dujh22/DM_ClusterAnalysisOfPatientData)] |
| | Knowledge Engineering | NLP-KG | Event Extraction Based on MAVEN Dataset<br />Cross-lingual Knowledge Graph |
| | Principles of Artificial Intelligence | AI | Machine Translation (Chinese-English) Based on Machine Learning<br />Reading Comprehension Based on Prior Knowledge [[Code](https://github.com/dujh22/KE_Knowledge-oriented_reading_comprehension)] |
| | Parallel Computing, Algorithm and Complexity Theory, Combinatorics | High-Performance Computing | Parallelization of Π Solving<br />Applications of Combinatorics in AI |
| Other | Related Skills | Comprehensive | Chinese Marxism and Contemporary (A), Dialectics of Nature (A), Big Data Analysis, Big Data and Biostatistics, Big Data Practice, Doctoral English (Exempted), Professional Capability Extension Training |

## Published Academic Works

[11] Zeng A, Lv X, Zheng Q, et al. [Glm-4.5: Agentic, reasoning, and coding (arc) foundation models](https://arxiv.org/abs/2508.06471)[J]. arXiv preprint arXiv:2508.06471, 2025. (Arxiv)

[10] Du J, Li X, Liu Y, et al. [Large language models driven reliable clinical decision-making: Framework and application](https://www.sciencedirect.com/science/article/pii/S294995342500030X)[J]. Informatics and Health, 2025. (SCI Q3, First Author)

[9] X. Li, J. Du, Y. Liu, H. Yin and H. Liu, "[Towards Artificial Intelligence for Science: A Case Study of Using ChatGPT for Disease Causality Discovery from Biomedical Literature](https://ieeexplore.ieee.org/abstract/document/11373497)," in Big Data Mining and Analytics, vol. 9, no. 2, pp. 554-562, April 2026, doi: 10.26599/BDMA.2025.9020086. (SCI Q1 *Big Data Mining and Analytics*, Co-first Author)

[8] Liu Y, Li X, Luo Y, et al. [Toward a Large Language Model-Driven Medical Knowledge Retrieval and QA System: Framework Design and Evaluation](https://doi.org/10.1016/j.eng.2025.02.010)[J]. Engineering, 2025. (SCI Q1 *Engineering*, Fourth Author)

[7] Hanyu Lai, Xiao Liu, Junjie Gao, Jiale Cheng, Zehan Qi, Yifan Xu, Shuntian Yao, Dan Zhang, Jinhua Du, Zhenyu Hou, Xin Lv, Minlie Huang, Yuxiao Dong, and Jie Tang. 2025. [A Survey of Post-Training Scaling in Large Language Models](https://aclanthology.org/2025.acl-long.140/). In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 2771–2791, Vienna, Austria. Association for Computational Linguistics. (CCF-A: ACL)

[6] J. Du, X. Li, Z. Jiang, Y. Liu, H. Yin and H. Liu, "[AiMed: Artificial Intelligent Large Language Model for Medicine in China](https://ieeexplore.ieee.org/document/10803480)," 2024 IEEE International Conference on Medical Artificial Intelligence (MedAI), Chongqing, China, 2024, pp. 360-365, doi: 10.1109/MedAI62885.2024.00054. (IEEE, First Author)

[5] Lü Tingyu, Li Xiaoying, Zhang Ying, Liu Yuyang, Du Jinhua, et al. [Research on Construction of Chinese Medical Knowledge Large Model Q&A Corpus Dataset](https://d.wanfangdata.com.cn/periodical/yxqbgz202405004)[J]. Journal of Medical Informatics, 2024, 45(5):20-25. DOI:10.3969/j.issn.1673-6036.2024.05.004. (Chinese Science and Technology Core Journal, Fifth Author)

[4] Zhang Ruilin, Du Jinhua, Yin Hao. [Research of Client Selection Algorithm in Cross-device Federated Learning](https://www.jos.org.cn/josen/article/abstract/nb023)[J]. Journal of Software. (CCF-A Recommended Chinese Science Journal, THU-B Journal, Peking University Core, Second Author)

[3] Jinhua Du and Hao Yin. KLDP: A Data Profiling Technique Based on Knowledge Graph and Large Language Modeling. 2023 IEEE 22nd International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom), 2023.11 (DOI 10.1109/TrustCom60117.2023.00329) (CCF-C International Conference, First Author)

[2] Du J, Yin H. [KrNER: A Novel Named Entity Recognition Method Based on Knowledge Enhancement and Remote Supervision](https://ieeexplore.ieee.org/abstract/document/10538843)[C]//2023 IEEE 22nd International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom). IEEE, 2023: 2323-2332. (CCF-C International Conference, First Author)

[1] Du Jinhua, Yin Hao, Feng Song. [Research and Progress in Chinese Electronic Medical Record Named Entity Recognition](https://www.ejournal.org.cn/CN/abstract/abstract13029.shtml)[J]. Chinese Journal of Electronics, 2022, 50(12): 3030-3053. (CCF-A Recommended Chinese Science Journal, THU-B Journal, Peking University Core, First Author)

## Unpublished Academic Works

[7-9] Under anonymous review

[6] Jinhua Du. ChatFUV: Chat Chain for Follow-Up Visit

[5] Jinhua Du. NewMed: Large Language Modeling Technology Enables Full Process Digital Intelligence in Medical Care

[4] Jinhua Du. Doctor: The Most Reliable Digital Intelligence Healthcare Large Language Model System

[3] Jinhua Du. OpenMonet: Open Model Orchestration Network

[2] Jinhua Du. Med-Eval: Benchmarks for the Medical Large Language Model

[1] Jinhua Du. MedLib: Research on the construction of a knowledge library for medical large language modeling

## Published Software Copyrights

[1] AiMed Medical Knowledge Large Model Application Service System — Software Copyright (2024.02.29). Service available at the Institute of Medical Information, Chinese Academy of Medical Sciences: [AiMed Medical Knowledge Large Model](http://aimed.imicams.ac.cn/#/) — Jointly developed by the Institute of Medical Information, Chinese Academy of Medical Sciences and Tsinghua University OpenDE team, providing medical knowledge Q&A and intelligent literature services for medical research and innovation.

## Media Coverage

[3] 2025 "Large Model Wild Goose Migration Plan" Initiator | [Year-end Review and Outlook: Journeying Together Toward a New Era](https://mp.weixin.qq.com/s/xNk6H0mLj7C6sqeaiSaUcQ)

[2] 2024 Outstanding Practice Individual | [Computer Science Du Jinhua: Iron Will, Pursuing Dreams in Public Security](https://mp.weixin.qq.com/s/RyUsmJ1ZuZ38XbXRmd3a8A)

[1] [3rd China Medical Informatics Discipline Development Conference](https://mp.weixin.qq.com/s/RDQUcnGLRciSwub1HuOh4Q) (2023.11.25) As first completer, AiMed large model was [released](https://bt7cezha1x.feishu.cn/wiki/Bu3YwOsyyixkswkYGS1cjbXPnMf?from=from_copylink). [GitHub code](https://github.com/dujh22/AiMed) and [Hugging Face parameters](https://huggingface.co/DuJinHua/AiMed) have been open-sourced. Corresponding paper [AiMed: Artificial Intelligent Large Language Model for Medicine in China](https://ieeexplore.ieee.org/document/10803480) was published at MedAI.

## Honors & Awards

| Category | Content | Unit | Date |
| -------- | ------- | ---- | ---- |
| Recognition | Outstanding Communist Youth League Member | Tsinghua University Communist Youth League Committee | 2025.10 |
| | Led class to Excellence Class & League (1st place), Paired Class & League | Tsinghua University | 2025.09 |
| | Outstanding Trainee in Social Work Seminar | Tsinghua University | 2025.04 |
| | Led class to Dedication Class & League | Tsinghua University Graduate Communist Youth League Committee | 2025.03 |
| | Outstanding Graduate Student Cadre | Tsinghua University Computer Science Department | 2024.06 |
| | Outstanding Department Member, Computer Science Graduate League | Tsinghua University Computer Science Department | 2023.05 |
| | Outstanding Department Member, Tanzhen Technology Department | Tsinghua University | 2022.12 |
| | Outstanding Trainee, Graduate New Student Cadre Training & League School | Tsinghua University Graduate Committee | 2022.08 |
| Awards | 2024 Journal of Software Highly Cited Researcher | Journal of Software Editorial Board | 2026.01 |
| | Tsinghua Friends - Hefei Elite Scholarship | Tsinghua University | 2025.12 |
| | Tsinghua University Ma Yuehan Cup Bodybuilding Competition 5th Place | Tsinghua University Student Bodybuilding Association | 2025.12 |
| | "Computing Future" Doctoral Forum Excellence Award (1st) | Tsinghua University Computer Science Department | 2025.10 |
| | Social Work Second Prize Scholarship | Tsinghua University | 2024.12 |
| | University Huiyan Elite Scholarship (Second Class) | Tsinghua University | 2024.12 |
| | Outstanding Social Practice Award | Tsinghua University | 2024.12 |
| | Social Practice Gold Award Team (2nd university-wide) | Tsinghua University Party Graduate Work Department | 2024.11 |
| | Beijing Challenge Cup Gold, National Challenge Cup Third | Beijing Communist Youth League Committee | 2024.09 |
| Thank-you Letters | Zhoushan City, Zhejiang | Zhoushan Municipal Talent Work Leading Group | 2024.09 |
| | Zhoushan Dinghai District Public Security Bureau | Public Security Bureau Cyber Security Team | 2024.09 |
| | Hangzhou High-tech Zone, Zhejiang | Human Resources Bureau | 2023.07 |

## Work Experience

| Category | Location | Position | Period |
| -------- | -------- | -------- | ------ |
| Lab | [Tsinghua University Knowledge Engineering Group (KEG)](https://keg.cs.tsinghua.edu.cn/) | Doctoral Student | 2024.02-present |
| Lab | Beijing National Research Center for Information Science and Technology — Big Data-driven Knowledge Management and Decision Team | Research Assistant | 2021.09-2024.02 |
| Internship | [Beijing Zhipu Huazhang Technology](https://zhipuai.cn/aboutus) — AI Institute | Intern | 2024.03-present |
| Internship | Zhoushan Dinghai District Public Security Bureau Cyber Security Team, Zhejiang | External Expert | 2024.07-2024.08 |
| Internship | Hunan Wangshu Technology | AI Algorithm Engineer | 2022.08 |
| Social Work | Tsinghua University Communist Youth League Practice Department — Platform Group | Team Leader | 2024.09-2025.03 |
| Social Work | Tsinghua University Computer Science Department — Class 53 | Class Assistant | 2024.09-present |
| Social Work | Tsinghua University Computer Science Department — Class 53 | Party Branch Secretary | 2024.09-present |
| Social Work | Tsinghua University Computer Science Department — Class 52 | League Branch Secretary | 2022.08-2023.09 |
| Social Work | Tsinghua University Computer Science Department Communist Youth League Practice Department | Secretary | 2023.05-2024.06 |
| Social Work | Tsinghua University Computer Science Department Communist Youth League Practice Department | Department Member | 2022.09-2023.05 |
| Social Work | Tsinghua University Tanzhen Technology Review Society Editorial Department | Staff: AI Community Lead | 2022.08-2023.08 |
| Social Work | Tsinghua University Graduate Student Union Sports Department | Staff | 2022.08-2023.08 |

- Served as course teaching assistant (AML & ML course — bilingual Chinese-English graduate course taught by Prof. Tang Jie). Tasks include: creating course materials, course design, assignment design, website, lectures, book writing, teaching, serving as session chair at two paper conferences, and maintaining contact with each student and guest for communication.
- Participated twice in Tsinghua think tank seminars and spoke as representative.
- Summer 2024: As team captain, led a six-week summer social practice in Zhoushan, Zhejiang. Successfully completed the "Crime Prediction Large Model Establishment" project at Dinghai District Public Security Bureau, applying public security big data to real-world needs. Organized cross-regional, cross-unit activities, demonstrating Tsinghua spirit of learning, practice, and responsibility. Received university Gold Award and high praise from both the Public Security Bureau and team members.
- Served as Computer Science Department Communist Youth League Practice Department core member. Responsible for: summer graduate social practice award materials review, press release writing, university-enterprise visit planning, liaison, and organization. **Published one article as first correspondent** on Tsinghua University News website; assisted with multiple practice announcements.
- Served as University Student Union Sports Department core member. Responsible for on-site promotional materials collection. **Participated and received 2022 Campus Marathon 10km medal, 2023 Campus Marathon half-marathon medal**.
- Served as University Tanzhen Technology Review Society Editorial Department core member. Responsible for **tech hotspot research and commentary** and **interviewing academicians** with press release writing. Handled weekly tech consultation work 6 times, corresponding to 6 published articles.
- **Served as Computer Science Department Graduate League Practice Vice Secretary**. Participated in all "Welcoming the 20th Congress, Industrial New Forces" seven-department joint industry visits. 2023.03.16 ByteDance OpenDay captain, liaison and publicity lead; 2023.04.13 Tencent OpenDay captain, liaison and publicity lead; 2023.04.24 Meituan OpenDay captain, liaison and publicity lead; 2023.04.27 Ninecube Investment OpenDay deputy captain; 2023.06.17 NetEase Youdao OpenDay captain, liaison and publicity lead; 2023.07.10-12 Hangzhou regional visit: 13 enterprises, captain, liaison and publicity lead. Total output: 1 report (50,000 words), 23 main articles.
- **Completed 2 social work courses and trainings**: 2022.09 Tsinghua University Doctoral Lecturer Corps "Liyan Plan" 6th Session (Fall); 2022.08 Tsinghua University 16th Graduate New Student Cadre Training & 37th League School (Graduate Class).
