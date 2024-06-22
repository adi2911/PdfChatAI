from langchain_core.messages import BaseMessage
from langchain.schema import BaseChatMessageHistory

from pydantic.v1 import BaseModel
from app.web.api import (get_messages_by_conversation_id, add_message_to_conversation)





class SqlMessageHistory(BaseChatMessageHistory,BaseModel):
    converstaion_id:str

    @property
    def messages(self):
        return get_messages_by_conversation_id(self.converstaion_id)
    
    def add_message(self, message: BaseMessage):
        return add_message_to_conversation(
                conversation_id=self.converstaion_id,
                role=message.type,
                content=message.content )
    
    def clear(self):
        pass

