<div align="center">

# Dify-Workflow-DSL-Examples 🚀 # Dify开源工作流示例库  
<strong>Open Collaboration | Workflow-as-Code | Empower Developers. 开放协作·流程即代码·赋能开发者</strong>


<a href="https://space.bilibili.com/3494355666995510/upload/video" target="_blank"><img src="https://github.com/BannyLon/DifyAIA/blob/main/Dify%20workflow/IME/112update.png" alt="B站bannylon7视频合集"/></a>

</div>

本仓库为B站 **bannylon7** UP主 设计制作的 **Dify工作流DSL开源示例库（Dify-Workflow-DSL-Examples）** ，这里开源的Dify工作流均是B站UP主 **bannylon7** 在学习Dify过程中构建的完整工作流示例，全部调试成功后才发布，但不保证随着dify版本升级以及大模型的选择使用而出现错误。所有示例均附带注释说明。欢迎通过Issue提交需求，也期待你的PR共同完善这个知识库！项目采用MIT开源协议，特别适合：

✅ 刚接触Dify的开发者快速上手
✅ 企业团队建立标准化流程规范
✅ 教学场景演示工作流设计原理
✅ 开源社区协作改进自动化方案


# VIP群（AIGC交流群）
我准备筹建一个AIGC交流群:专注于人工智能生成内容(AIGC)技术的交流和学习。
### 群友要求:
群友可以是开发者、内容生产者、创业者和学习者等。
### 群内交流:
1. 群内主要交流和探讨 AIGC相关领域的知识、技术和应用。
2. 分项讨论AIGC在实际场景中的落地应用，如Midjourney、ChatGPT、StableDiffusion等 AIGC产品的实际体验与应用场景;
3. 分项讨论AI绘画技术和工具，如Dalle2、SD、MJ、AIGC等、
4. 分项讨论大语言模型(LLM)的发展和应用落地，以及国内LLM的发展和市场研究。

### 社群福利:
1. 每日分享AIGC趋势!AIGC实战案例;
2. 不定时分享最新精选的 AIGC工具;
3. AI文本、图像、视频、音乐等工具等使用教程以及答疑;
4. 分享最新 AI技术论文;分项最新的AIGC报告!4.
5. 分享开源模型(图、文、视等)，只要你的硬盘足够大!

