import streamlit as st
from datetime import datetime

# 页面配置
st.set_page_config(
    page_title="AI 视频标题生成工具",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义样式
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stButton > button {
        width: 100%;
        padding: 0.75rem;
        font-size: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ============ 标题和介绍 ============

st.markdown("""
# 🎬 AI 视频标题生成工具

**智能转文字 · 多风格标题 · 平台适配**

---
""")

# ============ 主要功能 ============

col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 第一步：输入内容")
    
    # 标签页选择：视频或文字
    input_method = st.radio(
        "选择输入方式",
        ["📝 输入文字", "📹 上传视频"],
        horizontal=True
    )
    
    if input_method == "📝 输入文字":
        user_text = st.text_area(
            "输入视频描述或关键词",
            placeholder="例如：这是一个关于AI技术发展的视频，介绍了最新的深度学习模型...",
            height=150
        )
        video_file = None
    else:
        user_text = None
        video_file = st.file_uploader(
            "上传视频文件",
            type=["mp4", "mov", "mkv", "avi", "webm", "flv", "wav", "m4a", "mp3"]
        )

with col2:
    st.subheader("✨ 第二步：生成标题")
    
    # 标题风格选择
    tone = st.selectbox(
        "选择标题风格",
        ["中性", "营销", "幽默", "专业"]
    )
    
    # 生成按钮
    generate_button = st.button("🚀 生成标题", use_container_width=True, type="primary")

# ============ 标题生成逻辑 ============

def get_example_titles(tone_cn):
    """根据风格返回示例标题"""
    titles_dict = {
        "中性": [
            "📌 视频内容深度解读",
            "🎯 核心要点完整指南",
            "📺 详细讲解与分析",
            "💡 关键信息总结",
            "🔍 完整内容解析"
        ],
        "营销": [
            "🚀 必看！这个秘诀改变一切",
            "💥 震撼！你不知道的真相",
            "⚡ 5分钟掌握核心技巧",
            "🎁 免费获取专业知识",
            "✨ 成功者都在看这个"
        ],
        "幽默": [
            "😂 笑到停不下来的真相",
            "🤣 这波操作绝了",
            "😆 你没看过这样的讲解",
            "🎪 娱乐性满分的干货",
            "🎭 搞笑又实用的内容"
        ],
        "专业": [
            "📊 专业分析与深度洞察",
            "🏢 企业级解决方案详解",
            "📈 数据驱动的决策指南",
            "🔬 科学方法论讲解",
            "💼 行业最佳实践分享"
        ]
    }
    return titles_dict.get(tone_cn, titles_dict["中性"])

# 处理生成按钮
if generate_button:
    if not user_text and not video_file:
        st.error("❌ 请输入内容或上传视频")
    elif video_file and user_text:
        st.error("⚠️ 请选择其中一种方式（输入文字或上传视频），不要同时选择")
    else:
        # 显示处理过程
        with st.spinner("✨ 正在生成标题..."):
            import time
            time.sleep(1)  # 模拟处理时间
            
            if video_file:
                st.info(f"📹 收到视频：{video_file.name}")
                st.markdown("""
                在 MVP 版本中，这里会调用语音识别服务。
                
                🔧 **完整版功能**：
                - 视频上传与处理
                - Whisper 语音识别
                - AI 模型标题生成
                - 平台适配
                """)
            else:
                # 生成标题
                titles = get_example_titles(tone)
                
                # 显示结果
                st.success("✅ 标题生成成功！")
                
                st.markdown(f"### 🎯 生成的标题（{tone}风格）")
                
                for i, title in enumerate(titles, 1):
                    st.write(f"**{i}. {title}**")
                
                # 显示原文
                st.markdown("---")
                st.markdown(f"**📝 原始输入**：\n{user_text[:200]}..." if len(user_text) > 200 else f"**📝 原始输入**：\n{user_text}")

# ============ 侧边栏 - 使用说明 ============

with st.sidebar:
    st.markdown("## 📖 使用说明")
    
    st.markdown("""
    ### 功能介绍
    
    **1. 输入方式**
    - 直接输入文字描述
    - 或上传视频文件
    
    **2. 标题风格**
    - 🎯 **中性**：客观、专业
    - 💰 **营销**：吸引眼球、高点击
    - 😂 **幽默**：轻松娱乐
    - 💼 **专业**：企业级、高端
    
    **3. 支持格式**
    - 视频：MP4, MOV, MKV, AVI, WebM, FLV
    - 音频：WAV, M4A, MP3
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 🚀 MVP 版本说明
    
    这是最小化可行产品版本，用于快速验证想法。
    
    **当前特性**：
    - ✅ 文字输入与处理
    - ✅ 多风格标题生成
    - ✅ 简洁的 Web 界面
    
    **计划中的功能**：
    - 🔲 语音识别（Whisper）
    - 🔲 本地 AI 模型（Ollama）
    - 🔲 平台适配
    - 🔲 用户账户系统
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 💡 技术栈
    - **前端**：Streamlit
    - **托管**：Streamlit Cloud（免费）
    - **后端**：Python
    
    ### 📊 统计
    - 部署时间：5 分钟
    - 成本：完全免费
    - 可用性：24/7
    """)
    
    # 时间戳
    st.markdown(f"---\n_最后更新：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_")

# ============ 底部信息 ============

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; padding: 1rem;'>
    <p>🎬 AI 视频标题生成工具 MVP | 完全免费 | Powered by Streamlit</p>
</div>
""", unsafe_allow_html=True)
