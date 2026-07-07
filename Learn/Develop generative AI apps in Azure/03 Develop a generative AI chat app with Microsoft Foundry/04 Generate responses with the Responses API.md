
OpenAI _Responses_ API รวมความสามารถจาก API ที่เดิมแยกกันสองตัว (_ChatCompletions_ และ _Assistants_) ให้เป็นประสบการณ์แบบรวมศูนย์เดียว โดยรองรับการสร้างคำตอบแบบ stateful และ multi-turn จึงเหมาะอย่างยิ่งกับแอปพลิเคชัน conversational AI คุณสามารถเข้าถึง Responses API ผ่าน OpenAI-compatible client โดยใช้ได้ทั้ง Foundry SDK และ OpenAI SDK

## Understanding the Responses API

_Responses_ API มีข้อดีหลายอย่างเมื่อเทียบกับ chat completions แบบเดิม:

- **Stateful conversations**: คง conversation context ข้ามหลาย turn ได้
- **Unified experience**: รวมรูปแบบของ chat completions และ Assistants API เข้าด้วยกัน
- **Foundry direct models**: ใช้งานกับโมเดลที่โฮสต์ตรงใน Microsoft Foundry ได้ ไม่ได้จำกัดเฉพาะ Azure OpenAI models
- **Simple integration**: เข้าถึงได้ผ่าน OpenAI-compatible client

> [!NOTE]
>  
> _Responses_ API คือแนวทางที่แนะนำสำหรับการสร้าง AI responses ในแอป Microsoft Foundry และมาแทนที่ _ChatCompletions_ API แบบเดิมในกรณีใช้งานส่วนใหญ่

## Generating a simple response

เมื่อใช้ OpenAI-compatible client คุณสามารถสร้างคำตอบด้วยเมธอด **responses.create()** ได้:

```python
# Generate a response using the OpenAI-compatible client
response = openai_client.responses.create(
    model="gpt-4.1",  # Your model deployment name
    input="What is Microsoft Foundry?"
)

# Display the response
print(response.output_text)
```

พารามิเตอร์ **input** รับค่าเป็นข้อความ prompt และโมเดลจะสร้างคำตอบโดยอิงจาก input นี้

## Understanding response structure

response object มี properties ที่ใช้งานได้จริงหลายรายการ:

- **output_text**: ข้อความคำตอบที่โมเดลสร้าง
- **id**: ตัวระบุเฉพาะของ response นี้
- **status**: สถานะของ response (เช่น "completed")
- **usage**: ข้อมูลการใช้ token (input, output และ total tokens)
- **model**: โมเดลที่ใช้สร้างคำตอบ

คุณสามารถอ่าน properties เหล่านี้เพื่อนำไปจัดการ responses ได้อย่างมีประสิทธิภาพ:

```python
response = openai_client.responses.create(
    model="gpt-4.1",
    input="Explain machine learning in simple terms."
)

print(f"Response: {response.output_text}")
print(f"Response ID: {response.id}")
print(f"Tokens used: {response.usage.total_tokens}")
print(f"Status: {response.status}")
```

### Adding instructions

นอกจาก _input_ จากผู้ใช้แล้ว คุณสามารถระบุ _instructions_ (มักเรียกว่า _system prompt_) เพื่อกำหนดแนวทางพฤติกรรมของโมเดลได้:

```python
response = client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="Explain neural networks."
)

print(response.output_text)
```

## Controlling response generation

คุณสามารถควบคุมการสร้างคำตอบด้วยพารามิเตอร์เพิ่มเติมได้:

```python
response = openai_client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="Write a creative story about AI.",
    temperature=0.8,  # Higher temperature for more creativity
    max_output_tokens=200  # Limit response length
)

print(response.output_text)
```

- **temperature**: ควบคุมความสุ่ม (0.0-2.0) ค่ายิ่งสูง output จะยิ่งสร้างสรรค์และหลากหลาย
- **max_output_tokens**: จำกัดจำนวน token สูงสุดของคำตอบ
- **top_p**: ทางเลือกแทน temperature สำหรับควบคุมความสุ่ม

## Working with Foundry direct models

เมื่อใช้ FoundrySDK หรือ AzureOpenAI client เพื่อเชื่อมต่อกับ _project_ endpoint นั้น Responses API สามารถทำงานได้ทั้งกับ Azure OpenAI models และ Foundry direct models (เช่น Microsoft Phi, DeepSeek หรือโมเดลอื่นที่โฮสต์ตรงใน Microsoft Foundry):

