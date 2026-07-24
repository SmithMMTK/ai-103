การ test, deploy และ publish agents เป็นขั้นตอนสำคัญในการย้ายจาก development ไปสู่ production Microsoft Foundry มีความสามารถครบสำหรับตรวจสอบพฤติกรรม agent, deploy ไปยัง Foundry project และ publish เป็น endpoint ที่ external consumers และแอปพลิเคชันเรียกใช้งานได้

## Testing strategies for agents

การทดสอบอย่างละเอียดช่วยให้มั่นใจว่า agent ทำงานได้เชื่อถือได้ในสถานการณ์ที่หลากหลายก่อนเจอผู้ใช้จริง ทั้ง Foundry portal และ Visual Studio Code extension มี playground สำหรับการทดสอบแบบ interactive

**Using the playground effectively:**

- **Happy path testing** - ตรวจว่า agent จัดการคำขอทั่วไปที่คาดหวังได้ถูกต้อง
- **Edge case testing** - ลอง input ที่คลุมเครือ ข้อมูลไม่ครบ และคำขอที่ผิดปกติ เพื่อดูว่า agent รับมือความไม่แน่นอนได้อย่างไร
- **Boundary testing** - ยืนยันว่า agent เคารพขอบเขตที่กำหนดใน instructions โดยทดสอบคำขอนอกขอบเขต
- **Multi-turn conversation testing** - ตรวจว่า agent รักษา context ข้ามหลายรอบบทสนทนาและต่อยอดจากคำตอบก่อนหน้าได้
- **Tool invocation testing** - ตรวจว่า agent เรียกใช้ tools ที่ถูกต้องในเวลาที่เหมาะสม และรวมผลลัพธ์ได้ถูกต้อง

ควรบันทึกผลการทดสอบเพื่อใช้ติดตามการปรับปรุงและป้องกัน regression

## Deploying agents to your project

Microsoft Foundry รองรับการ deploy agents ทั้งจาก portal และ Visual Studio Code การ deploy จะบันทึก configuration ของ agent ลงใน Foundry project เพื่อให้คุณ test และ iterate ต่อได้

### Deploying from the Foundry portal

1. ไปยัง agent ของคุณใน Foundry portal
2. ตรวจสอบว่า configuration และผลทดสอบอยู่ในระดับที่พอใจ
3. เลือก **Save** จากหน้า agent
4. ยืนยัน version และ deployment settings

### Deploying from Visual Studio Code

1. เปิด agent ใน AI Toolkit
2. เลือก **Save to Foundry** เพื่อ push การเปลี่ยนแปลง configuration
3. สำหรับ hosted agents ให้เปิดเมนู **+Build** ใน developer tools แล้วเลือก **Deploy to Microsoft Foundry**
4. เลือก container configuration แล้วกดยืนยัน

ทั้งสองวิธีจะคง agent ไว้ใน project workspace เดียวกันเพื่อให้ทีมเข้าถึงและทดสอบได้

## Publishing agents to an endpoint

การ publish คือการย้าย agent จาก project workspace ไปเป็น Azure resource ที่จัดการได้ในชื่อ **Agent Application** ซึ่งทำให้ agent ถูกเรียกจากภายนอกผ่าน endpoint ที่คงที่ได้

### What publishing creates

เมื่อคุณ publish agent version, Foundry จะสร้าง:

- **Agent Application** - Azure resource ที่มี invocation URL, authentication policy และ Entra agent identity ของตัวเอง
- **Deployment** - instance ที่กำลังรันของ agent version เฉพาะภายใน application พร้อม lifecycle แบบ start/stop

ความต่างหลักระหว่าง deploy กับ publish คือขอบเขตการใช้งาน deploy คือเก็บงานไว้ใน project แต่ publish จะสร้าง endpoint เฉพาะที่ consumer ภายนอกเรียกได้โดยไม่ต้องมีสิทธิ์เข้าถึง Foundry project

### Publishing from the Foundry portal

1. ใน portal เลือก agent version ที่ต้องการ publish
2. เลือก **Publish** เพื่อสร้าง Agent Application และ deployment

### Publishing from Visual Studio Code

1. เปิด Command Palette (**Ctrl+Shift+P**) แล้วรัน **Microsoft Foundry: Deploy Hosted Agent** (สำหรับ hosted agents)
2. เลือก target workspace และ container configuration
3. ยืนยันแล้ว deploy

หลัง publish แล้ว agent จะปรากฏในส่วน **Hosted Agents (Preview)** ของ tree view ใน AI Toolkit extension

### The Agent Application endpoint

published agents จะเปิด endpoint แบบคงที่ผ่าน Responses API protocol:

