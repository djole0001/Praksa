import os 
import replicate 

os.environ["REPLICATE_API_TOKEN"] = "r8_FzplpKTEDDkYjR5YBdHd6UkIIi5OqAL1TeXvV"

def with_chatbot(user_input):  
    output = replicate.run(
    "meta/llama-2-70b-chat",
    input={
            "prompt": f"{user_input}",
            "system_prompt": "You are a helpful, respectful and honest assistant. Policy structure contains attributes that are joined using Boolean operators AND and OR syntax example: attr1:value1 AND attr2:value2 OR attr3:value3. Create a policy that will satisfy given condition. Print only policy, without any explanation",
        },
    )
    
    full_response = ""
    for item in output:
        full_response += item
    # print(full_response)
    return full_response


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input == "quit":
            break 
        response_from_chatbot = with_chatbot(user_input)
        print("Chatbot: ", response_from_chatbot)
