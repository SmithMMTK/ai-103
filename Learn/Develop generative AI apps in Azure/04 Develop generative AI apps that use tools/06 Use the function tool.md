
tool _function_ ช่วยให้โมเดลของคุณเรียกใช้ developer-defined functions เพื่อดึงข้อมูลหรือ trigger actions ระหว่างการสร้าง response ได้

## What is the function tool?

function tool (function calling) ช่วยให้โมเดลตัดสินใจได้เองว่าเมื่อใดควรเรียก named tools ที่คุณ expose ไว้ในแอปพลิเคชัน โมเดลไม่ได้รัน business logic ของคุณโดยตรง แต่จะส่งกลับ structured function call จากนั้นโค้ดของคุณจึงรัน function และส่ง function output กลับไปให้โมเดล

pattern นี้เหมาะมากสำหรับเชื่อม model reasoning เข้ากับระบบจริง เช่น APIs, databases, business workflows และ utility functions

ความสามารถหลักประกอบด้วย:

- **Structured tool calls** - โมเดลส่ง function-call requests แบบชัดเจน
- **Developer-controlled execution** - แอปพลิเคชันของคุณเป็นผู้กำหนดว่า functions จะรันอย่างไรและที่ไหน
- **Reliable integration pattern** - เรียก APIs, internal services หรือ helper utilities ได้อย่างปลอดภัย
- **Multi-turn orchestration** - ส่ง tool output กลับไปแล้วให้โมเดล reasoning ต่อได้
- **Grounded responses** - คำตอบสามารถรวม live, system-generated data ได้

## Common use cases

|Use Case|Example|
|---|---|
|**System Integration**|เรียก internal API เพื่อดึงรายละเอียดบัญชีหรือคำสั่งซื้อ|
|**Task Automation**|trigger workflows เช่น การสร้าง ticket หรือการส่ง notifications|
|**Data Lookup**|query business rules หรือ reference tables ก่อนตอบ|

## A simple example

ตัวอย่างต่อไปนี้แสดงการ expose function `get_time` และให้โมเดลเรียกใช้เมื่อจำเป็น:

Python

```python
import time
from openai import OpenAI

# Function to get the current time
def get_time():
    return f"The time is {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}"


# Main function
def main():
    client = OpenAI(
        base_url={openai_endpoint},
        api_key={auth_key_or_token}
    )

    function_tools = [
        {
            "type": "function",
            "name": "get_time",
            "description": "Get the current time"
        }
    ]

    # Initialize messages with a system prompt
    messages = [
        {"role": "developer", "content": "You are an AI assistant that provides information."},
    ]

    # Loop until the user types 'quit'
    while True:
        prompt = input("\nEnter a prompt (or type 'quit' to exit)\n")
        if prompt.lower() == "quit":
            break

        # Append the user prompt to the messages
        messages.append({"role": "user", "content": prompt})

        # Get initial response
        response = client.responses.create(
            model=model_deployment,
            input=messages,
            tools=function_tools
        )

        # Append model output to the messages
        messages += response.output

        # Was there a function call?
        for item in response.output:
            if item.type == "function_call" and item.name == "get_time":
                current_time = get_time()
                messages.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": current_time
                })

                # Get a follow up response using the tool output
                response = client.responses.create(
                    model=model_deployment,
                    instructions="Answer only with the tool output.",
                    input=messages,
                    tools=function_tools
                )

        print(response.output_text)


# Run the main function when the script starts
if __name__ == '__main__':
    main()
```

ใน flow นี้ โมเดลจะตัดสินใจเองว่าเมื่อใดควรเรียก `get_time` จากนั้นโค้ดของคุณจะรัน function และโมเดลจะส่ง grounded final answer กลับมา เนื่องจากผู้ใช้สามารถป้อน prompt ใดก็ได้ โมเดลจึงต้องพิจารณาเองว่าเมื่อใดจำเป็นต้องเรียก function หากจำเป็น response ของ prompt นั้นจะมี function call รวมอยู่ และโค้ดแอปพลิเคชันต้องรองรับการทำงานดังกล่าวก่อนส่ง prompt ใหม่พร้อม output จาก function ให้โมเดลประมวลผลต่อ

output อาจมีลักษณะประมาณนี้:

```
Enter a prompt (or type 'quit' to exit)
Hello

Hello! How can I help you today?

Enter a prompt (or type 'quit' to exit)
What time is it?

The time is 2026-03-19 17:17:41.

Enter a prompt (or type 'quit' to exit)
```

prompt แรกของผู้ใช้ ("Hello") ยังไม่จำเป็นต้องใช้ function tool โมเดลจึงตอบกลับตามปกติ ส่วน prompt ที่สอง ("What time is it?") กระตุ้นให้โมเดลเลือก function `get_time` ซึ่งโมเดลระบุไว้ใน response จากนั้นโค้ดแอปพลิเคชันจึงรัน function และส่งผลลัพธ์กลับให้โมเดล ก่อนที่โมเดลจะส่ง response รอบถัดไปพร้อมผลจาก function

 Tip

ตัวอย่างนี้ใช้ function เดียวและไม่มี parameters คุณสามารถตั้งค่า tool ให้ใช้หลาย functions ได้ ทั้งแบบมีหรือไม่มี parameters หากต้องการรายละเอียดเพิ่มเติมเกี่ยวกับการระบุข้อมูลของ function โปรดดู [OpenAI developers guide](https://developers.openai.com/api/docs/guides/function-calling)

## How the function tool works

กระบวนการทั่วไปในการใช้ function tool มีดังนี้:

1. **You define tools** - ระบุ function definitions อย่างน้อยหนึ่งรายการใน tools array
2. **Model evaluates the prompt** - โมเดลพิจารณาว่าจำเป็นต้องมี function call หรือไม่
3. **Model emits a function call** - response จะมีชื่อ function และ call metadata
4. **Your app runs logic** - รัน function ที่ตรงกันในโค้ดของคุณ
5. **You return function output** - ส่ง item แบบ `function_call_output` กลับไปพร้อมผลลัพธ์
6. **Model completes the answer** - โมเดลนำผลจาก tool มาประกอบเป็น response สุดท้าย

## Best practices

- **Keep tools focused** - functions ขนาดเล็กที่มีหน้าที่เดียวควบคุมและทดสอบได้ง่ายกว่า
- **Validate function inputs** - อย่าเชื่อถือ tool arguments แบบไม่มีการตรวจสอบใน production systems
- **Handle errors safely** - ส่ง error outputs ที่ชัดเจนเพื่อให้โมเดล reasoning ต่อได้
- **Log tool usage** - ติดตาม calls, latency และ failure rates เพื่อ debugging และ governance
- **Limit sensitive operations** - กำหนดให้มี explicit authorization สำหรับ actions ที่มีผลกระทบสูง

## Limitations to know about

- โมเดลสามารถ request function calls ได้ แต่แอปพลิเคชันของคุณต้องเป็นผู้รันจริง
- อาจเกิด tool arguments ที่ไม่ถูกต้องหรือไม่คาดคิดได้ และควรมีการ validate
- Tool latency อาจเพิ่ม end-to-end response time
- Function calling ช่วยเพิ่ม reliability แต่ final outputs ยังต้องได้รับการตรวจทานสำหรับการตัดสินใจที่สำคัญ

หากใช้อย่างเหมาะสม function tool จะเปลี่ยนโมเดลจาก text generator ให้กลายเป็น orchestrator ที่โต้ตอบกับระบบจริงได้อย่างควบคุมได้และตรวจสอบย้อนหลังได้