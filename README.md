# miniapp-general-zh

面向中文小程序前端开发的通用技能包。

这个技能包适用于：
- 微信小程序
- uni-app
- Taro
- 其他以小程序为主要运行环境的前端项目

它提供的不是某个平台专属配置，而是一套可跨项目复用的内容：
- 中文输出规范
- 通用交互规范
- 组件设计规范
- 工程实现约束
- 可直接复用的风格方案
- 可复制的 token 文件
- token 导出脚本

## 设计目标

这个技能包的目标是解决两类问题：

1. 当一个项目没有成熟规范时，提供一套可以直接落地的默认基线。
2. 当一个项目已有自己的体系时，提供一套更清晰的组织方式，帮助统一口径，而不是强行替换现有规范。

它默认强调：
- 中文
- 小程序优先
- 工具型产品优先
- 清楚、稳定、易维护

## 目录结构

```text
miniprogram-skill/
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
  给模型看的说明文件，定义这个技能包在什么场景下使用、如何读取内容、有哪些硬规则。

- `references/core/`
  存放长期稳定的通用规范，包括基础规范、交互规范、组件规范、文案规范、工程约束。

- `references/styles/`
  存放可直接复用的风格方案。后续新增不同风格时，优先放在这里。

- `assets/tokens/`
  存放可直接复制到项目中的 token 文件。

- `scripts/`
  存放辅助脚本，例如导出 token。

## 当前包含的内容

### 通用规范

- `references/core/foundation.md`
- `references/core/interaction.md`
- `references/core/components.md`
- `references/core/writing.md`
- `references/core/engineering.md`

### 风格方案

- `references/styles/warm-enterprise.md`

### Token 资产

- `assets/tokens/warm-enterprise.css`

### 脚本

- `scripts/export_tokens.py`

## 使用方式

## 1. 作为规范技能包使用

如果你在一个小程序项目里需要统一规范：

1. 先读 `SKILL.md`
2. 再按任务去读 `references/core/` 下对应文件
3. 如果需要具体风格，再读 `references/styles/`
4. 如果需要直接落地 token，使用 `assets/tokens/` 中的文件

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

## 维护建议

### 新增通用规则时

优先判断它是不是长期稳定、跨项目通用：
- 如果是，放到 `references/core/`
- 如果不是，不要轻易塞进 core

### 新增风格时

优先放到 `references/styles/`，并为它配一份 token 文件。
如果需要 JSON 或 SCSS 格式，再使用 `scripts/export_tokens.py` 导出。

### 新增案例时

如果后续积累了多个真实项目案例，建议再新增一层：

```text
references/cases/
```

目前这套结构先保持 `core + styles`，避免过早拆得过细。

## 平台说明

这个仓库默认保持平台无关。

也就是说：
- 不内置 OpenAI、Codex 或其他特定平台的配置文件
- 不要求使用者依赖某个固定宿主系统

如果某个平台需要自己的附加配置，可以由使用者在外部自行添加。

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
