import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
a = """Data structure for symbols tables, representing scope information. Run-Time
Administration: Implementation of simple stack allocation scheme, storage allocation in block
structured language. Error Detection & Recovery: Lexical Phase errors, syntactic phase errors
semantic errors."""
for p in a.split(","):
    response = openai.Completion.create(
    model="text-davinci-003",
      prompt=f"write in detail about {p} with reference to Symbol Tables in compiler design, and add <p> to start of each paragraph and </p> at end of each paragraph and add ### when you have completed the indepth answer.",
    # prompt ="hi",
    temperature=0.7,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["###"]
)

    with open('output.txt', 'a',encoding="utf-8") as f:
        f.write("""<h2>"""+p+"""</h2>""")
        f.write(response.choices[0].text)

    print(response.choices[0].text)