## 交流群的建立旨在促进AIGC技术的普及和应用。让更多人喜欢A1，爱上AI，利用 A...
![](https://github.com/BannyLon/DifyAIA/blob/main/Dify%20workflow/IME/202505221432.png?raw=true)



# DifyAIA仓库-工作流分储情况

## Excel_Flask_Dify（生成Excel数据表）
为B战bannylon7发布的Dify AI实战案例教学视频：[dify AI教程：Dify_Flask_Excel](https://www.bilibili.com/video/BV1WKkzYhEAM/) 相关源码。<br><br>
Excel_Flask_Dify是一款利用大语言模型生成内容，将内容写入excel数据表中。该功能涉及两大核心；其一如何创建并保存excel文件；其二如何动态写入数据表字段和字段条目。这次的教学实践只是我的一次小小尝试，希望能为大家打开一扇新的思路之门，起到抛砖引玉的作用哦！
<details>
<summary>Excel_Flask_Dify 使用指南</summary>

#### 使用指南
1、下载文件夹Excel_Flask_Dify到本地任意目录；<br>
2、在Excel_Flask_Dify文件夹上右键单击，选择“服务——新建位于文件夹位置的终端窗口“；<br>
3、在打开的终端命令窗口输入命令：cd Excel_flask_Service；然后执行启动flask服务命令：`python3 Excel_flask_Service.py`<br>
4、运行dify，在dify中导入 “Dify AI应用：Excel_Flask_Dify.yml” DSL文件，根据flask服务生成的链接地址对应修改http请求节点；然后执行即可。<br>
</details>

## DifyMarpFlask_PPT（生成PPT）
为B战bannylon7发布的Dify AI实战案例教学视频：[Dify AI 教程：DifyMarpFlask_PPT](https://www.bilibili.com/video/BV1CL6MYKEGd/) 相关源码。<br><br>
DifyMarpFlask_PPT是一款自动生成PPT的dify应用，希望对你的工作、学习有所帮助。
<details>
<summary>DifyMarpFlask_PPT 使用指南</summary>

#### 使用指南
1、下载文件夹DifyMarpFlask_PPT到本地任意目录；<br>
2、在DifyMarpFlask_PPT文件夹上右键单击，选择“服务——新建位于文件夹位置的终端窗口“；<br>
3、在打开的终端命令窗口输入命令：cd marp-flask-service；然后执行启动flask服务命令：`python3 marp-flask-service.py`<br>
4、运行dify，在dify中导入 “PPT生成工具.yml” DSL文件，根据flask服务生成的链接地址对应修改http请求节点；然后生成工具。<br>
5、最后导入 “PPT制作助手.yml” DSL文件，重新添加工具后即可执行操作。
</details>

## DifyWordBridg(生成Word文档)
为B战bannylon7发布的Dify AI实战案例教学视频：[（全网首创）Dify AI 教程：DifyWordBridg](https://www.bilibili.com/video/BV13vSuYyE9X/) 相关源码。<br><br>
DifyWordBridg是将Dify与Word结合。实现将大模型生成的内容一键生成Word文档
<details>
<summary>DifyWordBridg 使用指南</summary>

#### 使用指南
1、下载文件夹DifyWordBridg到本地任意目录；<br>
2、在DifyWordBridg文件夹上右键单击，选择“服务——新建位于文件夹位置的终端窗口“；<br>
3、在打开的终端窗口中输入执行启动flask服务命令：`Python3 Doc_flask_app.py`<br>
4、运行dify，在dify中导入 “Dify AI 应用：DifyWordBridg.yml” DSL文件：在打开的工作流中修改LLM节点模型，以及修改HTTP请求节点的post请求的URL。<br>
![](https://raw.githubusercontent.com/BannyLon/DifyAIA/refs/heads/main/DifyWordBridg/1732613793721.jpg)
</details>

## BillPic2Web(票据内容识别并将识别的票据内容用HTML页面展示)
为B战bannylon7发布的Dify AI实战案例教学视频：[(MAC)BillPic2Web—AI智读票据，它能够实现票据图片的自动解析并生成网页](https://www.bilibili.com/video/BV166DDYLE7n/) 的相关源码。<br><br>
BillPic2Web—AI智读票据，它能够实现票据图片的自动解析并生成网页。该AI应用支持用户上传票据图片并选定票据类型。系统首先校验用户所选类型与模型识别图片所得类型是否一致。若一致，应用将自动识别票据内容，并将其转化为可预览的HTML网页；若不一致，则提示用户确认类型后重试。简而言之，BillPic2Web能快速将票据图片转换成可视化的HTML页面，提升工作效率与便捷性。它集成了票据类型识别、内容提取及HTML生成等功能，旨在为用户提供全面的票据数字化解决方案。

#### 使用指南
1、下载文件夹bBillPic2Web到本地任意目录；<br>
2、在BillPic2Web文件夹上右键单击，选择“服务——新建位于文件夹位置的终端窗口“；<br>
3、在打开的终端窗口中输入执行flask服务命令：`Python invoice.py`<br>
4、运行dify，在dify中导入 “Dify AI 应用：BillPic2Web.yml” DSL文件：在打开的工作流中修改LLM节点模型，以及修改HTTP请求节点的get请求的URL。<br>
![](https://raw.githubusercontent.com/BannyLon/DifyAIA/refs/heads/main/BillPic2Web/1731242789983.jpg)


## 解读Github项目智能机器人(analysis-Github-project)
为B战bannylon7发布的Dify AI实战案例教学视频：[(MAC)使用本地部署的Dify搭建 AI自动总结概括GitHub项目](https://www.bilibili.com/video/BV1eNtse9Epo) 的相关源码。<br><br>
这是一个解读Github项目的工作流，用户输入一个github项目的url，通过HTTP请求获取GitHub项目的README文件，并将README文件转换为纯文本，然后HTTP请求获取GitHub项目的README文件的完整结构，利用大语言模型对GitHub项目进行归纳总结，最后输出。这个工作流帮助用户快速了解Github项目。

#### 使用指南
1、下载analysis-Github-project到任意目录；<br>
2、在analysis-Github-project文件夹上右键单击，选择“服务——新建位于文件夹位置的终端窗口“；<br>
3、在打开的终端窗口中输入执行flask服务命令：`Python readme.py`<br>
4、运行dify，在dify中导入 解读Github项目智能机器人.yml DSL文件：在打开的工作流中修改LLM节点模型，以及修改HTTP请求节点的get请求的URL。<br>

![](https://github.com/BannyLon/DifyAIA/blob/main/analysis-Github-project/readmes/analysis-Github-project.png)

## 思维导图生成助手(Mindmap-generate-assistant)
为B战bannylon7发布的Dify AI实战案例教学视频：[Dify AI 教程：自动生成思维导图](https://www.bilibili.com/video/BV1qnsDeZErX)的相关源码。<br><br>
这是一个功能强大的Dify AI应用，它能够根据用户提供的参考内容，迅速一键生成思维导图。该应用的工作流程高度自动化：首先，通过HTTP请求节点配置一个精密的工作流，这个工作流负责将生成的Markdown内容发送到Flask服务，并将其发布为一个便捷的工具。随后，创建一个Agent应用，这个应用能够智能地通过工作流触发工具，进一步将Markdown内容发送到Flask服务。在Flask服务中，Markdown内容会被精心保存为一个.md文件。更为先进的是，该服务会调用Markmap工具，将Markdown文件巧妙地转化为交互式的HTML思维导图。最终，Flask服务会返回一个包含查看链接的JSON响应，用户只需轻松点击链接，即可直观地查看生成的思维导图文件。

#### 使用指南
1、下载Mindmap-generate-assistant到任意目录；<br>
2、在Mindmap-generate-assistant文件夹上右键单击，选择“服务——新建位于文件夹位置的终端窗口“；<br>
3、在打开的终端窗口中输入执行flask服务命令：`Python markmap.py`<br>
4、运行dify，在dify中导入 `思维导图生成助手mindmap_generator.yml` DSL文件：在打开的工作流中修改LLM节点模型，以及修改HTTP请求节点的get请求的URL。然后发布为工具。<br>
5、再次导入 `思维导图生成助手.yml` DSL文件，在打开的Agent更换模型，同时删除已调用的工具，再重新添加刚发布的工具。然后就可以直接运行操作了。


# Dify workflow(Dify精选工作流)

DifyAIA库中的 **【Dify workflow】文件夹** 存储我精心整理的所有与学习相关的Dify工作流。我会不定期进行更新，确保你能找到所需的工作流。

## 2025年8月5日更新
| 文件名称 | 文件描述 |文件图示 |
| :-------------: | :----------: | :------------: |
| [智票通 - 批量发票智能解析.yml]|   「智票通 - 全时发票智能录入与飞书同步」 是一款专为财务人员设计的智能发票处理助手，深度融合多模态大模型与飞书电子表格自动化能力，支持在多轮对话中随时上传发票图片，并自动完成信息识别、结构化提取与云端归档。本功能特别适用于报销初审、费用归集、进项管理等高频、分散的发票处理场景，真正实现“拍一拍、传一传、自动记账”的极简财务体验。！  |![](./Dify%20workflow/IME/20250805150738.png?raw=true)|
| [票录精灵.yml]|   「本工作流主要是为财务工作人员提供一种识别电子发票（图片）信息，并自动录入飞书多维表格！  |![](./Dify%20workflow/IME/20250805151147.png?raw=true)|

</br>

## 2025年8月4日更新
| 文件名称 | 文件描述 |文件图示 |
| :-------------: | :----------: | :------------: |
| [PDF翻译Agent.yml]|   它通过集成 MCP 服务（调用大神开发的pdftranslate2 mcp），简化了与外部工具的集成过程，提高了工作流的可重用性和系统的稳定性，为 PDF 文档翻译等特定任务提供了强大、便捷的解决方案。只需上传您的文件并指定目标语言，我将自动为您处理翻译，并尽最大努力保留原始文档的格式与排版。！  |![](./Dify%20workflow/IME/20250805151732.png?raw=true)|
| [架构魔法师.yml]|   一键生成系统架构图！  |![](./Dify%20workflow/IME/20250805151923.png?raw=true)|

</br>

## 2025年7月21日更新
| 文件名称 | 文件描述 |文件图示 |
| :-------------: | :----------: | :------------: |
| [Zapier MCP test.yml](https://www.bilibili.com/video/BV1hjgNzVEBU/)|   用Zapier MCP + Gmail 实现自动发邮件！手把手带你三步配置专属Zapier MCP服务器，无缝调用Gmail“Send Email”，体验AI“动手”执行的魔力！  |![](./Dify%20workflow/IME/20250721202457.png?raw=true)|
</br>
## 2025年6月21日更新
| 文件名称 | 文件描述 |文件图示 |
| :-------------: | :----------: | :------------: |
| [实时热点新闻聚合引擎（每日简报版）.yml]|   这是「实时热点新闻聚合引擎」的官方升级版。它不仅继承了实时抓取并聚合哔哩哔哩、微博、抖音等八大主流平台热点榜单的核心能力，更实现了智能化的主动服务。工作流将经过AI清洗与结构化处理后的高价值新闻摘要，自动生成一份「每日热点简报」，并准时投递至您的指定邮箱。从“主动搜索”到“自动查收”，让您以最高效、最从容的方式，5秒掌握全网焦点，真正实现“信息找人”。  |![](./Dify%20workflow/IME/20250621175555.png?raw=true)|
| [实时热点新闻聚合引擎（聚合八大平台）.yml]|   本工作流深度集成 Rookie RSS 插件，实时抓取并聚合 8 大主流平台（哔哩哔哩、微博、抖音、知乎、百度、36氪、少数派、IT之家）的热点榜单，形成跨领域全景式热点图谱。通过智能清洗与结构化处理，自动输出高价值新闻摘要，帮助用户 5 秒掌握全网焦点。  |![](./Dify%20workflow/IME/20250620205437.png?raw=true)|

## 2025年6月12日更新
| 文件名称 | 文件描述 |文件图示 |
| :-------------: | :----------: | :------------: |
| [文生视频.yml]|   利用开源工具（doubao-image-and-video-generator）创建的文生视频，同理，可以创建图片生成视频。https://github.com/AllenWriter/doubao-image-and-video-generator   |![](./Dify%20workflow/IME/20250612090956.png?raw=true)|
| [文思泉涌.yml]|   “文思泉涌”是一款基于 LLM 协同创作理念打造的自动化长文案生产工作流。它将复杂的写作任务解构为“策略规划、分段精撰、整合润色”三大核心步骤，模拟专业内容团队的协作模式。通过“大纲生成器”精准构筑文章骨架，再由“章节迭代器”并行处理各部分细节，最后经“总编辑”模块赋予全文灵魂。无论是深度行业报告、营销白皮书还是万字博客，文思泉涌都能高效、稳定地输出逻辑严谨、结构清晰、风格统一的高质量内容，将您的灵感瞬间化为杰作。   |![](./Dify%20workflow/IME/20250612091520.png?raw=true)|


| 文件名称 | 文件描述 |文件图示 |
| :-------------: | :----------: | :------------: |
| [智能合同卫士.yml]|   智能合同卫士是AI驱动的智能合同审查与生成系统，它能自动扫描合同法律风险，优化条款以最大化主体利益。系统支持生成带修订批注的Word和PDF文件。   |![](./Dify%20workflow/IME/20250515134528.png?raw=true)|
| [智学规划师（Smart Study Planner）.yml]|   智能化地帮助你规划学习路径。   |![](./Dify%20workflow/IME/20250423140354.png?raw=true)|
| [知识图解（KnowGraph）.yml]|   知识图解（KnowGraph） 是一款集 知识提取、智能总结、思维导图可视化 于一体的高效工具。用户仅需输入网页链接或上传文件（文档/图片），系统即可自动解析内容，精准提炼关键信息，并以直观的思维导图形式呈现。它让碎片化信息结构化、可视化，使知识获取更高效便捷，适用于学习研究、报告整理、商业分析等多种场景，让您的信息管理更智能、更清晰！  |![](./Dify%20workflow/IME/20250423140340.png?raw=true)|
| [智筛简历.yml](https://www.bilibili.com/video/BV1mudrYVER1/#reply259480632001)|   “智筛简历”智能体采用多维度、全面且细致的评分方式，为 HR 提供了高效精准的筛选体系。HR 无需再耗费大量时间手动筛选，只需参考智能体的评分结果，即可快速锁定最优简历，大幅提升工作效率，从繁琐的筛选中解放出来，专注于更具战略价值的人力资源管理。  |![](./Dify%20workflow/IME/zhixuanjianli.png?raw=true)|
| [出题组卷.yml](https://www.bilibili.com/video/BV1mudrYVER1/#reply259480632001) |   "出题组卷"是一款AI驱动的教学辅助智能体，专注将教案内容智能转化为结构化的测评试卷。教师可自定义题型配比（判断/单选/填空），系统自动解析教材重点生成双版本试卷：含标准答案的教师版与纯净试题的学生版，实现教学测评全流程智能化。  |![](./Dify%20workflow/IME/chutizujuan.png?raw=true)|
| [链文智译-LinkTrans Smart.yml] |   链文智译是一款基于大型语言模型的智能助手，其核心功能是通过提交网页链接即可自动获取网页内容并智能翻译为高质量的中文。  |![](./Dify%20workflow/IME/zl41889FY.png?raw=true)|
| [获取金融投资新闻top10.yml] |   运用大模型抓取 两个信息源（the daily upside 和 Edward Jones）的新闻原始数据，进行分析和理解，并进行总结。《The Daily Upside》‌是一个专注于金融顾问新闻、市场洞察和投资策略的媒体平台（https://www.thedailyupside.com/）；Edward Jones是一家总部位于美国的金融服务公司，专注于为个人投资者提供投资管理、财务咨询服务等。（https://www.edwardjones.com/）   |![](./Dify%20workflow/IME/1739502431373.jpg?raw=true)|
| [词汇故事生成器.yml] |   输入一个词汇，自动生成一个短篇故事并配上 AI 生成的插图，工作流用到的生图节点是comfyui，因为我本地部署的有comfyui，就比较方便，如果你没有，你可以选择其它生图节点！   |![](./Dify%20workflow/IME/1736135410314.jpg?raw=true)|
| [RedCanvas.yml](https://www.bilibili.com/video/BV1jTyeYGE8q/) |   一键生成吸引眼球的小红书文案和配图，让您的每篇内容都成为焦点！   |![](./Dify%20workflow/IME/RedCanvas.jpg?raw=true)|
| [Twitter 账号分析助手.yml](https://www.bilibili.com/video/BV1Vw2QY4Ezf/)        |    根据用户提供的Twitter账户ID，利用HTTP请求和外部爬虫工具来抓取该ID的推文内容，并使用先进的LLM（Large Language Model，大型语言模型）技术对抓取到的社交平台数据进行深度分析。最终，我们将基于分析结果，模拟该用户的写作风格，撰写出符合我们要求的推文内容。     |        ![](./Dify%20workflow/IME/Twitter.jpg?raw=true) |
| [知识库图像检索与展示.yml](https://www.bilibili.com/video/BV1zexgeDEMe/)        |    通过知识检索从知识库中检索出带有图片链接的内容，然后借助HTTP请求节点将图片链接显示出来，实现一个直观且吸引人的图文结合客服交互场景，为用户带来更加生动、便捷的沟通体验。     |        ![](./Dify%20workflow/IME/1729836804207.jpg?raw=true) |
| [知识全网搜索.yml](https://www.bilibili.com/video/BV1BhtCeUEye/)        |    根据用户提问，利用Exa.ai搜索引擎搜索相关网页内容，然后对网页内容进行摘要，最后以一种便于阅读的的格式排版输出。妈妈再也不用担心我的学习，想学哪里搜哪里。     |        ![](./Dify%20workflow/IME/1729837233247.jpg?raw=true) |
| [资讯推送应用.yml](https://www.bilibili.com/video/BV1XsxneqE96/)       |    从号称程序员圈的"微博"的 Hacker News 获取最佳的文章资讯，并将整理后的资讯推送到企业微信群中。     |        ![](./Dify%20workflow/IME/1729837393352.jpg?raw=true) |
| [解析网页内容存到知识库.yml](https://www.bilibili.com/video/BV1CkxXeLEnn/?spm_id_from=333.1387.collection.video_card.click&vd_source=19b174391bdaac16c3008a0ce3bb38c9)      |    利用Jina Reader从指定URL提取核心内容，借助大语言模型（LLM）将这些内容转化为清晰、易管理的文本内容，最后通过知识库API，将精炼后的文档上传至指定的ID知识库中。这一流程将极大地促进我们未来在构建检索增强生成模型（RAG）方面的工作。     |        ![](./Dify%20workflow/IME/1729837328598.jpg?raw=true) |
| [dify AI 教程：图文智控链.yml](https://www.bilibili.com/video/BV1JiyXYNE2g/)      |    图文智控链是一款基于人工智能技术的智能工作流工具。它能够智能识别用户上传的图片和文档，并根据内容的不同进行灵活处理。无论是纯图片、纯文档还是图文混合的内容，该工作流都能迅速判断并启动相应的处理模式。通过精准的图片解读和文档总结功能，该工作流能够帮助用户快速获取所需信息，提高工作效率。     |        ![](./Dify%20workflow/IME/1729845555795.jpg?raw=true) |
| [Dify AI 教程：ChatWithPaper .yml](https://www.bilibili.com/video/BV1CCSUYrExd/)     |    AI - ChatWithPaper 是由 Dify 开发的学术论文对话助手。它基于预先提供的论文摘要、方法论分析和评估来回答用户关于特定论文的问题。它能像该领域的资深学者一样，与对研究感兴趣的读者进行专业交流。当涉及知识局限性时， AI - ChatWithPaper会及时告知用户。     |        ![](./Dify%20workflow/IME/1730695240344.jpg?raw=true) |
| [Dify AI 应用：Save To Notion.yml](https://www.bilibili.com/video/BV1BaUuYXEde/)     |    复刻“Save to Notion”这个扩展的功能，教大家如何在dify上搭建一个“一键将网页内容保存至Notion”的工作流。     |        ![](./Dify%20workflow/IME/1732612780877.jpg?raw=true) |
| [Dify_AI应用：News_Hot_List_36氪.yml](https://www.bilibili.com/video/BV1R5U6YvEZB/)     |    一键获取36氪平台的热榜精华文章     |        ![](./Dify%20workflow/IME/1732613122342.jpg?raw=true) |
| [儿童故事播客.yml](https://www.bilibili.com/video/BV1xPioYPEJB/)     |    运用先进的大语言模型，根据用户需求定制生成精彩的儿童故事内容；随后，利用Audio工具将故事转化为生动的语音；同时，借助ComfyUI工具，还会为播客创作一张吸引人的主题图片。     |        ![](./Dify%20workflow/IME/1733996694245.jpg?raw=true) |


<br><br><br><br><br><br>


👨‍💼 作者：BannyLon7<br>
💚 微信：banny-pan<br>
🗨 微信公众号：嗯哌<br>
🌍网站: https://www.agidt.com/<br>
&emsp;&emsp;&emsp;&emsp;https://www.npie.net/
