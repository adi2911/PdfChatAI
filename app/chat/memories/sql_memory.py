
from langchain.memory import ConversationBufferMemory
from app.chat.memories.histories.sql_history import SqlMessageHistory


def build_memory(chat_args):
    return ConversationBufferMemory(
        chat_memory=SqlMessageHistory(converstaion_id=chat_args.conversation_id),
        return_messages=True,
        memory_key="chat_history", # this is expected by ConversationQAChain
        output_key="answer"
    )
