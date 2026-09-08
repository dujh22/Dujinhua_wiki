# 集成指南

## 项目概述

本仓库为个人MkDocs网站，集成了智谱实习期间的30份项目报告。

## 技术栈

- MkDocs 1.6.1
- Material for MkDocs 9.7.1
- Mermaid 图表支持

## 目录结构

```
docs/
├── index_zh.md          # 首页
├── javascripts/
│   └── mermaid_init.js  # Mermaid初始化脚本
└── projects/            # 项目报告（37个文件）
    ├── index.md         # 项目总览
    ├── phase1/          # 阶段一：ChatGLM数学推理与国际化
    ├── phase2/          # 阶段二：多模态、元评估、助教等
    ├── phase3/          # 阶段三：逻辑推理、GLM-4.5等
    ├── phase4/          # 阶段四：综述、训练自进化等
    ├── phase5/          # 阶段五：过程级评测、GLM-5等
    └── tools/           # 工具类项目
```

## 本地开发

```bash
# 安装依赖
pip install mkdocs mkdocs-material

# 本地预览
mkdocs serve

# 构建
mkdocs build --clean
```

## 部署状态

| 项目 | 状态 |
|------|------|
| 最新部署时间 | 2026-09-08 19:40 CST |
| 部署状态 | ✅ 已部署到GitHub Pages |
| 访问地址 | https://dujh22.github.io/Dujinhua_wiki/ |
| 项目总览 | https://dujh22.github.io/Dujinhua_wiki/projects/ |
| master分支 | `1c18fa4` |
| gh-pages分支 | `05217c7` |

## 部署命令

```bash
# 提交更改
git add docs/projects/ docs/javascripts/ mkdocs.yml
git commit -m "集成智谱30份项目报告到MkDocs站点"
git push origin master

# 部署到GitHub Pages
mkdocs gh-deploy --force
```

## 部署记录

详细部署记录见 [DEPLOYMENT_RECORD.md](./DEPLOYMENT_RECORD.md)
