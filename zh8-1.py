import streamlit as st
import pandas as pd
import time

# 页面配置
st.set_page_config(
    page_title="多功能应用中心 - 侧边栏导航",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS
st.markdown("""
<style>
    .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: white;
    }
    .metric-card {
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# 侧边栏导航
with st.sidebar:
    st.title("🌐 导航菜单")
    page = st.radio(
        "选择功能模块",
        ["🏠 首页概览", "📚 书籍档案", "🎬 视频中心", "🌿 旅游探索", "📄 简历生成"]
    )
    
    st.markdown("---")
    st.markdown("### 📊 系统信息")
    st.info(f"当前时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")

# 首页模块
if page == "🏠 首页概览":
    st.title("🚀 多功能应用中心")
    st.markdown("---")
    
    # 功能卡片
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.subheader("📚 书籍档案")
        st.write("Python编程学习进度管理")
        st.metric("当前进度", "72%", "+5%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.subheader("🎬 视频中心")
        st.write("喜羊羊与灰太狼全集")
        st.metric("视频数量", "8集", "在线播放")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.subheader("🌿 旅游探索")
        st.write("南宁景点数据分析")
        st.metric("景点数量", "5个", "实时推荐")
        st.markdown('</div>', unsafe_allow_html=True)

# 书籍档案模块
elif page == "📚 书籍档案":
    st.title("📚 书籍数字档案")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("📖《Python编程：从入门到实践》")
        st.markdown("""
        **书籍信息**  
        • 作者：埃里克·马瑟斯  
        • 出版社：人民邮电出版社  
        • 出版时间：2023-01-15  
        • 当前状态：在架阅读中
        """)
        
        st.subheader("📈 阅读进度")
        st.progress(72)
        st.caption("当前章节：第12章 - Web应用开发")
    
    with col2:
        st.subheader("⭐ 评分信息")
        st.metric("豆瓣评分", "9.1", "+0.2")
        st.metric("知乎评分", "9.3", "0.0")

# 其他模块实现类似...