```python
# Using a Foundry direct model
response = openai_client.responses.create(
    model="microsoft-phi-4",  # Example Foundry direct model
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="What are the benefits of small language models?"
)

print(response.output_text)
```

## Creating conversational experiences

สำหรับสถานการณ์ conversational ที่ซับซ้อนขึ้น คุณสามารถใส่ system instructions และสร้างบทสนทนาแบบ multi-turn ได้:

```python
# First turn in the conversation
response1 = openai_client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful AI assistant that explains technology concepts clearly.",
    input="What is machine learning?"
)

print("Assistant:", response1.output_text)

# Continue the conversation
response2 = openai_client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful AI assistant that explains technology concepts clearly.",
    input="Can you give me an example?",
    previous_response_id=response1.id
)

print("Assistant:", response2.output_text)
```

ในการใช้งานจริง มักพัฒนาเป็น loop เพื่อให้ผู้ใช้พิมพ์ข้อความโต้ตอบต่อเนื่องตามแต่ละคำตอบที่ได้รับจากโมเดล:

```python
# Track responses
last_response_id = None

# Loop until the user wants to quit
print("Assistant: Enter a prompt (or type 'quit' to exit)")
while True:
    input_text = input('\nYou: ')
    if input_text.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    # Get a response
    response = openai_client.responses.create(
                model=model_name,
                instructions="You are a helpful AI assistant that explains technology concepts clearly.",
                input=input_text,
                previous_response_id=last_response_id
    )
    assistant_text = response.output_text
    print("\nAssistant:", assistant_text)
    last_response_id = response.id 
```

ผลลัพธ์จากตัวอย่างนี้จะมีลักษณะใกล้เคียงดังนี้:


```text
Assistant: Enter a prompt (or type 'quit' to exit)

You: What is machine learning?

Assistant: Machine learning is a type of artificial intelligence (AI) that enables computers to learn from data and improve their performance over time without being explicitly programmed. It involves training algorithms on large datasets to recognize patterns, make predictions, or take actions based on those patterns. This allows machines to become more accurate and efficient in their tasks as they are exposed to more data.

You: Can you give me an example?

Assistant: Certainly! Let's look at a simple example of supervised learning—predicting house prices based on features like size, location, and number of rooms.
Imagine you want to build a machine learning model that can predict the price of a house based on various factors.
...
    { the example provided in the model response may be extensive}
...

You: quit

Assistant: Goodbye!
```

เมื่อผู้ใช้ป้อน input ใหม่ในแต่ละ turn ข้อมูลที่ส่งให้โมเดลจะประกอบด้วย _Instructions_ system message, _input_ จากผู้ใช้ และ _previous_ response ที่ได้จากโมเดลก่อนหน้า วิธีนี้ทำให้ input ใหม่มีบริบทอ้างอิงจากคำตอบก่อนหน้าอย่างต่อเนื่อง

### Alternative: Manual conversation chaining

คุณสามารถจัดการบทสนทนาแบบ manual ได้ โดยสร้าง message history เอง วิธีนี้ช่วยให้ควบคุมบริบทที่ต้องการส่งเข้าไปได้ละเอียดขึ้น:

```python
try:
    # Start with initial message
    conversation_history = [
        {
            "type": "message",
            "role": "user",
            "content": "What is machine learning?"
        }
    ]

    # First response
    response1 = openai_client.responses.create(
        model="gpt-4.1",
        input=conversation_history
    )

    print("Assistant:", response1.output_text)

    # Add assistant response to history
    conversation_history += response1.output

    # Add new user message
    conversation_history.append({
        "type": "message",
        "role": "user", 
        "content": "Can you give me an example?"
    })

    # Second response with full history
    response2 = openai_client.responses.create(
        model="gpt-4.1",
        input=conversation_history
    )

    print("Assistant:", response2.output_text)

except Exception as ex:
    print(f"Error: {ex}")
```

แนวทางแบบ manual นี้เหมาะเมื่อคุณต้องการ:

- ปรับแต่งได้ว่าจะใส่ข้อความใดบ้างใน context
- ทำ conversation pruning เพื่อควบคุม token limits
- จัดเก็บและเรียกคืน conversation history จากฐานข้อมูล

### Retrieving specific previous responses

Responses API จะเก็บ response history ทำให้คุณเรียกดู responses ก่อนหน้าได้:

```python
try:   

    # Retrieve a previous response
    response_id = "resp_67cb61fa3a448190bcf2c42d96f0d1a8"  # Example ID
    previous_response = openai_client.responses.retrieve(response_id)

    print(f"Previous response: {previous_response.output_text}")

except Exception as ex:
    print(f"Error: {ex}")
```

### Context window considerations

พารามิเตอร์ **previous_response_id** ใช้เชื่อม responses เข้าด้วยกัน เพื่อคง conversation context ข้ามหลาย API calls

สิ่งสำคัญที่ต้องทราบคือ การเก็บ conversation history จะเพิ่มการใช้ token ได้ ในการรันหนึ่งครั้ง active context window อาจประกอบด้วย:

- System instructions (instructions, safety rules)
- prompt ปัจจุบันของคุณ
- Conversation history (ข้อความก่อนหน้าของ user + assistant)
- Tool schemas (functions, OpenAPI specs, MCP tools ฯลฯ)
- Tool outputs (search results, code interpreter output, files)
- memory หรือ documents ที่ดึงมาใช้ (จาก memory stores, RAG, file search)

องค์ประกอบทั้งหมดนี้จะถูกนำมาต่อรวมกัน, tokenized และส่งไปยังโมเดลพร้อมกันในทุก request โดย SDK ช่วยจัดการ state ให้ได้ แต่ไม่ได้ทำให้ค่าใช้ token ถูกลงโดยอัตโนมัติ

## Creating responsive chat apps

การสร้าง responses จากโมเดลอาจใช้เวลาพอสมควร ขึ้นกับปัจจัยอย่างโมเดลที่ใช้, ขนาดของ context window และความยาวของ prompt ผู้ใช้อาจรู้สึกหงุดหงิดหากแอปดูเหมือน "ค้าง" ระหว่างรอคำตอบ ดังนั้นควรคำนึงถึง app responsiveness ในการพัฒนา

### Streaming responses

สำหรับคำตอบที่ยาว คุณสามารถใช้ streaming เพื่อรับ output แบบทยอยได้ ทำให้ผู้ใช้เห็นคำตอบที่กำลังก่อตัวได้ทันที:

```python
stream = openai_client.responses.create(
    model="gpt-4.1",
    input="Write a short story about a robot learning to paint.",
    stream=True
)

for event in stream:
    print(event, end="", flush=True)
```

หากคุณติดตาม conversation history ระหว่าง streaming คุณสามารถดึง response ID ได้เมื่อ stream สิ้นสุด ดังนี้:

```python
stream = openai_client.responses.create(
    model="gpt-4.1",
    input="Write a short story about a robot learning to paint.",
    stream=True
)
for event in stream:
                if event.type == "response.output_text.delta":
                    print(event.delta, end="")
                elif event.type == "response.completed":
                    response_id = event.response.id
```

### Async usage

สำหรับแอปที่ต้องการประสิทธิภาพสูง คุณสามารถใช้ asynchronous client เพื่อทำ non-blocking API calls ได้ การใช้งานแบบ asynchronous เหมาะกับ request ที่ใช้เวลานาน หรือกรณีที่ต้องจัดการหลาย requests พร้อมกันโดยไม่บล็อกแอปของคุณ วิธีใช้คือ import `AsyncOpenAI` แทน `OpenAI` และใช้ `await` กับแต่ละ API call:

```python
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    base_url="https://<resource-name>.openai.azure.com/openai/v1/",
    api_key=token_provider,
)

async def main():
    response = await client.responses.create(
        model="gpt-4.1",
        input="Explain quantum computing briefly."
    )
    print(response.output_text)

asyncio.run(main())
```

Async streaming ทำงานในลักษณะเดียวกัน:

```python
async def stream_response():
    stream = await client.responses.create(
        model="gpt-4.1",
        input="Write a haiku about coding.",
        stream=True
    )

    async for event in stream:
        print(event, end="", flush=True)

asyncio.run(stream_response())
```

เมื่อใช้ _Responses_ API ผ่าน Microsoft Foundry SDK คุณจะสามารถสร้างแอป conversational AI ที่ซับซ้อนได้ โดยยังคงบริบทการสนทนา รองรับโมเดลหลายประเภท และมอบประสบการณ์ใช้งานที่ตอบสนองได้ดี

---

## Next unit: Generate responses with the ChatCompletions API

[](https://learn.microsoft.com/en-us/training/modules/foundry-sdk/03-microsoft-foundry-sdk/)[](https://learn.microsoft.com/en-us/training/modules/foundry-sdk/05-openai-api/)