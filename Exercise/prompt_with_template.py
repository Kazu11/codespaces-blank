from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import gradio as gr

openai = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key="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"
)
def chatbot(user_input):
    template = """Question: {question}
    please provide step by step Answer:
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])
    formated_prompt =prompt.format(question=str(user_input))
    return openai.invoke(formated_prompt).content

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch(share=True)