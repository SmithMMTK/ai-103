Microsoft Foundry Models มีโมเดลที่สามารถใช้ tools เพื่อค้นหาข้อมูลหรือทำงานตามภารกิจได้ คุณสามารถใช้ความสามารถด้าน tool support ในโมเดลได้ โดยระบุว่าอยากให้โมเดลใช้ tools ใดบ้างใน prompt ที่ส่งผ่าน OpenAI _Responses_ API

![Diagram of an application configuring a model to use tools.|364](https://learn.microsoft.com/en-us/training/wwl-data-ai/use-generative-ai-tools/media/tools.png)

เมื่อคุณพัฒนาแอปพลิเคชัน generative AI ด้วย Microsoft Foundry คุณสามารถค้นหาโมเดลใน Foundry Models ที่รองรับความสามารถในการเรียกใช้ tools แล้ว deploy โมเดลนั้นได้ จากนั้นคุณสามารถพัฒนา client application ที่ใช้ OpenAI Responses API เพื่อส่ง prompt ไปยังโมเดลที่ deploy แล้ว พร้อมระบุ tools ที่โมเดลสามารถใช้งานได้

> [!NOTE]
>  
> โดยค่าเริ่มต้น _model_ จะเป็นผู้ตัดสินใจเองว่าเมื่อใดควรใช้ tool (และควรใช้ตัวใด) ตามเนื้อหาใน prompt คุณสามารถกำหนดกฎการเลือก tool และใช้พารามิเตอร์ _Instructions_ (system prompt) เพื่อชี้นำการตัดสินใจนี้ได้

ตัวอย่าง tools ที่นิยมใช้ใน _Responses_ API ได้แก่:

- **code_interpreter**: Python environment ที่โมเดลสามารถสร้างและรันโค้ดได้
- **web_search**: tool ที่ช่วยให้โมเดลค้นหาข้อมูลทั่วไปบน Internet ได้ ทำให้ตอบโดยอ้างอิงข้อมูลที่อัปเดตกว่าข้อมูลที่ใช้ฝึกมา
- **file_search**: tool ที่ช่วยให้โมเดลค้นหาไฟล์เฉพาะที่คุณอัปโหลดไปยัง vector search index แบบเฉพาะทาง เพื่อให้โมเดลสามารถ ground คำตอบด้วยองค์ความรู้ที่เจาะจง
- **function**: tool ที่ช่วยให้โมเดลเรียกใช้ custom functions ในโค้ดของแอปพลิเคชันคุณได้

ในโมดูลนี้ เราจะสำรวจ tools เหล่านี้

> [!tip]
> 
> ตัวอย่างข้างต้นเป็นเพียง _some_ ส่วนหนึ่งของ tools ที่มีอยู่เท่านั้น และการพัฒนา tools สำหรับ agentic AI solutions เป็นด้านที่กำลังเติบโตอย่างต่อเนื่อง หากต้องการเรียนรู้เพิ่มเติมเกี่ยวกับ tools ที่รองรับใน OpenAI Response API โปรดดู [OpenAI developer guide](https://developers.openai.com/api/docs/guides/tools)

## Specifying tools in the _Responses_ API

คุณสามารถระบุ tools ได้ตั้งแต่หนึ่งรายการขึ้นไปในคำสั่งเรียกเมธอด `responses.create()` ขณะสร้าง response จากโมเดล ตัวอย่าง Python pseudocode ต่อไปนี้แสดงตำแหน่งที่ใช้ระบุรายการ callable tools:

Python

```python
from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

response = client.responses.create(
    model={model_deployment},
    instructions="You are a helpful AI assistant.",
    input="Find me some information about vintage computers.",
    # Specify available tools as a JSON list
    tools=[
        { 
            # A tool definition
            "type": "{tool_type}",
            "{tool-specific-setting}": "{value}",
                ...
        },
        { 
            # Another tool definition
            "type": "{another_tool_type}",
            "{tool-specific-setting}": "{value}",
                ...
        }
    ]
)
print(response.output_text)
```

 Tip

หากต้องการเรียนรู้เพิ่มเติมเกี่ยวกับการใช้ _Responses_ API เพื่อส่ง prompt ไปยังโมเดลใน Microsoft Foundry โปรดดูโมดูล [Develop a generative AI chat app with Microsoft Foundry](https://learn.microsoft.com/en-us/training/modules/foundry-sdk)

---

## Next unit: Use the code_interpreter tool