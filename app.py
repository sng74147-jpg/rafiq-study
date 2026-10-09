import streamlit as st

st.set_page_config(
    page_title="رفيق الدراسة",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>
body {
    direction: rtl;
}
.main {
    direction: rtl;
}
h1, h2, h3, p, label {
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

st.title("📚 رفيق الدراسة")
st.subheader("منصتك البسيطة للمذاكرة والاختبارات")

st.sidebar.title("📚 القائمة")
page = st.sidebar.radio(
    "اختر القسم",
    ["الرئيسية", "🤖 مساعد الدراسة", "📝 الاختبارات", "📖 المناهج والكتب"]
)

if page == "الرئيسية":
    st.success("مرحباً بك في رفيق الدراسة 👋")
    st.write("منصة تعليمية للطلاب السودانيين تساعدك على المذاكرة والمراجعة.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🤖 مساعد الدراسة")
    with col2:
        st.info("📝 اختبارات")
    with col3:
        st.info("📖 المناهج والكتب")

elif page == "🤖 مساعد الدراسة":
    st.header("🤖 مساعد الدراسة")
    question = st.text_input("اكتب سؤالك الدراسي:")
    
    if st.button("إرسال"):
        if question:
            st.success(
                "أهلاً بك! 🌟\n\n"
                "تم استلام سؤالك. في النسخة القادمة سنربط المساعد "
                "بذكاء اصطناعي حقيقي ليشرح لك الدرس خطوة بخطوة."
            )
        else:
            st.warning("اكتب سؤالك أولاً.")

elif page == "📝 الاختبارات":
    st.header("📝 اختبار سريع")
    st.write("اختبر معلوماتك:")

    answer = st.radio(
        "ما عاصمة السودان؟",
        ["الخرطوم", "بورتسودان", "مدني", "الأبيض"]
    )

    if st.button("تصحيح الإجابة"):
        if answer == "الخرطوم":
            st.success("✅ إجابة صحيحة!")
        else:
            st.error("❌ الإجابة الصحيحة هي: الخرطوم")

elif page == "📖 المناهج والكتب":
    st.header("📖 المناهج والكتب")
    st.write("هنا سنضع كتب ومناهج السودان بصيغة PDF.")

    st.info(
        "📚 قريباً ستجد هنا المناهج والكتب مرتبة حسب الصف والمادة."
    )

st.divider()
st.caption("© 2026 رفيق الدراسة — منصة تعليمية للطلاب")
