---
name: miniapp-general-zh
description: 当处理微信小程序、uni-app、Taro 等小程序前端任务时使用。覆盖中文输出、页面结构、表单与反馈、语音交互、组件边界、工程约束和可选风格方案。适用于新页面设计、组件重构、风格统一、中文文案规范、移动端体验优化和小程序前端代码评审。
---

# 中文小程序通用规范

这个 skill 面向通用小程序前端开发，不绑定具体业务仓库。
它的职责是给出默认做法，并把详细规则分散到少量任务型参考文件中，避免一次加载过多上下文。

## 适用场景

- 新建或修改小程序页面、组件
- 设计或重构表单、列表、详情页、设置页
- 统一中文文案、错误提示和反馈方式
- 处理语音输入、权限、录音态和处理中反馈
- 设计组件边界、页面模板和工程约束
- 为项目选择或复用一套小程序风格方案
- 做小程序前端代码评审，重点检查交互、文案、组件边界和一致性

## 跳过场景

- 当前项目已有成熟设计系统、成熟组件库或明确品牌规范时，不要强行覆盖
- 当前任务主要是后端、管理后台或非小程序场景时，不要把这里的移动端规则硬套进去
- 当前任务纯粹是接口、数据库、部署、运维脚本时，不需要使用这个 skill

## 硬规则

1. 默认使用中文输出，包括说明、注释、交互文案、错误提示和评审结论。
2. 只有代码标识符、接口字段、数据库字段、第三方固定参数和少量必要技术术语保留英文。
3. 永远按移动端优先、小程序优先来设计和实现。
4. 如果项目已有成熟规范，优先继承；本 skill 主要在“补齐缺失”和“统一口径”时发挥作用。
5. 不向用户暴露原始技术异常、接口路径、状态码原文、堆栈或底层调试信息。
6. 默认先统一页面结构、字段状态和反馈规则，再做局部视觉优化。

## 默认工作流

1. 先判断当前项目有没有现成规范。
2. 如果有，优先沿用现有规范，只补缺失项。
3. 如果没有，再按本 skill 的 `core` 规范落地。
4. 只在需要具体视觉方案时读取 `styles` 和 `tokens`。
5. 落地后按 `references/core/acceptance.md` 做最小验收。
6. 验收时优先检查：点击区、键盘、安全区、弱网、空态、错误态、重复点击。

## 任务读取路径

- 做整体基线和统一原则：读 `references/core/overview.md`
- 做页面结构和信息层级：读 `references/core/page-flow.md`
- 做表单、picker、错误反馈和提交态：读 `references/core/form-and-feedback.md`
- 做语音交互、权限和录音状态：读 `references/core/voice.md`
- 做组件边界和接口：读 `references/core/component-boundary.md`
- 做语义 token 和命名映射：读 `references/core/design-tokens.md`
- 做按钮、表单项、卡片、吸底栏等样式契约：读 `references/core/component-styles.md`
- 做中文文案和错误提示：读 `references/core/writing.md`
- 做工程实现和平台约束：读 `references/core/engineering.md`
- 做最小验收、自检和评审：读 `references/core/acceptance.md`
- 需要具体风格和 token：读 `references/styles/` 与 `assets/tokens/`

## 目录说明

- `references/core/`：按任务拆分的长期稳定规范
- `references/styles/`：可直接复用的风格方案
- `assets/tokens/`：可直接复制到项目里的 token 文件
- `scripts/`：辅助脚本

## 内置脚本

- `scripts/export_tokens.py`：把 CSS token 导出为 JSON 和 SCSS
- `scripts/check_skill.py`：检查引用路径、核心文档结构和 token 导出是否正常

## 明确禁止

- 把桌面端交互习惯原样搬到小程序端
- 把 hover 当成核心交互前提
- 用大量弹窗和多层确认替代清晰流程
- 明明项目已有规范，却绕开现有体系另起炉灶
- 把风格方案当成所有项目都必须使用的唯一答案
