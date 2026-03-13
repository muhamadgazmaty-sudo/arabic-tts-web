import gradio as gr
from transformers import pipeline

tts = pipeline("text-to-speech", model="facebook/mms-tts-ara")

def speak(text):
    output = tts(text)
    return output["audio"]

demo = gr.Interface(
    fn=speak,
    inputs=gr.Textbox(lines=5, placeholder="اكتب نص فصحى هنا...", label="النص العربي"),
    outputs=gr.Audio(type="numpy", label="الصوت الناتج"),
    title="محول النص العربي إلى كلام طبيعي",
    description="اكتب أي نص بالعربية الفصحى وسيتم تحويله إلى صوت واضح وطبيعي."
)

demo.launch()