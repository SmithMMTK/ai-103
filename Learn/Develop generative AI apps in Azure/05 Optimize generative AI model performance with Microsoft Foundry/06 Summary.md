
ในโมดูลนี้ คุณได้เรียนรู้วิธี optimize generative AI model performance ด้วยกลยุทธ์ที่ทำงานเสริมกันใน Microsoft Foundry

คุณได้เรียนรู้วิธี:

- ใช้เทคนิค prompt engineering รวมถึง system messages, few-shot learning และ model parameters เพื่อ optimize model output
- เข้าใจว่าเมื่อใดและอย่างไรจึงควร ground language model ด้วย Retrieval Augmented Generation (RAG)
- ระบุได้ว่าเมื่อใดการ fine-tuning model จะช่วยเพิ่ม behavioral consistency
- เปรียบเทียบ optimization strategies และตัดสินใจว่าเมื่อใดควรนำมาใช้ร่วมกัน

สาระสำคัญคือ prompt engineering, RAG และ fine-tuning ไม่ได้เป็นแนวทางที่แข่งขันกัน แต่เป็นกลยุทธ์เสริมกันที่แก้ปัญหาคนละมิติของ model performance ให้เริ่มจาก prompt engineering เพื่อกำกับ behavior ของโมเดล จากนั้นเพิ่ม RAG เมื่อ factual accuracy ต้องพึ่งพา domain-specific data และพิจารณา fine-tuning เมื่อคุณต้องการ style และ format ที่สม่ำเสมอ ซึ่ง prompt engineering อย่างเดียวอาจทำได้ไม่เสถียรพอ

สำหรับ travel agency scenario แนวทางที่มีประสิทธิภาพที่สุดอาจเป็นการผสานทั้งสามแบบเข้าด้วยกัน: fine-tuned model ที่คง brand voice, RAG ที่ ground responses ด้วยข้อมูลจริงจาก hotel catalog และ prompt engineering ที่เพิ่มคำสั่งเฉพาะบทสนทนาพร้อม safety guardrails

## Further reading

หากต้องการศึกษาหัวข้อในโมดูลนี้เพิ่มเติม โปรดดู resources ต่อไปนี้:

- [Getting started with customizing a large language model (LLM)](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/customizing-llms)
- [Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/prompt-engineering)
- [System message design](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/advanced-prompt-engineering)
- [Retrieval Augmented Generation in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/retrieval-augmented-generation)
- [Customize a model with fine-tuning](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/fine-tuning)
- [Microsoft Foundry fine-tuning considerations](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/fine-tuning-considerations)
- [Augment large language models with RAG or fine-tuning](https://learn.microsoft.com/en-us/azure/developer/ai/augment-llm-rag-fine-tuning)