```text
https://<foundry-resource-name>.services.ai.azure.com/api/projects/<project-name>/applications/<app-name>/protocols/openai/responses
```

URL นี้จะคงเดิมแม้มีการปล่อย agent version ใหม่ จึงไม่กระทบผู้ใช้งาน downstream

### Authentication and identity

Agent Applications ใช้ Microsoft Entra ID สำหรับ authentication โดยผู้เรียกต้องมีบทบาท **Azure AI User** บน Agent Application resource และไม่รองรับ API key authentication

> [!IMPORTANT]
> เมื่อคุณ publish agent, ระบบจะให้ Entra identity เฉพาะของ agent ตัวนั้น ซึ่งแยกจาก shared identity ของ project สิทธิ์ต่างๆ จะไม่ถูกโอนให้อัตโนมัติ คุณต้องกำหนด RBAC roles ให้ agent identity ใหม่สำหรับทุก resource ที่ agent ต้องเข้าถึง หากข้ามขั้นตอนนี้ tool calls ที่เคยทำงานตอนพัฒนาอาจล้มเหลวด้วย authorization errors หลัง publish

### Verifying the endpoint

หลัง publish ควรตรวจสอบว่า endpoint ใช้งานได้:

1. ขอ access token:

```azurecli
az account get-access-token --resource https://ai.azure.com
```

2. เรียก Agent Application endpoint:

```bash
curl -X POST \
  "https://<foundry-resource-name>.services.ai.azure.com/api/projects/<project-name>/applications/<app-name>/protocols/openai/responses?api-version=2025-11-15-preview" \
  -H "Authorization: Bearer <access-token>" \
  -H "Content-Type: application/json" \
  -d '{"input":"Say hello"}'
```

หากได้ `403 Forbidden` ให้ตรวจสอบว่าผู้เรียกมีบทบาท **Azure AI User** บน Agent Application resource แล้ว

### Updating published agents

เมื่อต้อง rollout agent version ใหม่:

1. แก้ไขใน development environment และทดสอบให้ครบ
2. ใน Foundry portal เลือก **Publish Updates** จาก Agent playground
3. Agent Application จะ route ทราฟฟิก 100% ไปยัง version ใหม่ให้อัตโนมัติ

endpoint URL จะไม่เปลี่ยน จึงทำให้ integration เดิมทำงานต่อได้

## Generating integration code

Microsoft Foundry VS Code extension สามารถ generate ตัวอย่าง integration code สำหรับเชื่อมแอปของคุณกับ published agent:

1. เลือก deployed agent ใน My Resources view
2. เลือก **View Code**
3. เลือกโฟลเดอร์ปลายทาง
4. extension จะสร้างโค้ดสำหรับ authentication, การเชื่อมต่อ, การส่งข้อความ และการประมวลผล response

## Integration patterns

pattern ที่พบบ่อยสำหรับการเชื่อม published agents:

- **Web applications** - ส่งข้อความผู้ใช้ไปยัง Responses API endpoint แล้วแสดงคำตอบใน UI ของคุณ พร้อมเก็บ conversation history ฝั่ง client สำหรับ multi-turn interactions
- **API-driven workflows** - เรียก endpoint จาก backend services ที่ถูก trigger โดย event หรือ schedule แล้วประมวลผล response เพื่อต่อยอด action ปลายทาง
- **Chatbot interfaces** - map user sessions เข้ากับ conversations และจัดการการแลกเปลี่ยนข้อความแบบ real-time ผ่าน endpoint
- **Background automation** - ตั้ง schedule ให้ agent calls สำหรับงานซ้ำๆ ป้อน system data ให้ agent และนำ output ไปอัปเดต business systems

## Production considerations

การรัน agents ใน production ต้องพิจารณาด้านปฏิบัติการสำคัญหลายเรื่อง:

- **Monitoring** - ติดตาม response times, อัตราความสำเร็จของการเรียก tools, รูปแบบ error และ token consumption ผ่าน Application Insights integration
- **Security** - ใช้ managed identities สำหรับ authentication, ใช้ least-privilege access และกำหนด data retention policies
- **Cost management** - ติดตาม token usage, ตั้ง response length limits และทำ rate limiting เพื่อป้องกันการพุ่งของค่าใช้จ่าย
- **Error handling** - implement retry logic แบบ exponential backoff สำหรับ transient failures, รองรับ rate limiting ด้วย backoff strategies และ validate input ก่อนส่งให้ agent
- **Conversation management** - endpoint ของ Agent Application ปัจจุบันรองรับเฉพาะ stateless Responses API จึงควรเก็บ conversation history ไว้ฝั่ง client สำหรับประสบการณ์แบบ multi-turn

---

## Next unit: Exercise - Build and deploy an AI agent