# miniapp-general-zh

面向中文小程序前端开发的通用技能包。

## 它是什么

这不是一个组件库，而是一套给 AI 和团队协作都能直接使用的小程序前端规范包。

它主要解决 7 类问题：
- 中文输出和中文文案统一
- 页面结构和信息层级统一
- 表单与反馈规则统一
- 语音交互和录音状态统一
- 组件边界和复用方式统一
- 小程序工程约束统一
- 风格方案与 design token 复用

这个技能包适用于：
- 微信小程序
- uni-app
- Taro
- 其他以小程序为主要运行环境的前端项目

它提供的不是某个平台专属配置，而是一套可跨项目复用的内容：
- 短入口文件
- 任务型核心规范
- 可直接复用的风格方案
- 可复制的 token 文件
- token 导出脚本

## 核心特性

- 中文优先：说明、注释、交互提示、错误文案默认使用中文
- 小程序优先：默认按移动端、小程序体验做设计和实现决策
- 渐进披露：`SKILL.md` 只放入口和读取路径，详细规则按任务读取
- 规范分层：`core` 负责稳定规则，`styles` 负责具体风格方案
- 风格可复用：内置一套暖色企业工具型方案
- token 可迁移：提供可复制的 CSS token，并可导出为 JSON 和 SCSS
- 平台中立：不绑定 OpenAI、Codex 或其他特定宿主平台

## 设计目标

这个技能包的目标是解决两类问题：

1. 当一个项目没有成熟规范时，提供一套可以直接落地的默认基线。
2. 当一个项目已有自己的体系时，提供一套更清晰的组织方式，帮助统一口径，而不是强行替换现有规范。

它默认强调：
- 中文
- 小程序优先
- 工具型产品优先
- 清楚、稳定、易维护
- 按任务读取，避免一次加载过多上下文

## 最小示例

如果你要为一个新的小程序项目建立统一规范，可以这样使用：

1. 先读 `SKILL.md`
2. 做整体基线时读 `references/core/overview.md`
3. 做页面结构时读 `references/core/page-flow.md`
4. 做表单和反馈时读 `references/core/form-and-feedback.md`
5. 做语音交互时读 `references/core/voice.md`
6. 做组件设计时读 `references/core/component-boundary.md`
7. 做语义 token 时读 `references/core/design-tokens.md`
8. 做按钮、卡片、表单项、吸底栏样式时读 `references/core/component-styles.md`
9. 中文文案优先读 `references/core/writing.md`
10. 做落地验收或代码评审时读 `references/core/acceptance.md`
11. 如果项目没有现成风格，直接复用 `references/styles/warm-enterprise.md`
12. 需要 token 时复制 `assets/tokens/warm-enterprise.css`

## 目录结构

```text
skills/
├── README.md
├── SKILL.md
├── references/
│   ├── core/
│   └── styles/
├── assets/
│   └── tokens/
└── scripts/
```

### 目录说明

- `README.md`
  给人看的说明文档，介绍技能包怎么用、目录怎么组织。

- `SKILL.md`
  给模型看的入口文件，定义这个技能包在什么场景下使用、如何读取内容、有哪些硬规则。

- `references/core/`
  存放按任务拆分的稳定规范，包括基线、页面结构、表单与反馈、语音交互、组件边界、语义 token、组件样式、文案规范、工程约束。

- `references/styles/`
  存放可直接复用的风格方案。后续新增不同风格时，优先放在这里。

- `assets/tokens/`
  存放可直接复制到项目中的 token 文件。

- `scripts/`
  存放辅助脚本，例如导出 token。

## 当前包含的内容

### 通用规范

- `references/core/overview.md`
- `references/core/page-flow.md`
- `references/core/form-and-feedback.md`
- `references/core/voice.md`
- `references/core/component-boundary.md`
- `references/core/design-tokens.md`
- `references/core/component-styles.md`
- `references/core/writing.md`
- `references/core/engineering.md`
- `references/core/acceptance.md`

### 风格方案

- `references/styles/warm-enterprise.md`

### Token 资产

- `assets/tokens/warm-enterprise.css`
- `assets/tokens/warm-enterprise-semantic.css`

### 脚本

- `scripts/export_tokens.py`
- `scripts/check_skill.py`

## 使用方式

## 1. 作为规范技能包使用

如果你在一个小程序项目里需要统一规范：

1. 先读 `SKILL.md`
2. 再按任务去读 `references/core/` 下对应文件
3. 落地后用 `references/core/acceptance.md` 做最小验收
4. 只在需要视觉方案时读 `references/styles/`
5. 只在需要直接落地 token 时读 `assets/tokens/`

## 2. 作为风格方案库使用

如果你想直接借用一套风格：

1. 读取 `references/styles/` 中对应方案
2. 复制 `assets/tokens/` 中对应 token 文件
3. 在目标项目中统一按钮、卡片、输入区和页面壳

## 3. 导出 token

执行：

```bash
python3 scripts/export_tokens.py assets/tokens/warm-enterprise.css
```

默认会在同目录导出：
- `warm-enterprise.json`
- `warm-enterprise.scss`

也可以指定输出目录：

```bash
python3 scripts/export_tokens.py assets/tokens/warm-enterprise.css --output-dir /tmp/out
```

## 检查 skill

执行：

```bash
python3 scripts/check_skill.py
```

默认会检查：
- Markdown 中引用的本地路径是否存在
- 核心规范文件是否带有自检段落
- token 导出脚本能否成功处理当前两份 token 文件

## 维护建议

### 新增通用规则时

优先判断它是不是长期稳定、跨项目通用：
- 如果是，放到 `references/core/`
- 如果不是，不要轻易塞进 core

优先按任务归档，而不是按抽象学科归档。
例如优先放进“表单与反馈”或“语音交互”，而不是继续堆进一个过大的“交互规范”。

### 新增风格时

优先放到 `references/styles/`，并为它配一份 token 文件。
如果需要 JSON 或 SCSS 格式，再使用 `scripts/export_tokens.py` 导出。

建议每个风格方案统一包含这些部分：
- 适用场景
- 风格关键词
- 视觉基线
- 页面结构
- 组件外观
- 交互偏好
- 文案口吻
- 不适用场景

### 控制文件体量

- `SKILL.md` 只保留入口信息和读取路径
- 单个 `core` 文件只覆盖一个任务域
- 当某个文件开始明显跨多个任务域时，再拆分
- 避免创建大量很小但边界模糊的文件

## 平台说明

这个仓库默认保持平台无关。

也就是说：
- 不内置 OpenAI、Codex 或其他特定平台的配置文件
- 不要求使用者依赖某个固定宿主系统

如果某个平台需要自己的附加配置，可以由使用者在外部自行添加。

## 为什么不是普通 prompt

普通 prompt 只能告诉模型“想要什么”，但很难长期稳定复用。

这个技能包把：
- 规则
- 风格
- token
- 输出语言
- 工程约束

拆成可持续维护的结构，更适合多项目复用和持续沉淀。

## 适合谁

适合以下人群：
- 想沉淀自己小程序设计与开发规范的人
- 有多个小程序项目，想统一风格和实现习惯的人
- 想把“风格方案 + token + 脚本”一起开源的人
- 想把技能包做成平台中立结构的人

## 不适合什么

这不是一个现成组件库，也不是完整设计系统。

它更适合做：
- 规范底座
- 风格方案库
- token 资产库
- 小型自动化工具包

而不是直接替代完整 UI 框架。
