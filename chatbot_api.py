import openai

class ChatGPTBotAPI:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        self.prompts = []  # Initialize the prompts list in the constructor.

    def initialize_gpt3(self):
        try:
            openai.api_key = self.openai_api_key
        except Exception as e:
            raise Exception("Error initializing OpenAI API:", e)

    def create_prompt(self, prompt):
        try:
            self.prompts.append(prompt)
            return len(self.prompts) - 1
        except Exception as e:
            raise Exception("Error creating prompt:", e)

    def get_response(self, prompt_index):
        try:
            if 0 <= prompt_index < len(self.prompts):
                response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=self.prompts[prompt_index],
                    max_tokens=100,
                    n=1,
                    stop=None
                )
                return response['choices'][0]['text']
            else:
                return "Invalid prompt index."
        except Exception as e:
            raise Exception("Error getting response:", e)

    def update_prompt(self, prompt_index, new_prompt):
        try:
            if 0 <= prompt_index < len(self.prompts):
                self.prompts[prompt_index] = new_prompt
                return "Prompt updated successfully."
            else:
                return "Invalid prompt index."
        except Exception as e:
            raise Exception("Error updating prompt:", e)
            
    def delete_prompt(self, prompt_index):
        try:
            if 0 <= prompt_index < len(self.prompts):
                del self.prompts[prompt_index]
                return "Prompt deleted successfully."
            else:
                return "Invalid prompt index."
        except Exception as e:
            raise Exception("Error deleting prompt:", e)