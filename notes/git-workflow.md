# Git 工作流备忘

## 每次写完代码 4 步

```bash
git status                     # 看改了什么（可选）
git add .                      # 打包所有改动
git commit -m "写清楚这次改了什么"   # 拍快照 + 贴标签
git push                       # 上传 GitHub
```

## 命令含义

| 命令 | 含义 | 类比 |
|------|------|------|
| `git status` | 查看哪些文件改动了 | 检查作业本 |
| `git add .` | 把所有改动打包 | 放书包里 |
| `git commit -m "..."` | 存档并写说明标签 | 贴便签"今天写了啥" |
| `git push` | 上传到 GitHub 云端 | 复印一份存保险柜 |

## commit 消息规范

格式：`什么地方: 做了什么`

| ❌ 差 | ✅ 好 |
|-------|------|
| `update` | `week1: add calculator with error handling` |
| `fix` | `week3: fix missing value in Titanic EDA` |
| `代码` | `ml: train random forest on house prices` |

## 不要做的事

- 不要攒一周才 push，写完一个小功能就 push
- 不要在 commit 里写中文（终端可能乱码）
- 不要用 `git push --force`，除非你知道自己在干什么
