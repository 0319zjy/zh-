import streamlit as st
import pandas as pd
import time
from datetime import timedelta

# ========== 页面配置 ==========
st.set_page_config(
    page_title="多功能应用中心（侧边目录版）",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"  # 侧边目录默认展开
)

# ========== 自定义CSS样式 ==========
st.markdown("""
<style>
    /* 主页面样式 */
    .main { background-color: #f0f2f6; }
    
    /* 侧边目录样式 */
    .css-1d391kg { background-color: #2c3e50; color: white; }
    .css-1d391kg .stRadio > label { color: white; }
    .css-1d391kg .stRadio [role="radio"] + div { color: white; }
    
    /* 卡片样式 */
    .stContainer {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    /* 按钮样式 */
    .stButton > button {
        border-radius: 8px;
        height: 3em;
        font-size: 14px;
        width: 100%;
        background-color: #3498db;
        color: white;
        border: none;
    }
    .stButton > button:hover {
        background-color: #2980b9;
    }
    
    /* 侧边栏标题样式 */
    .css-1d391kg h1 { color: white; font-size: 1.8rem; }
    .css-1d391kg h2 { color: white; font-size: 1.4rem; margin-top: 1rem; }
    .css-1d391kg hr { border-color: #4a6fa5; }
</style>
""", unsafe_allow_html=True)

# ========== 初始化会话状态 ==========
if "main_menu" not in st.session_state:
    st.session_state.main_menu = "首页概览"  # 默认选中首页
if "sub_menu" not in st.session_state:
    st.session_state.sub_menu = ""  # 子菜单默认空
if "rerun_trigger" not in st.session_state:
    st.session_state.rerun_trigger = False  # 重渲染触发器

# ========== 侧边目录导航（核心：层级目录结构 + 即时刷新） ==========
with st.sidebar:
    # 系统标题
    st.title("🔗 应用中心目录")
    st.markdown("---")
    
    # 主目录（一级菜单）
    st.markdown("### 📚 主功能目录")
    new_main_menu = st.radio(
        "选择主功能",
        ["首页概览", "学习工具", "娱乐中心", "生活服务", "系统设置"],
        index=["首页概览", "学习工具", "娱乐中心", "生活服务", "系统设置"].index(st.session_state.main_menu),
        label_visibility="collapsed"  # 隐藏默认标签
    )
    
    # 检测主菜单变化，更新状态并强制刷新
    if new_main_menu != st.session_state.main_menu:
        st.session_state.main_menu = new_main_menu
        st.session_state.sub_menu = ""  # 切换主菜单时清空子菜单
        st.rerun()  # 关键：强制页面即时刷新
    
    st.markdown("---")
    
    # 子菜单（二级菜单，根据主目录动态显示）
    new_sub_menu = ""
    if st.session_state.main_menu == "学习工具":
        st.markdown("### 📝 学习子功能")
        new_sub_menu = st.radio(
            "选择学习功能",
            ["书籍档案", "简历生成"],
            label_visibility="collapsed"
        )
    elif st.session_state.main_menu == "娱乐中心":
        st.markdown("### 🎨 娱乐子功能")
        new_sub_menu = st.radio(
            "选择娱乐功能",
            ["视频中心", "音乐播放器"],
            label_visibility="collapsed"
        )
    elif st.session_state.main_menu == "生活服务":
        st.markdown("### 🌿 生活子功能")
        new_sub_menu = st.radio(
            "选择生活功能",
            ["旅游探索"],
            label_visibility="collapsed"
        )
    elif st.session_state.main_menu == "系统设置":
        st.markdown("### ⚙️ 设置选项")
        new_sub_menu = st.radio(
            "选择设置项",
            ["账户管理", "主题设置", "关于系统"],
            label_visibility="collapsed"
        )
    
    # 检测子菜单变化，更新状态并强制刷新
    if new_sub_menu and new_sub_menu != st.session_state.sub_menu:
        st.session_state.sub_menu = new_sub_menu
        st.rerun()  # 关键：强制页面即时刷新
    
    # 系统状态信息
    st.markdown("---")
    st.markdown("### 📊 系统状态")
    st.metric("当前用户", "访客", delta_color="off")
    st.metric("在线时间", "2小时15分", delta_color="off")

# ========== 页面内容渲染逻辑 ==========
# 组合当前选中的功能（主菜单+子菜单）
current_func = f"{st.session_state.main_menu}-{st.session_state.sub_menu}".strip("-")

