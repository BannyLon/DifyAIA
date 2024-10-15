DifyAIA仓库-说明文档
==========
本仓库为B站：bannylon7相关Dify AI实战案例相关源码

解读Github项目智能机器人(analysis-Github-project)
---
为B战bannylon7发布的Dify AI实战案例教学视频：[(MAC)使用本地部署的Dify搭建 AI自动总结概括GitHub项目](https://www.bilibili.com/video/BV1eNtse9Epo) 的相关源码。<br><br>
这是一个解读Github项目的工作流，用户输入一个github项目的url，通过HTTP请求获取GitHub项目的README文件，并将README文件转换为纯文本，然后HTTP请求获取GitHub项目的README文件的完整结构，利用大语言模型对GitHub项目进行归纳总结，最后输出。这个工作流帮助用户快速了解Github项目。

#### 使用指南
1、下载analysis-Github-project到任意目录；<br>
2、在analysis-Github-project文件夹上右键单击，选择“服务——新建位于文件夹位置的终端窗口“；<br>
3、在打开的终端窗口中输入执行flask服务命令：`Python readme.py`<br>
4、运行dify，在dify中导入 解读Github项目智能机器人.yml DSL文件：在打开的工作流中修改LLM节点模型，以及修改HTTP请求节点的get请求的URL。<br>

![](https://github.com/BannyLon/DifyAIA/blob/main/analysis-Github-project/readmes/analysis-Github-project.png)

思维导图生成助手(Mindmap-generate-assistant)
---
为B战bannylon7发布的Dify AI实战案例教学视频：[Dify AI 教程：自动生成思维导图](https://www.bilibili.com/video/BV1qnsDeZErX)的相关源码。<br><br>
这是一个功能强大的Dify AI应用，它能够根据用户提供的参考内容，迅速一键生成思维导图。该应用的工作流程高度自动化：首先，通过HTTP请求节点配置一个精密的工作流，这个工作流负责将生成的Markdown内容发送到Flask服务，并将其发布为一个便捷的工具。随后，创建一个Agent应用，这个应用能够智能地通过工作流触发工具，进一步将Markdown内容发送到Flask服务。在Flask服务中，Markdown内容会被精心保存为一个.md文件。更为先进的是，该服务会调用Markmap工具，将Markdown文件巧妙地转化为交互式的HTML思维导图。最终，Flask服务会返回一个包含查看链接的JSON响应，用户只需轻松点击链接，即可直观地查看生成的思维导图文件。

#### 使用指南
1、下载Mindmap-generate-assistant到任意目录；<br>
2、在Mindmap-generate-assistant文件夹上右键单击，选择“服务——新建位于文件夹位置的终端窗口“；<br>
3、在打开的终端窗口中输入执行flask服务命令：`Python markmap.py`<br>
4、运行dify，在dify中导入 `思维导图生成助手mindmap_generator.yml` DSL文件：在打开的工作流中修改LLM节点模型，以及修改HTTP请求节点的get请求的URL。然后发布为工具。<br>
5、再次导入 `思维导图生成助手.yml` DSL文件，在打开的Agent更换模型，同时删除已调用的工具，再重新添加刚发布的工具。然后就可以直接运行操作了。

