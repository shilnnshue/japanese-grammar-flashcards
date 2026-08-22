<div align="center">

# 🇯🇵 日语 N1/N2 必备语法 368 句 · 闪卡

**把《笔记本日语1·2级必备语法368句》做成单文件 HTML 闪卡应用**  
完全离线 · 双击即用 · 带语音朗读

[![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://github.com/shilnnshue/japanese-grammar-flashcards)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://github.com/shilnnshue/japanese-grammar-flashcards)
[![Offline](https://img.shields.io/badge/Offline-Ready-green?style=flat-square)](https://github.com/shilnnshue/japanese-grammar-flashcards)

</div>

---

## ✨ 功能亮点

| 功能 | 说明 |
|------|------|
| **卡片正面** | 日文例句（大字）+ 中文翻译 + 语法提示（句型 / 接続） |
| **卡片背面** | 中文释义 + 接続公式 + 句型 |
| **语音朗读** | 点 🔊 或按 `S` 朗读；优先 Google 自然语音，离线自动回退 |
| **筛选 / 搜索** | 按级别（1级/2级）、分类、单元筛选，支持搜索句型或释义 |
| **记忆追踪** | `认识`(K) / `不认识`(J)，本地保存，可只刷「未掌握」 |
| **进度可视化** | 打乱 / 重置 / 进度条：认识 · 不认识 · 未学 · 完成度一目了然 |

---

## 📦 数据说明

源 Excel 只有 `句型 / 接続 / 释义` 三列，本身**没有例句**。  
本项目中的**例句由 AI 生成**（卡片内已标注「AI生成·请核对」），作为学习参考，考试前建议自行核对准确性。

---

## 📁 文件结构

| 文件 | 说明 |
|------|------|
| `日语语法闪卡.html` | **成品应用**（已内嵌全部 368 条数据，直接打开即可） |
| `grammar_data.json` | 从 Excel 提取的结构化数据 |
| `examples.json` | 每条句型对应的 AI 生成例句 |
| `finalize.py` | 合并数据并注入 HTML 的构建脚本 |

---

## 🚀 使用方法

**最简单的方式**：直接双击 `日语语法闪卡.html`（推荐 Chrome / Edge）。  
无需安装、无需联网（联网时语音更自然）。

```bash
git clone https://github.com/shilnnshue/japanese-grammar-flashcards.git
cd japanese-grammar-flashcards
# 打开 日语语法闪卡.html 即可
```

---

## ⌨️ 快捷键

- `S`：朗读当前例句
- `K`：标记「认识」
- `J`：标记「不认识」

---

<div align="center">

**Made with ❤️ by [石林雪](https://github.com/shilnnshue)**

如果觉得有用，欢迎给个 ⭐ Star！祝你日语学习顺利 🌸

</div>