# ========== 1. 首页概览 ==========
if current_func == "首页概览":
    st.title("🏠 应用中心首页")
    st.markdown("欢迎使用多功能应用中心！通过左侧层级目录选择您想要使用的功能模块。")
    
    # 功能分类卡片
    st.markdown("### 📋 功能分类导航")
    col1, col2, col3 = st.columns(3)
    
    # 学习工具卡片
    with col1:
        with st.container():
            st.subheader("📚 学习工具")
            st.markdown("• 书籍档案（阅读管理）")
            st.markdown("• 简历生成（求职必备）")
            if st.button("进入学习工具", key="study_btn"):
                st.session_state.main_menu = "学习工具"
                st.rerun()  # 按钮点击后即时刷新
    
    # 娱乐中心卡片
    with col2:
        with st.container():
            st.subheader("🎨 娱乐中心")
            st.markdown("• 视频中心（影视观看）")
            st.markdown("• 音乐播放器（休闲听歌）")
            if st.button("进入娱乐中心", key="entertain_btn"):
                st.session_state.main_menu = "娱乐中心"
                st.rerun()  # 按钮点击后即时刷新
    
    # 生活服务卡片
    with col3:
        with st.container():
            st.subheader("🌿 生活服务")
            st.markdown("• 旅游探索（景点推荐）")
            st.markdown("• 更多功能持续更新...")
            if st.button("进入生活服务", key="life_btn"):
                st.session_state.main_menu = "生活服务"
                st.rerun()  # 按钮点击后即时刷新

# ========== 2. 学习工具 - 书籍档案 ==========
elif current_func == "学习工具-书籍档案":
    st.title("📚 书籍《Python编程：从入门到实践》数字档案")
    
    # 1. 书籍基础信息模块
    with st.container():
        st.subheader("📌 基础信息")
        col1, col2 = st.columns(2)
        with col1:
            st.info("""
            **书籍ID**：BOOK-2023-007  
            **出版时间**：2023-01-15  
            **书籍状态**：在架
            """)
        with col2:
            st.info("""
            **标签**：Python入门 | 编程经典  
            **作者**：埃里克·马瑟斯  
            **出版社**：人民邮电出版社
            """)
    
    # 2. 书籍评分矩阵模块
    with st.container():
        st.subheader("📊 评分矩阵")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("豆瓣评分", "9.1", "+0.2")
        with col2:
            st.metric("知乎评分", "9.3", "0")
        with col3:
            st.metric("Goodreads", "4.7/5", "-0.1")
        with col4:
            st.metric("专业评测", "95/100", "+3")
    
    # 3. 阅读进度模块
    with st.container():
        st.subheader("📖 阅读进度")
        st.progress(72)
        st.caption("当前进度：第12章 - 12.3 项目实战 - Web应用开发")
    
    # 4. 章节任务日志
    with st.container():
        st.subheader("📋 章节学习任务")
        chapter_tasks = [
            {"日期": "2025-12-01", "章节": "第1章：初识Python", "状态": "✅ 完成", "难度": "⭐☆☆☆☆"},
            {"日期": "2025-12-05", "章节": "第6章：字典与集合", "状态": "✅ 完成", "难度": "⭐⭐☆☆☆"},
            {"日期": "2025-12-10", "章节": "第12章：Web应用开发", "状态": "🔄 进行中", "难度": "⭐⭐⭐☆☆"},
            {"日期": "2025-12-18", "章节": "第15章：数据可视化", "状态": "❌ 未开始", "难度": "⭐⭐⭐⭐☆"}
        ]
        st.dataframe(chapter_tasks, use_container_width=True)

# ========== 3. 学习工具 - 简历生成 ==========
elif current_func == "学习工具-简历生成":
    st.title("📄 个人简历生成器")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("📝 个人信息")
        name = st.text_input("姓名", "张三")
        gender = st.radio("性别", ["男", "女"], horizontal=True)
        phone = st.text_input("手机号", "13800138000")
        email = st.text_input("邮箱", "zhangsan@email.com")
        
        skills = st.multiselect(
            "技能选择",
            ["Python", "Java", "JavaScript", "SQL", "HTML/CSS", "React", "Vue"],
            default=["Python", "SQL"]
        )
    
    with col2:
        st.subheader("📄 简历预览")
        st.markdown(f"### {name}")
        st.write(f"**联系电话**：{phone} | **邮箱**：{email}")
        st.write(f"**性别**：{gender}")
        
        st.subheader("专业技能")
        for skill in skills:
            st.write(f"✅ {skill}")
        
        st.subheader("工作经历")
        st.write("• 某某科技有限公司 - Python开发工程师 (2023-至今)")
        st.write("• 某某信息公司 - 后端开发工程师 (2021-2023)")

