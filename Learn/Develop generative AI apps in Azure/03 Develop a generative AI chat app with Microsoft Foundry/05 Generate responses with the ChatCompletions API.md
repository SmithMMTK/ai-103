
OpenAI _ChatCompletions_ API ถูกใช้อย่างแพร่หลายในโมเดลและแพลตฟอร์มด้าน generative AI แม้ว่า _Responses_ API จะเป็นตัวเลือกที่แนะนำสำหรับการพัฒนาโปรเจ็กต์ใหม่ แต่คุณก็มักจะพบสถานการณ์ที่ _ChatCompletions_ API มีประโยชน์สำหรับการดูแลรักษาโค้ดหรือความเข้ากันได้ข้ามแพลตฟอร์ม

## Submitting a prompt

_ChatCompletions_ API ใช้ชุดของ _message_ objects ในรูปแบบ JSON เพื่อห่อหุ้ม prompts:

```python
completion = openai_client.chat.completions.create(
    model="gpt-4o",  # Your model deployment name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "When was Microsoft founded?"}
    ]
)

print(completion.choices[0].message.content)
```

## Retaining conversational context

ต่างจาก _Responses_ API ตรงที่ _ChatCompletions_ API ไม่มีฟีเจอร์ติดตาม response แบบมี state ในตัว หากต้องการคงบริบทของบทสนทนา คุณต้องเขียนโค้ดเพื่อติดตาม prompts และ responses ก่อนหน้าเอง

```python
# Initial messages
conversation_messages=[
    {
        "role": "system",
        "content": "You are a helpful AI assistant that answers questions and provides information."
    }
]

# Add the first user message
conversation_messages.append(
    {"role": "user",
    "content": "When was Microsoft founded?"}
)

# Get a completion
completion = openai_client.chat.completions.create(
    model="gpt-4o",
    messages=conversation_messages
)
assistant_message = completion.choices[0].message.content
print("Assistant:", assistant_text)

# Append the response to the conversation
conversation_messages.append(
    {"role": "assistant", "content": assistant_text}
)

# Add the next user message
conversation_messages.append(
    {"role": "user",
    "content": "Who founded it?"}
)

# Get a completion
completion = openai_client.chat.completions.create(
    model="gpt-4o",
    messages=conversation_messages
)
assistant_message = completion.choices[0].message.content
print("Assistant:", assistant_text)

# and so on...
```

ในแอปพลิเคชันจริง บทสนทนามักจะถูกทำงานในลูป ลักษณะดังนี้:

```python
# Initial messages
conversation_messages=[
    {
        "role": "system",
        "content": "You are a helpful AI assistant that answers questions and provides information."
    }
]

# Loop until the user wants to quit
print("Assistant: Enter a prompt (or type 'quit' to exit)")
while True:
    input_text = input('\nYou: ')
    if input_text.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    # Add the user message
    conversation_messages.append(
        {"role": "user",
        "content": input_text}
    )

    # Get a completion
    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=conversation_messages
    )
    assistant_message = completion.choices[0].message.content
    print("\nAssistant:", assistant_message)

    # Append the response to the conversation
    conversation_messages.append(
        {"role": "assistant", "content": assistant_message}
    )
```

ผลลัพธ์จากตัวอย่างนี้จะมีลักษณะใกล้เคียงดังนี้:

```text
Assistant: Enter a prompt (or type 'quit' to exit)

You: When was Microsoft founded?

Assistant: Microsoft was founded on April 4, 1975 in Albuquerque, New Mexico, USA.

You: Who founded it?

Assistant: Microsoft was founded by Bill Gates and Paul Allen.

You: quit

Assistant: Goodbye!
```

ทุกครั้งที่มี user prompt และ completion ใหม่ ระบบจะเพิ่มเข้าไปในบทสนทนา และส่งประวัติการสนทนาทั้งหมดในแต่ละรอบ

แม้ _ChatCompletions_ API จะมีความสามารถไม่ครบเท่า _Responses_ API แต่ก็เป็น API ที่ใช้งานอย่างมั่นคงใน ecosystem ของโมเดล generative AI ดังนั้นการทำความคุ้นเคยกับมันจึงเป็นประโยชน์

---

## Next unit: Exercise - Create a generative AI chat app