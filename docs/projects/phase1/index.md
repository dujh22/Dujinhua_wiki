---
title: "阶段一：ChatGLM 数学推理与国际化"
hide:
  - navigation
---

# :material/calculator-variant-outline: 阶段一：ChatGLM 数学推理与国际化

!!! info "时间范围"
    2024.3 – 2024.6

[:material-arrow-left: 返回项目总览](../index.md) | [:material-home: 返回首页](../../index_zh.md)

---

## 报告列表

### [01. ChatGLM 数学推理](./01_ChatGLM数学推理.md)

> 本项目旨在通过**过程奖励模型（Process Reward Model, PRM）**与**PPO/RLHF**强化学习 pipeline，系统性提升 ChatGLM 系列大模型的数学推理能力。项目核心成果包括：（1）搭建"前向自动标注 + 后向评分反馈"的自动化数据标注 pipeline，历经 3 次系统性迭代，标注准确率约 80%（达人工标注水平），支持高并发达每小时万级标注，累计自动标注数...

---

### [02. ChatGLM 国际化](./02_ChatGLM国际化.md)

> 本项目旨在提升 ChatGLM 系列大模型的跨语种理解与表达能力，重点解决模型在面对**英文问题时返回中文回答**的"中英混杂"现象。项目核心成果包括：（1）搭建"**数据收集 → 数据预处理 → 有效数据生成 → 数据校验与合并**"的全流程数据 pipeline，清洗出 **5W 条**高质量中英混杂任务训练数据；（2）复现"**通过语言对齐将 LLM 英语能力外推到非英语语言**"算法（x-...

---