# ========== 4. 娱乐中心 - 视频中心 ==========
elif current_func == "娱乐中心-视频中心":
    st.title("🎬 喜羊羊与灰太狼第一部")

    # 视频数据
    video_arr = [
        {
            'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/22/49/34889204922/34889204922-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&gen=playurlv3&os=estghw&og=hw&uipk=5&oi=2067284620&trid=4c54593a709c4440adcb975bf7ddf27O&deadline=1766567848&platform=html5&mid=0&nbs=1&upsig=249ad2f3a6a819f29ecb129402597b94&uparams=e,gen,os,og,uipk,oi,trid,deadline,platform,mid,nbs&bvc=vod&nettype=1&bw=568430&dl=0&f=O_0_0&agrr=1&buvid=&build=7330300&orderid=0,3',
            'title': '喜羊羊与灰太狼-第001集、狼来了（上）'
        },
        {
            'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/72/76/27250917672/27250917672-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&og=hw&trid=0d44221c3d7449fa866a9ef537a9db5O&mid=0&uipk=5&gen=playurlv3&platform=html5&deadline=1766567946&nbs=1&oi=144233936&os=zosbv&upsig=5a86974336cb6b2e42c992a1953a0de0&uparams=e,og,trid,mid,uipk,gen,platform,deadline,nbs,oi,os&bvc=vod&nettype=1&bw=459448&dl=0&f=O_0_0&agrr=1&buvid=&build=7330300&orderid=0,3',
            'title': '喜羊羊与灰太狼-第002集、狼来了（下）'
        },
        {
            'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/31/86/27251508631/27251508631-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1766568051&os=estghw&nbs=1&mid=0&platform=html5&gen=playurlv3&og=hw&oi=2067284620&uipk=5&trid=c2f363fc7ae2492cbf2685aa2423737O&upsig=e2763a670ca0cb14f07d4c944f6ab6cd&uparams=e,deadline,os,nbs,mid,platform,gen,og,oi,uipk,trid&bvc=vod&nettype=1&bw=431582&buvid=&build=7330300&dl=0&f=O_0_0&agrr=1&orderid=0,3',
            'title': '喜羊羊与灰太狼-第003集、大小药丸'
        },
        {
            'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/59/38/27251703859/27251703859-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&oi=2067284620&os=estgoss&og=hw&uipk=5&trid=1e37cc6be0f9431d8b399afc15d73faO&deadline=1766568095&nbs=1&gen=playurlv3&platform=html5&upsig=c9f0b313bf5e8b5d99ecd91fdf4bbfa1&uparams=e,mid,oi,os,og,uipk,trid,deadline,nbs,gen,platform&bvc=vod&nettype=1&bw=441640&dl=0&f=O_0_0&agrr=1&buvid=&build=7330300&orderid=0,3',
            'title': '喜羊羊与灰太狼-第004集、昏睡果'
        },
        {
            'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/91/43/25728064391/25728064391-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=7c0d1808481c461bb0f507546782efbO&uipk=5&nbs=1&gen=playurlv3&os=estghw&og=hw&mid=0&deadline=1766568141&platform=html5&oi=1385955528&upsig=2a2c3eea7875ab858ad3ffc1d77e3665&uparams=e,trid,uipk,nbs,gen,os,og,mid,deadline,platform,oi&bvc=vod&nettype=1&bw=450605&build=7330300&dl=0&f=O_0_0&agrr=1&buvid=&orderid=0,3',
            'title': '喜羊羊与灰太狼-第005集、变色狼'
        }
    ]

    # 初始化会话状态
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0

    # 播放视频
    st.video(video_arr[st.session_state['ind']]['url'])
    st.subheader(video_arr[st.session_state['ind']]['title'])

    # 定义播放函数
    def playVideo(e):
        st.session_state['ind'] = int(e)
        st.rerun()  # 视频切换也即时刷新

    # 按每5个一组生成按钮
    group_size = 5
    for i in range(0, len(video_arr), group_size):
        cols = st.columns(min(group_size, len(video_arr)-i))
        for j, idx in enumerate(range(i, min(i + group_size, len(video_arr)))):
            with cols[j]:
                st.button(f'第{idx + 1}集', on_click=playVideo, args=(idx,))

