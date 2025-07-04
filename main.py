from src.reflection_pattern import ReflectionPattern

def invoke_reflection_pattern():
    reflection_pattern = ReflectionPattern("./src/prompts/prompt_template.toml")
    reflection_pattern()


if __name__ == "__main__":
    invoke_reflection_pattern()
