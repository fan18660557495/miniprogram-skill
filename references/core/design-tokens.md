# 语义 Token

这个文件定义小程序样式体系里从基础值到语义值的映射方式。

它的目标不是替代具体风格文件，而是防止页面和组件直接依赖原始色值、圆角和间距。

## 分层原则

推荐分为 4 层，最少先做 3 层：

1. 基础值  
颜色、圆角、间距、字号、阴影等原始值。

2. 语义值  
把基础值映射成有明确用途的名字，例如 `brand`、`text-primary`、`page-bg`。

3. 组件值  
把语义值继续映射到组件，例如 `button-primary-bg`、`card-border`、`form-item-label-color`。

4. 页面值  
只在页面壳、分区间距或特殊布局稳定存在时再补这一层。

如果项目规模还小，可以先做到“基础值 + 语义值”；当按钮、卡片、表单项开始反复出现时，再补组件值。

## 命名原则

- 先写用途，不先写颜色名
- 先写语义，不先写视觉形容词
- 名字应该能跨风格复用
- 一个 token 只表达一个稳定职责

推荐：

- `brand`
- `page-bg`
- `surface-card`
- `surface-soft`
- `text-primary`
- `text-secondary`
- `text-placeholder`
- `border-soft`
- `border-strong`
- `danger`
- `warning`
- `success`

不推荐：

- `orange-1`
- `main-orange`
- `light-gray-border`
- `white-card-bg`

## 颜色语义层

常见最小集合：

- 品牌主色：`brand`
- 页面背景：`page-bg`
- 卡片背景：`surface-card`
- 轻底色：`surface-soft`
- 主文本：`text-primary`
- 次文本：`text-secondary`
- 占位文本：`text-placeholder`
- 主按钮文字：`text-on-brand`
- 柔和边框：`border-soft`
- 强边框：`border-strong`
- 危险态：`danger`
- 警示态：`warning`
- 成功态：`success`

## 尺寸语义层

至少统一这些：

- `radius-sm`
- `radius-md`
- `radius-lg`
- `space-xs`
- `space-sm`
- `space-md`
- `space-lg`
- `height-input`
- `height-btn`
- `height-btn-lg`

如果项目里总在手写 `16px`、`20px`、`24px`，说明语义尺寸层还没立住。

## 状态语义层

除了正常态，至少给这些状态留清楚映射：

- 默认
- 激活
- 禁用
- loading
- 错误
- 警示
- 成功

状态层的重点不是多，而是稳定。
同一状态在不同组件里应尽量沿用同一套语义值来源。

## 落地规则

- 页面不要直接依赖原始色值
- 公共组件不要直接写裸十六进制色值
- 新风格优先替换语义映射，不优先大面积改组件代码
- 视觉方案先产出基础值，再产出语义映射

## warm-enterprise 建议映射

结合当前 `warm-enterprise.css`，建议按下面理解：

- `--color-brand` -> `brand`
- `--color-bg-page` -> `page-bg`
- `--color-bg-card` -> `surface-card`
- `--color-bg-soft` -> `surface-soft`
- `--color-text-primary` -> `text-primary`
- `--color-text-secondary` -> `text-secondary`
- `--color-text-placeholder` -> `text-placeholder`
- `--color-text-on-primary` -> `text-on-brand`
- `--color-border-soft` -> `border-soft`
- `--color-border-strong` -> `border-strong`
- `--color-danger` -> `danger`
- `--color-warning` -> `warning`
- `--color-success` -> `success`

如果后续需要更明确的主题切换或多品牌支持，可以再补一层 alias token 文件。

## 自检

- 页面和组件是否仍在直接写原始色值
- 颜色名是否写成了用途名
- 同一状态是否在不同组件里出现多套叫法
- 新风格切换时，是否只需要改语义映射而不是改大量页面代码