# ========== 5. 娱乐中心 - 音乐播放器 ==========
elif current_func == "娱乐中心-音乐播放器":
    st.title("🎵 休闲音乐播放器")

    # 歌曲数据
    songs = [
        {
            "title": "日落黄昏（吉他曲）",
            "artist": "茹俊龙",
            "duration": "03:07",
            "duration_sec": 187, 
            "cover": "http://p1.music.126.net/5OI7-KYwQ6-OPazlc4cAIg==/109951169473831411.jpg?param=130y130",
            "audio": "https://music.163.com/song/media/outer/url?id=2148920607.mp3"  
        },
        {
            "title": "桜道",
            "artist": "Jusqu'à Grand-Père",
            "duration": "4:00",
            "duration_sec": 240, 
            "cover": "http://p2.music.126.net/4mL5D9TVXq6xRpeRFB--hQ==/862017116176645.jpg?param=130y130",
            "audio": "https://music.163.com/song/media/outer/url?id=756112.mp3"
        },
        {
            "title": "山行",
            "artist": "耸耸肩膀",
            "duration": "2:23",
            "duration_sec": 143, 
            "cover": "http://p1.music.126.net/k0b1eHO-XHidclBs4KaLZQ==/109951164550319919.jpg?param=130y130",
            "audio": "https://music.163.com/song/media/outer/url?id=1409713910.mp3"
        }
    ]
    
    # 初始化状态
    if "current_song_idx" not in st.session_state:
        st.session_state.current_song_idx = 0
    
    current_song = songs[st.session_state.current_song_idx]
    
    # 播放器布局
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(current_song["cover"], use_column_width=True)
    
    with col2:
        st.markdown(f"### {current_song['title']}")
        st.write(f"**歌手**: {current_song['artist']}")
        st.write(f"**时长**: {current_song['duration']}")
        
        # 控制按钮
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        with col_btn1:
            def prev_song():
                st.session_state.current_song_idx = (st.session_state.current_song_idx - 1) % len(songs)
                st.rerun()  # 上一首即时刷新
            st.button("⏮ 上一首", use_container_width=True, on_click=prev_song)
        with col_btn2:
            st.button("⏯ 播放", use_container_width=True)
        with col_btn3:
            def next_song():
                st.session_state.current_song_idx = (st.session_state.current_song_idx + 1) % len(songs)
                st.rerun()  # 下一首即时刷新
            st.button("⏭ 下一首", use_container_width=True, on_click=next_song)
    
    # 音频组件
    st.audio(current_song["audio"], format="audio/mp3")

# ========== 6. 生活服务 - 旅游探索 ==========
elif current_func == "生活服务-旅游探索":
    st.title("🌿 南宁旅游探索")
    
    # 景点数据
    spots_data = pd.DataFrame({
        "景点": ["青秀山", "南宁园博园", "大明山", "三街两巷", "南湖公园"],
        "评分": [4.8, 4.5, 4.7, 4.6, 4.4],
        "游客量(万/月)": [80, 45, 30, 65, 70]
    })
    
    # 显示地图和图表
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🗺 景点分布")
        st.map(pd.DataFrame({
            "lat": [22.8170, 22.7658, 23.4856, 22.8108, 22.8254],
            "lon": [108.3895, 108.4723, 108.3408, 108.3242, 108.3418]
        }))
    
    with col2:
        st.subheader("⭐ 景点评分")
        st.bar_chart(spots_data, x="景点", y="评分")
    
    # 详细数据
    st.subheader("📊 详细数据")
    st.dataframe(spots_data, use_container_width=True)

# ========== 7. 系统设置 - 子菜单 ==========
elif current_func.startswith("系统设置-"):
    st.title("⚙️ 系统设置")
    if current_func == "系统设置-账户管理":
        st.subheader("👤 账户管理")
        st.markdown("• 个人信息修改")
        st.markdown("• 密码重置")
        st.markdown("• 登录记录查询")
    elif current_func == "系统设置-主题设置":
        st.subheader("🎨 主题设置")
        theme = st.selectbox("选择主题", ["浅色", "深色", "护眼模式"])
        st.markdown(f"当前选中主题：{theme}")
    elif current_func == "系统设置-关于系统":
        st.subheader("ℹ️ 关于系统")
        st.markdown("• 版本号：v1.0.0")
        st.markdown("• 开发工具：Streamlit")
        st.markdown("• 更新时间：2025-12-01")

# ========== 页脚信息 ==========
st.markdown("---")
st.caption("© 2025 多功能应用中心 | 侧边目录版")
