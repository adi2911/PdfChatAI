from .chatopenai import build_llm
from functools import partial

#partial creates a function that call the function given with extra argumenrs added to partial function
llm_map={
    "gpt-4":partial(build_llm,model_name="gpt-4"),
    "gpt-3.5-turbo":partial(build_llm,model_name="gpt-3.5-turbo")
}

